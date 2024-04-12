#!/usr/bin/env python3

from flask import Flask, request,render_template

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('home.html'),200

@app.route("/echo_user_input", methods=["POST"])
def echo_input():
    input_text = request.form.get("user_input", "")

    return render_template('response.html',input_text=input_text),200
