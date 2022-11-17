from flask import Blueprint, request, jsonify

from errors import SERVICE_ERROR_NONE
from errors import response_from_error

from controllers.quotas import quotas_get_all
from controllers.quotas import quota_create
from controllers.quotas import quota_info
from controllers.quotas import quota_remove

quotas = Blueprint ("quotas", __name__)

# GET /api/quotas
@quotas.route ("/api/quotas", methods=["GET"])
def quotas_handler ():
	return jsonify (quotas_get_all ())

# POST /api/quotas/create
@quotas.route ("/api/quotas/create", methods=["POST"])
def quota_create_handler ():
	data = request.get_json ()
	error, quota_id = quota_create (data)
	return jsonify ({"oki": "doki"})

# GET /api/quotas/:quota_id/info
@quotas.route ("/api/quotas/<quota_id>/info", methods=["GET"])
def quota_info_handler (quota_id):
	error, result = quota_info (quota_id)

	if (error == SERVICE_ERROR_NONE):
		return jsonify (result), error

	return jsonify (response_from_error (error)), error

# DELETE /api/quotas/:quota_id/remove
@quotas.route ("/api/quotas/<quota_id>/remove", methods=["DELETE"])
def quota_remove_handler (quota_id):
	error = quota_remove (quota_id)

	return jsonify (response_from_error (error)), error
