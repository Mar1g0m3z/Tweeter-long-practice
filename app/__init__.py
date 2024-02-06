# !!START
from flask import (Flask, render_template, redirect)
from .config import Config
from .tweets import tweets
from random import randint
from datetime import datetime
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


@app.route("/new", methods=['GET', 'POST'])
def new_tweet():
    form = NewTweet()
    if form.validate_on_submit():
        new_id = len(tweets) + 1
        new_tweet = {
            "id": new_id,
            "author": form.author.data,
            "tweet": form.tweet.data,
            "date": datetime.now().strftime("%m/%d/%y"),
            "likes": 0
        }
        tweets.append(new_tweet)
        return redirect("/feed")
    return render_template("new_tweet.html", form=form, errors=form.errors)


# comment
