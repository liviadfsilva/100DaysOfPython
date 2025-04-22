from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    blog_response = requests.get(blog_url)
    blog_data = blog_response.json()
    return render_template("index.html", posts=blog_data)

@app.route("/post/<id>")
def blog_post(id):
    return render_template("post.html")

if __name__ == "__main__":
    app.run(debug=True)
