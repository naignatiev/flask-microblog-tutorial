from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

from app.validators import PasswordRestrictions


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), PasswordRestrictions()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Sign in')
