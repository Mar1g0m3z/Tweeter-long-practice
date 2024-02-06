from wtforms import StringField, SubmitField
from flask_wtf import FlaskForm

from wtforms.validators import DataRequired


class NewTweet(FlaskForm):
    author = StringField("Author", validators=[DataRequired()])
    tweet = StringField("Tweet", validators=[DataRequired()])
    submit = SubmitField("Submit")
