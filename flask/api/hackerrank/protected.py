from flask import request, jsonify, Blueprint
import http
from werkzeug.exceptions import Unauthorized, BadRequest

# import hackerrank solutions
from hackerrank.challenges.electronics_shop.get_money_spent import get_money_spent
from hackerrank.challenges.picking_numbers.picking_numbers import picking_numbers
from hackerrank.challenges.library_fine.library_fine import library_fine
from hackerrank.challenges.repeated_string.repeated_string import repeated_string
from hackerrank.challenges.strong_password.minimum_number import minimum_number
from hackerrank.challenges.mars_exploration.mars_exploration import mars_exploration

# user authentication and authorization
from user import User

user = User()

# create flask blueprint
protected = Blueprint('protected', __name__)


@protected.route("/electronicShop", methods=["POST"])
def protected_route_electronic_shop():
    if not user.is_authenticated():
        raise Unauthorized()

    try:
        if not request.json.keys() >= {"keyboards", "drives", "budget"}:
            raise AttributeError()

        result = get_money_spent(**request.json)
    except AttributeError:
        raise BadRequest("Missing required request body json elements.")

    if result == -1:
        raise BadRequest("Insufficient budget")

    return jsonify(result=result)


@protected.route("/pickingNumber", methods=["POST"])
def protected_route_picking_number():
    if not user.is_authenticated() or not user.has_role("admin"):
        raise Unauthorized()

    try:
        if not request.json.keys() >= {"numbers"}:
            raise AttributeError()

        result = picking_numbers(**request.json)
    except AttributeError:
        raise BadRequest("Missing required request body json elements.")

    return jsonify(result=result)


@protected.route("/libraryFine")
def protected_route_library_fine():
    if not user.is_authenticated() or not user.has_role("admin"):
        raise Unauthorized()

    if not request.args >= {"return", "due"}:
        raise BadRequest("Missing required request query parameters.")

    return_date = map(int, request.args.get("return").split("-"))
    due_date = map(int, request.args.get("due").split("-"))

    if len(return_date) != 3 or len(due_date) != 3:
        raise BadRequest(
            "Incorrect request parameter format. Expected format: dd-mm-yyyy.")

    result = library_fine(*return_date, *due_date)

    if result == 0:
        return '', http.HTTPStatus.NO_CONTENT

    return jsonify(result=result)


@protected.route("/repeatedString")
def protected_route_repeated_string():
    if not user.is_authenticated():
        raise Unauthorized()

    if not request.args >= {"s", "n"}:
        raise BadRequest("Missing required request query parameters.")

    result = repeated_string(request.args.get("s"), request.args.get("n"))

    return jsonify(result=result)


@protected.route("/strongPassword")
def protected_route_strong_password():
    if not user.is_authenticated():
        raise Unauthorized()

    try:
        if not request.json.keys() >= {"password"}:
            raise AttributeError()

        result = minimum_number(**request.json)
    except AttributeError:
        raise BadRequest("Missing required request body json elements.")

    return jsonify(result=result)


@protected.route("/marsExploration")
def protected_route_mars_exploration():
    if not user.is_authenticated():
        raise Unauthorized()

    try:
        if not request.json.keys() >= {"message"}:
            raise AttributeError()

        result = mars_exploration(**request.json)
    except AttributeError:
        raise BadRequest("Missing required request body json elements.")

    return jsonify(result=result)