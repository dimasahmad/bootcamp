import os, sys
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

# allow importing modules from cwd
sys.path.append(os.getcwd())

# import hackerrank solutions
from hackerrank.quiz.is_prime import is_prime
from hackerrank.challenges.electronics_shop.get_money_spent import get_money_spent
from hackerrank.challenges.picking_numbers.picking_numbers import picking_numbers
from hackerrank.challenges.library_fine.library_fine import library_fine

# init flask app
app = Flask(__name__)


# Error handling with JSON response
@app.errorhandler(HTTPException)
def http_exceptions(e: HTTPException):
    return jsonify(error={"code": e.code, "message": e.description}), e.code


# Register protected routes
from protected import protected

app.register_blueprint(protected, url_prefix="/protected")


@app.route("/isPrime")
def route_is_prime():
    n = request.args.get('q', type=int)

    result = is_prime(n)
    return jsonify(result=result)


@app.route("/electronicShop", methods=["POST"])
def route_electronic_shop():
    result = get_money_spent(**request.json)
    return jsonify(result=result)


@app.route("/pickingNumber", methods=["POST"])
def route_picking_number():
    result = picking_numbers(**request.json)
    return jsonify(result=result)


@app.route("/libraryFine")
def route_library_fine():
    return_date = map(int, request.args.get("return").split("-"))
    due_date = map(int, request.args.get("due").split("-"))

    result = library_fine(*return_date, *due_date)
    return jsonify(result=result)
