from flask_wtf import FlaskForm
from wtforms import *
from wtforms.fields.html5 import EmailField

class SignInForm(FlaskForm):
    email = EmailField('Email')
    password = PasswordField('Password')
    submit = SubmitField('Accedi')

class IngredientForm(FlaskForm):
    name = StringField('Ingrediente')
    quantity = IntegerField('Quantità')
    unit = SelectField('Unità di misura', choices=[('grammi', 'grammi'),
                                                   ('chilogrammi', 'chilogrammi'),
                                                   ('litri', 'litri'),
                                                   ('unità', 'unità'),
                                                   ('quanto basta','quanto basta')
                                                  ])

class AddCakeForm(FlaskForm):
    name = StringField('Torta')
    price = DecimalField('Prezzo')
    availability = IntegerField('Disponibilità')
    ingredients = FieldList(FormField(IngredientForm), min_entries=3, max_entries=15)
    add = SubmitField('Aggiungi')