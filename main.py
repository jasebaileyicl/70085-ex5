from flask import Flask
from flask import request


app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>NEW NEW Token Hello, World! Again</p>"


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
