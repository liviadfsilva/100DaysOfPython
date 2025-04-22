from flask import Flask, render_template
from post import Post

app = Flask(__name__)

@app.route('/')
def home():
    blog = Post()
    return render_template("index.html", posts=blog.data)

@app.route("/post/<id>")
def blog_post(id):
    return render_template("post.html")

if __name__ == "__main__":
    app.run(debug=True)
