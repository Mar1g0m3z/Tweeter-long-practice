# !!START
from flask import (Flask, render_template)
from .config import Config
from .tweets import tweets
from random import randint

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
