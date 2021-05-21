from flask import Flask
from flask_minify import minify

app = Flask(__name__)

minify(app=app, html=True, js=True, cssless=True)

if __name__ == "__main__":
    app.run()
