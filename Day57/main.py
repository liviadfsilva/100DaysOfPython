from flask import Flask, render_template, redirect, url_for
from post import Post

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('home'))

@app.route('/blog')
def home():
    blog = Post()
    return render_template("index.html", posts=blog.data)

@app.route("/post/<int:index>")
def blog_post(index):
    test = Post()
    return render_template("post.html", index=test.show_post(index))

if __name__ == "__main__":
    app.run(debug=True)
