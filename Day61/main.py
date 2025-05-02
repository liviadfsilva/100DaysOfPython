from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label='Log In')
    
app.secret_key = os.getenv("APP_SECRET_KEY")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login")
def login():
    login_form = LoginForm()
    return render_template("login.html", form=login_form)

if __name__ == "__main__":
    app.run(debug=True)