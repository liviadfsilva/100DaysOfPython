from flask import Flask, render_template, request
import requests
import datetime

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
    if request.method == 'GET':
        return render_template("contact.html")
    elif request.method == 'POST':
        name = request.form["name"]
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
        print(name + "\n" + email + "\n" + phone + "\n" + message + "\n")
        return "<h1>Message successfully sent!<h1>"
    else:
        return "Try again later."

@app.route("/post/<int:index>")
def blog_post(index):
    requested_post = None
    for i in data:
        if i["id"] == index:
            requested_post = i
    return render_template("post.html", post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)