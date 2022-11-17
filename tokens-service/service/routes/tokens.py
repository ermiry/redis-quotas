from functools import wraps
import requests
import traceback

from flask import Blueprint, request, jsonify

from errors import SERVICE_ERROR_NONE
from errors import SERVICE_ERROR_UNAUTHORIZED
from errors import response_from_error

from controllers.tokens import tokens_get_all
from controllers.tokens import token_create
from controllers.tokens import token_info
from controllers.tokens import token_revoke

HTTP_STATUS_OK = 200

tokens = Blueprint ("tokens", __name__)

def token_check (token: str) -> bool:
	result = False

	try:
		response = requests.post (
			"http://auth:5000/api/auth/check", data={ "key": token }
		)

		if (response.status_code == HTTP_STATUS_OK):
			result = True

	except:
		print ("Failed to perform auth request!")

	return result

def token_required (function):
	@wraps (function)
	def decorator (*args, **kwargs):
		error = SERVICE_ERROR_UNAUTHORIZED
		token = None

		if ("Authorization" in request.headers):
			token = request.headers["Authorization"]

			if (token_check (token)):
				return function (token, *args, **kwargs)

		return jsonify (response_from_error (error)), error

	return decorator

# GET /api/tokens
@tokens.route ("/api/tokens", methods=["GET"])
def tokens_handler ():
	return jsonify (tokens_get_all ())

# GET /api/tokens/test
@tokens.route ("/api/tokens/test", methods=["GET"])
@token_required
def token_test_handler ():
	error = SERVICE_ERROR_NONE

	return jsonify (response_from_error (error)), error

# POST /api/tokens/create
@tokens.route ("/api/tokens/create", methods=["POST"])
def token_create_handler ():
	data = request.get_json ()
	error, token_value = token_create (data)
	return jsonify ({"api_key": token_value}), error

# GET /api/tokens/:token_id/info
@tokens.route ("/api/tokens/<token_id>/info", methods=["GET"])
def token_info_handler (token_id):
	error, result = token_info (token_id)

	if (error == SERVICE_ERROR_NONE):
		return jsonify (result), error

	return jsonify (response_from_error (error)), error

# GET /api/tokens/:token_id/revoke
@tokens.route ("/api/tokens/<token_id>/revoke", methods=["GET"])
def token_revoke_handler (token_id):
	error = token_revoke (token_id)

	return jsonify (response_from_error (error)), error
