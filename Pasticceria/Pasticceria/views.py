"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, url_for, request, flash, session, redirect
from flask_bootstrap import Bootstrap
from Pasticceria import app
from Pasticceria.forms import SignInForm, AddCakeForm, IngredientForm
import pyrebase
import json

app.config['SECRET_KEY'] = 'ai4cioccolati'
app.debug = True

config = {
    "apiKey": "",
    "authDomain": "",
    "databaseURL": "",
    "projectId": "",
    "storageBucket": "",
    "messagingSenderId": "",
    "appId": "",
    "measurementId": ""
}

firebase = pyrebase.initialize_app(config)
bootstrap = Bootstrap(app)
db = firebase.database()
auth = firebase.auth()
today = datetime.today().strftime('%Y-%m-%d')

user = {
    'id':'',
    'name':'',
    'email':'',
    'password':''
    }

def reset_user():
    user['email'] = ''
    user['password'] = ''
    user['id'] = ''
    user['name'] = ''

def days_between(d1, d2):
    d1 = datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    return abs((d2 - d1).days)

def is_logged():
    if user['id'] != '':
        return 'true'
    return 'false'

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    cakes = db.child("Cakes").get().val()
    return render_template(
        'index.html',
        title='Home',
        year=datetime.now().year,
        is_logged=is_logged(),
        day=today,
        cakes=cakes
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        is_logged=is_logged(),
        message='Contattaci per i tuoi ordini.'
    )

@app.route('/signIn', methods=['GET', 'POST'])
def signIn():
    form = SignInForm()
    if form.is_submitted():
        result = request.form
        try:
            email = result['email']
            password = result['password']
            user['id'] = auth.sign_in_with_email_and_password(email, password)
            user['email'] = email
            user['password'] = password
            user['name'] = (email.split('.'))[0].capitalize()
            return redirect(url_for('backoffice'))
        except:
            reset_user()
            flash("Errore durante l'accesso", 'error')

    """Renders the sign in page."""
    return render_template(
        'signIn.html',
        title='Accedi',
        year=datetime.now().year,
        is_logged=is_logged(),
        form=form
    )

@app.route('/signOut', methods=['GET', 'POST'])
def signOut():
    reset_user()
    flash('Sei uscito con successo!')
    """Renders the sign out page."""
    return redirect(url_for('home'))

@app.route('/backoffice', methods=['GET', 'POST'])
def backoffice():
    if not is_logged():
        return redirect(url_for('home'))
    else:
        if request.method == 'POST':
            new = request.json
            if new:
                for n in new:
                    x = new[n]
                    if x['Availability'] == 0:
                        db.child("Cakes").child(n).remove()
                    else:
                        db.child("Cakes").child(n).update(x)
                return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}
        cakes = db.child("Cakes").get().val()
        for ck in cakes:
            c = cakes[ck]
            if days_between(today, c['Day']) > 2:
                db.child("Cakes").child(ck).remove()

        """Renders the backoffice page."""
        return render_template(
            'backoffice.html',
            name=user['name'],
            title='Backoffice',
            year=datetime.now().year,
            is_logged=is_logged(),
            day=today,
            cakes=cakes
        )

@app.route('/addCake', methods=['GET', 'POST'])
def addCake():
    if not is_logged():
        redirect(url_for('home'))
    else:
        scroll = 'top-navbar'
        form = AddCakeForm()
        if form.is_submitted():
            result = request.form
            if request.form.get("AddField", False):
                form.ingredients.append_entry()
                scroll = 'add-new-field'
            else:
                cake = result['name']
                price = result['price']
                availability = result['availability']
                ingredients=[]
                for f in form.ingredients:
                    ingredients.append(f)

                r = {
                    "Price" : price,
                    "Availability" : availability,
                    "Day" : today
                    }
                db.child('Cakes').child(cake.capitalize()).update(r)
                s = {}
                for i in ingredients:
                    s[(i['name'].data).capitalize()] = {
                        "Quantity" : i['quantity'].data,
                        "Unit" : i['unit'].data
                        }
                db.child('Cakes').child(cake.capitalize()).child('Ingredients').update(s)
                return redirect(url_for('backoffice'))
        
        """Renders the add-a-cake page."""
        return render_template(
            'addCake.html',
            title='Backoffice',
            year=datetime.now().year,
            is_logged=is_logged(),
            form=form,
            scroll=scroll
        )
