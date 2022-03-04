from flask import Flask, render_template
import random
from datetime import datetime
import requests

app = Flask(__name__)


@app.route("/")
def home():
    random_number = random.randint(1, 10)
    current_year = datetime.now().year
    return render_template("index.html", num=random_number, year=current_year)


@app.route("/guess/<name>")
def guess_name(name):
    user_name = name.title()
    gender_url = "https://api.genderize.io"
    gender_params = {
        "name": f"{name}"
    }
    gender_response = requests.get(url=gender_url, params=gender_params)
    user_gender = gender_response.json()["gender"]
    age_url = "https://api.agify.io"
    age_params = {
        "name": f"{name}"
    }
    age_response = requests.get(url=age_url, params=age_params)
    user_age = age_response.json()["age"]
    return render_template("guess_name.html", user_name=user_name, user_gender=user_gender, user_age=user_age)


@app.route("/blog/<num>")
def blog(num):
    print(num)
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(url=blog_url)
    all_blogs = response.json()
    return render_template("blog.html", all_blogs=all_blogs)


if __name__ == "__main__":
    app.run(debug=True)
