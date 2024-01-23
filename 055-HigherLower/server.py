from flask import Flask
import random

number = random.randint(1, 9)

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Guess a number between 0 and 9</h1>' \
            '<img src="https://media.giphy.com/media/xUn3CftPBajoflzROU/giphy.gif" width=300>'

@app.route("/<int:guess>")
def guess_number(guess):
    if guess > number:
        return "<h1>Too high, try again!</h1>"

    elif guess < number:
        return "<h1>Too low, try again!</h1>"

    else:
        return "<h1>You found me!</h1>"

if __name__ == "__main__":
    app.run(port=8000, debug=True)