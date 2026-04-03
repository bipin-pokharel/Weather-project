from flask import Flask, render_template, request
from waitress import serve
from weather import get_current_weather


app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    return "Hello world"


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)
