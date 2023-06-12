from wtforms import validators
from wtforms import StringField, TextAreaField
from wtforms import Form


class KayitForm(Form):
    name = StringField(
        u'İsim', [validators.InputRequired(), validators.length(max=50)])
    surname = StringField(
        u'Soyisim', [validators.InputRequired(), validators.length(max=50)])
    email = StringField(
        u'Mail adresi', [validators.Email(), validators.InputRequired(), validators.length(max=100)])
    password = StringField(
        u'Parola', [validators.InputRequired(), validators.length(max=50)])
    confirm = StringField(
        u'Parola tekrar', [validators.InputRequired(), validators.EqualTo("password", message="Parolalar eşleşmiyor"), validators.length(max=50)])
    address = TextAreaField(u'Adres', [
                            validators.optional(), validators.length(max=200)])

class GirisForm(Form):
    email = StringField(
        u'Mail', [validators.Email(),validators.InputRequired(), validators.length(max=100)])
    
    password = StringField(
        u'Parola', [validators.InputRequired(), validators.length(max=50)])
    