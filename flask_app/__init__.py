from flask import Flask
import os

app = Flask(__name__)


app.secret_key = os.environ.get("FLASK_SECRET_KEY")
NSA_API_KEY=os.environ.get("NSA_API_KEY")
ROOT_KEY = os.environ.get('ROOT_KEY')