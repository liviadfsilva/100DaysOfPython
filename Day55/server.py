from flask import Flask
import random

random_number = random.randint(0, 9)
app = Flask(__name__)

@app.route('/')
def game():
    return '<h1>Guess a number between 0 and 9</h1><img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" width=200>'

@app.route('/<int:chosen_number>')
def number(chosen_number):
    if chosen_number < random_number:
        return "<h1 style='color:Tan'>Too low. Try again!</h1><img src='https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExZW53b21pZmF4Ynlia2VxdHVzYnA5cHZxcDB3NGNtajN6M2JsdWIyYyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/LYd7VuYqXokv20CaEG/giphy.gif'>"
    elif chosen_number > random_number:
        return "<h1 style='color:SaddleBrown'>Too high. Try again!</h1><img src='https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExcWk5NDgzNXg1MzJ4dHpkYXNzenJpbWY4cm5jeTFlc2xmbmNsbWwyMCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/NqZn5kPN8VVrW/giphy.gif'>"
    else:
        return "<h1 style='color:MediumVioletRed'>You guessed it right!</h1><img src='https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExb3B6YWJlZmZoZjZwd244YmdncGRtMzg0bHF3bWoydmp4M2JpaWxmMSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/j3N408mLpIXWU/giphy.gif'>"

if __name__ == "__main__":
    app.run(debug=True)