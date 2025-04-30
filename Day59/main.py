from flask import Flask, render_template
import requests

response = requests.get("https://api.npoint.io/3eda880271a88ac6a482")
data = response.json()

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("index.html", posts=data)

@app.route("/about")
def about_page():
    return render_template("about.html")

@app.route("/contact")
def contact_page():
    return render_template("contact.html")

@app.route("/post/<int:index>")
def blog_post(index):
    requested_post = None
    for i in data:
        if i["id"] == index:
            requested_post = i
    return render_template("post.html", post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)