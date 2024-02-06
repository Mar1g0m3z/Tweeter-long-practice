from wtforms import StringField, SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired


class NewTweet(FlaskForm):
    author = StringField("Author", validators=[InputRequired()])
    tweet = StringField("Tweet", validators=[InputRequired()])
    submit = SubmitField("Submit")
