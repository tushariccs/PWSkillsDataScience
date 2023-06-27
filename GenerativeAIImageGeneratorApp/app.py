from flask import Flask, render_template
from config import key

app = Flask(__name__)

@app.route('/')
def index():
    return render_template()