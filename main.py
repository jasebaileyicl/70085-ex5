import requests
from flask import Flask, render_template
from flask import request

app = Flask(__name__)

# flask run -h '0.0.0.0' -p 5000 main.py

@app.route("/")
def hello_world():
    return "<p>NEW NEW Token Hello, World! Again</p>"


@app.route("/username")
def get_github_username():
    return render_template("username.html")


@app.route("/submit-username", methods=["POST"])
def display_username():
    # https://api.github.com/users/espeecat
    # https://api.github.com/users/espeecat/repos
    # https://api.github.com/repos/espeecat/big-data-brighton-april-2013/commits

    username = request.form.get("username")

    user_details_resp = requests.get(f"https://api.github.com/users/{username}")
    status_code = user_details_resp.status_code
    if status_code == 404:
        return "user not found"

    if status_code != 200:
        return "error"

    data = user_details_resp.json()

    name = data["name"]
    company = data["company"]
    url = data["url"]
    avatar = data["avatar_url"]

    # repos

    repos_resp = requests.get(f"https://api.github.com/users/{username}/repos")
    if repos_resp.status_code != 200:
        repos=None

    repos=repos_resp.json()

    return render_template("view.html", username=username, name=name,company=company,url=url,avatar=avatar, repos=repos )


@app.route("/query")
def get_query():
    query = request.args.get("q")
    return process_query(query)


def process_query(query: str):
    if query == "dinosaurs":
        return "Dinosaurs ruled the Earth 200 million years ago"

    if query == "asteroids":
        return "Unknown"

    return "Query not known"
