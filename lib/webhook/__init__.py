from flask import Flask, request
import json
import ConfigParser
import os
import re

def create_app():
    app = Flask(__name__)
    return app

app = create_app()

@app.route('/')
def index():
    return "Nothing here"

def main():
    app.run(host='127.0.0.1')

if __name__ == '__main__':
    main()
