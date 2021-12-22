from flask import Flask
from flask import url_for
from markupsafe import escape

app = Flask(__name__)


@app.route("/<name>")
def hello(name):
    return f"<p>hello {escape(name)}</p>"
