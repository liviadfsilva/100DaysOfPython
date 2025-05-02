from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email(message=None, granular_message=True)])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8, max=16, message=None)])
    submit = SubmitField(label='Log In')
    
app.secret_key = os.getenv("APP_SECRET_KEY")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    login_form.validate_on_submit()
    return render_template("login.html", form=login_form)

if __name__ == "__main__":
    app.run(debug=True)