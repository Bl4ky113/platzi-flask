
from flask import Flask, request, make_response, redirect, render_template
import os

targets = [f"Your Mama - {i + 1}" for i in range(10)]

app = Flask(__name__)

@app.route("/")
def index ():
    user_ip = request.remote_addr
    
    response = make_response(redirect("/hello"))
    response.set_cookie("user_ip", user_ip)

    return response

@app.route("/hello")
def hello ():
    user_ip = request.cookies.get("user_ip")
    list_images = [f"images/{image}" for image in os.listdir("./static/images/") if image.endswith(".jpg")]
    context = {
            "user_ip": user_ip,
            "targets": targets,
            "images": list_images
            }

    
    return render_template("hello.html", **context)

@app.route("/error_test")
def error_test ():
    raise(Exception("500"))

@app.errorhandler(404)
def unkown_url (error):
    return render_template("error.html", error=error, num_error=404)

@app.errorhandler(500)
def server_error (error):
    return render_template("error.html", error=error, num_error=500)
