from flask import Flask, render_template
import requests
from datetime import datetime

current_year = datetime.now().year

blog_posts = requests.get("https://api.npoint.io/689ab1121ba448547db7").json()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", all_posts=blog_posts, year=current_year)

@app.route('/about/')
def about():
    return render_template("about.html", year=current_year)

@app.route('/contact/')
def contact():
    return render_template("contact.html", year=current_year)

@app.route('/post/<int:index>')
def post(index):
    requested_post = None
    for post in blog_posts:
        if post["id"] == index:
            requested_post = post
    return render_template("post.html", post=requested_post, year=current_year)

if __name__ == "__main__":
    app.run(port=8000, debug=True)