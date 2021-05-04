"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, url_for, request, flash, session, redirect
from Pasticceria import app
from Pasticceria.forms import SignInForm, AddCakeForm, IngredientForm
import pyrebase

app.config['SECRET_KEY'] = 'ai4cioccolati'

config = {
    "apiKey": "AIzaSyAhNhNVjG475NUV13qcUlzGuiK51eSbdbM",
    "authDomain": "pasticceria-b7f01.firebaseapp.com",
    "databaseURL": "https://pasticceria-b7f01-default-rtdb.europe-west1.firebasedatabase.app",
    "projectId": "pasticceria-b7f01",
    "storageBucket": "pasticceria-b7f01.appspot.com",
    "messagingSenderId": "1079999197910",
    "appId": "1:1079999197910:web:a923704d223639af9b8f77",
    "measurementId": "G-CHL8888R9S"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()
auth = firebase.auth()
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

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    cakes = db.child("Cakes").get()
    return render_template(
        'index.html',
        title='Home',
        year=datetime.now().year,
        cakes=cakes.val()
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Contattaci per i tuoi ordini.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Qualcosa su di noi.'
    )

@app.route('/signIn', methods=['GET', 'POST'])
def signIn():
    """Renders the sign in page."""
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
    return render_template(
        'signIn.html',
        title='Accedi',
        year=datetime.now().year,
        form=form
    )

@app.route('/signOut', methods=['GET', 'POST'])
def signOut():
    """Renders the sign out page."""
    reset_user()
    flash('Sei uscita con successo!')
    return redirect(url_for('home'))

@app.route('/backoffice', methods=['GET', 'POST'])
def backoffice():
    if user['id'] == '':
        return redirect(url_for('home'))
    else:
        """Renders the backoffice page."""
        cakes = db.child("Cakes").get()
        return render_template(
            'backoffice.html',
            name=user['name'],
            title='Backoffice',
            year=datetime.now().year,
            cakes=cakes.val()
    )

@app.route('/addCake', methods=['GET', 'POST'])
def addCake():
    if user['id'] == '':
        redirect(url_for('home'))
    else:
        """Renders the add-a-cake page."""
        form = AddCakeForm()
        if form.is_submitted():
            result = request.form
            cake = result['name']
            price = result['price']
            availability = result['availability']
            ingredients=[]
            for f in form.ingredients:
                ingredients.append(f)

            r = {
                "Price" : price,
                "Availability" : availability
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

        return render_template(
            'addCake.html',
            title='Backoffice',
            year=datetime.now().year,
            form=form
        )