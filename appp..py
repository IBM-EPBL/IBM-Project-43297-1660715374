from ast import Index
import base64
from flask import Flask;
render_template
base64.html
"<!DOCTYPE html>"
"<html>"
"<head>"
{"% block head %} {% endblock %"}
"</head>"
"<body>"

"<a href="/">HOME</a>"
"<a href="/"blog:>BLOG</a>"

"<a href="/"signin:>SIGNIN:</a>"
Index.html
{"% extends 'base.html' %"}

{"% block head%"}
"<title>Home Page</title>"
{"% endblock %"}
    
{"% block body%"}
"<h1>This is a Heading</h1>"
"<p>Hello, form Home page</p>"
{"% endblock%"}

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/blog")
def blog():
    return render_template('blog.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/signin')
def signin():
    return render_template('signin.html')