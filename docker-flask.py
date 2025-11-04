from flask import Flask
import numpy

docker_app = Flask(__name__)

golfer = "<h1>Tommy Fleetwood</h1>"

@docker_app.route("/", methods=["GET", "POST"])
def hello_flask():
    return "success"

@docker_app.route("/matt", methods = ["GET", "POST"])
def favorite_golfer():
    return golfer

docker_app.run(debug=True, host="0.0.0.0")