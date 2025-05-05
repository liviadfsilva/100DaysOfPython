from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email
from flask_bootstrap import Bootstrap4
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
bootstrap = Bootstrap4(app)

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
    if login_form.validate_on_submit():
        if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", form=login_form)

if __name__ == "__main__":
    app.run(debug=True, port=5001)