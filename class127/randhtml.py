# app.py
import flask
import os
import random

app = flask.Flask(__name__)

@app.route('/')  
def index(): 
    r=random.randint(1, 100)
    return "<h1>" + str(r) + "</h1>"
   # return flask.render_template("index.html", 
   #     random_num=r)

app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug=True
)