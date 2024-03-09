from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField
from wtforms import validators
import email_validator
from flask_bootstrap import Bootstrap5

class LoginForm(FlaskForm):
    email = EmailField(label='Email', validators=[validators.Email()])
    password = PasswordField(label='Password', validators=[validators.Length(min=8), validators.DataRequired()])
    submit = SubmitField(label='Log In')


app = Flask(__name__)
app.secret_key = "secretstring"
bootstrap = Bootstrap5(app)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login/", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == "admin@gmail.com" and login_form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", form=login_form)


if __name__ == '__main__':
    app.run(port=8000, debug=True)
