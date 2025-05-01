from flask import Flask, render_template, request
import requests
import datetime
import smtplib

OWN_EMAIL = "youremail@example.com"
OWN_PASSWORD = "yourpassword"

response = requests.get("https://api.npoint.io/3eda880271a88ac6a482")
data = response.json()

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("index.html", posts=data)

@app.context_processor
def inject_year():
    return {'copyright_year': datetime.datetime.now().strftime('%Y')}

@app.route("/about")
def about_page():
    return render_template("about.html")

@app.route("/contact", methods=["GET", "POST"])
def contact_page():
    if request.method == 'POST':
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])        
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)

def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(OWN_EMAIL, OWN_PASSWORD)
        connection.sendmail(OWN_EMAIL, OWN_EMAIL, email_message)

@app.route("/post/<int:index>")
def blog_post(index):
    requested_post = None
    for i in data:
        if i["id"] == index:
            requested_post = i
    return render_template("post.html", post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)