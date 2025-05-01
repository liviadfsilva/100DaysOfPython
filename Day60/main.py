from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def receive_data():
    error = None
    if request.method == 'POST':
        name = request.form["fname"]
        password = request.form['password']
        return f"<h1>Name: {name}, Password:{password}<h1>"
    else:
        error = 'Invalid username/password'
        return error

if __name__ == "__main__":
    app.run(debug=True)