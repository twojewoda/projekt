from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField



class AddForm(FlaskForm):

    name = StringField('Imie szczeniaka:')
    submit = SubmitField('Dodaj szczeniaka')

class AddOwnerForm(FlaskForm):

    name = StringField('Imie właściciela:')
    pup_id = IntegerField("Id szczeniaka: ")
    submit = SubmitField('Dodaj właściciela')

class DelForm(FlaskForm):

    id = IntegerField('Id szczeniaka do wypisania z listy:')
    submit = SubmitField('Wypisz szczeniaka')
