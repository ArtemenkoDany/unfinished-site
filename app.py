from flask import Flask, render_template # These are all we need for our purposes

app = Flask(__name__)

@app.route("/")
def index():
    return render_template(""
                           "index.html", **{"greeting": "Hello from Flask!"})
