from wtforms import validators
from wtforms import StringField, TextAreaField
from wtforms import Form


class RegisterForm(Form):
    name = StringField(
        u'İsim', [validators.InputRequired(), validators.length(max=10)])
    surname = StringField(
        u'Soyisim', [validators.InputRequired(), validators.length(max=10)])
    email = StringField(
        u'Soyisim', [validators.email(), validators.InputRequired(), validators.length(max=10)])
    password = StringField(
        u'Soyisim', [validators.InputRequired(), validators.length(max=10)])
    password_again = StringField(
        u'Soyisim', [validators.InputRequired(), validators.length(max=10)])
    address = TextAreaField(u'Mail adresi', [
                            validators.optional(), validators.length(max=200)])
