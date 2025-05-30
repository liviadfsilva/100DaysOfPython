from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("APP_SECRET_KEY")
Bootstrap5(app)

class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Cafe Location on Google Maps', validators=[DataRequired(), URL()])
    open = StringField('Opening Time, e.g. 8AM', validators=[DataRequired()])
    closed = StringField('Closing Time, e.g. 5:30PM', validators=[DataRequired()])
    coffee = SelectField('Coffee Rating', choices=[('☕️'), ('☕️☕️'), ('☕️☕️☕️'), ('☕️☕️☕️☕️'), ('☕️☕️☕️☕️☕️')])
    wifi = SelectField('Wifi Strength Rating', choices=[('✘'), ('💪'), ('💪💪'), ('💪💪💪'), ('💪💪💪💪'), ('💪💪💪💪💪')])
    power_socket = SelectField('Power Socket Availability', choices=[('✘'), ('🔌'), ('🔌🔌'), ('🔌🔌🔌'), ('🔌🔌🔌🔌'), ('🔌🔌🔌🔌🔌')])
    submit = SubmitField('Submit')

# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")

@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open('Day62/cafe-data.csv', mode="a", encoding='utf-8') as new_cafe:
            new_cafe.write(f"\n{form.cafe.data},"
                           f"{form.location.data},"
                           f"{form.open.data},"
                           f"{form.closed.data},"
                           f"{form.coffee.data},"
                           f"{form.wifi.data},"
                           f"{form.power_socket.data},")
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)

@app.route('/cafes')
def cafes():
    with open('Day62/cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)

if __name__ == '__main__':
    app.run(debug=True, port=5001)