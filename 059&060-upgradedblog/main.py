from flask import Flask, render_template, request
import requests
from datetime import datetime
import smtplib

current_year = datetime.now().year

blog_posts = requests.get("https://api.npoint.io/689ab1121ba448547db7").json()

EMAIL = ""
PASSWORD = ""


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", all_posts=blog_posts, year=current_year)

@app.route('/about/')
def about():
    return render_template("about.html", year=current_year)

@app.route('/contact/', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form 
        send_email(data["name"], data["email"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", year=current_year)

def send_email(name, email, message):
    email_message = f"Subject: New Message\n\nName: {name}\nEmail: {email}\nMessage: {message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        connection.sendmail(EMAIL, EMAIL, email_message)

@app.route('/post/<int:index>')
def post(index):
    requested_post = None
    for post in blog_posts:
        if post["id"] == index:
            requested_post = post
    return render_template("post.html", post=requested_post, year=current_year)

@app.route('/reviews/')
def reviews():
    return render_template("reviews.html", all_posts=blog_posts, year=current_year)

if __name__ == "__main__":
    app.run(port=8000, debug=True)