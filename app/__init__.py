# !!START
from flask import (Flask, render_template)
from .config import Config
from .tweets import tweets
from random import randint
from .form.form import NewTweet

app = Flask(__name__)

app.config.from_object(Config)
# !!END


@app.route("/")
def index():
    ri = randint(0, 4)
    print(ri)
    return render_template("index.html", tweet=tweets[ri])


@app.route("/feed")
def feed():
    return render_template("feed.html", tweets=tweets)

@app.route("/new")
def new_tweet():
    form = NewTweet()
    return render_template("new_tweet.html", form=form)

##comment
