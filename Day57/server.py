from flask import Flask, render_template
from datetime import datetime
import requests

app = Flask(__name__)

@app.route("/")
def home():
    current_year = datetime.now().strftime("%Y")
    return render_template("index.html", year=current_year)

@app.route("/guess/<name>")
def guess(name):
    gender_url = f"https://api.genderize.io?name={name}"
    gender_response = requests.get(gender_url)
    gender_data = gender_response.json()
    gender = gender_data["gender"]
    
    return render_template("guess.html", person_name=name, person_gender=gender)

if __name__ == "__main__":
    app.run(debug=True)