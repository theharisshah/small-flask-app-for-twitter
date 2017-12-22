import os
from flask import Flask, render_template, request, redirect, url_for
import tweepy

consumer_key = "JQjgBxhCbB1t4mdQr8Xkxxra6"
consumer_secret = "CGzfFjVyqT4FXwVsYIUlmocFdSBydKexDZ8m3shGewJBK9fIBf"
access_token = "61405344-c5PlnzQXr5CDGTxGo8iDDgtyTjlbfRdX165XssPDn"
token_secret = "axnj3hkFyn9M5WPSQ1GyTrgyUFjXrmjO4kxrfE3nJAWpe"
# session = dict()

# callback="http://localhost:5000/callback"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, token_secret)
api = tweepy.API(auth)

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('search.html', urlIMG="http://www.schoolchalao.com/app/webroot/img/no-user-image.png")

@app.route("/update", methods=['POST'])
def update():
    twat=request.form['updtestat']
    api.update_status(twat)
    return render_template("search.html", done= " Tweet Sucessfully Posted", urlIMG="http://www.schoolchalao.com/app/webroot/img/no-user-image.png")

@app.route("/search", methods=['POST'])
def search():
    twat=request.form['searchstat']
    guser=api.get_user(twat)
    followers = str(guser.followers_count)
    guname = str(guser.name)
    descrip = guser.description
    imgurl1 = guser.profile_image_url
    y=imgurl1.replace('normal', '400x400')
    twitterURL= "https://twitter.com/"
    newURL = twitterURL + (twat)
    loc = str(guser.location)
    # followww = guser.following
    actdate = guser.created_at
    joind = actdate.strftime('%B, %Y')
    return render_template("search.html", fol_count= followers, user_name= guname, urlIMG=y, urlPRO=newURL, location=loc, joined=joind)
if __name__ == "__main__":

    app.run(debug=True)
