# -----------------------------------------------------------------------------------
# File   :   app.py
# Author :   Mélodie Ohan
# Version:   09-02-2022 - original (dedicated to BI1)
# Remarks:   Entry point of the API on Flask Framework
# -----------------------------------------------------------------------------------

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, Docker!'
