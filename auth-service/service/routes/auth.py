from flask import Blueprint, request, jsonify

from errors import SERVICE_ERROR_NONE
from errors import response_from_error

from controllers.auth import auth_check

auth = Blueprint ("auth", __name__)

# GET /api/auth
@auth.route ("/api/auth", methods=["GET"])
def auth_handler ():
	error: int = SERVICE_ERROR_NONE

	return jsonify (response_from_error (error)), error

# GET /api/auth/check
@auth.route ("/api/auth/check", methods=["GET"])
def auth_check_handler ():
	data = request.get_json ()
	error = auth_check (data)
	return jsonify (response_from_error (error)), error
