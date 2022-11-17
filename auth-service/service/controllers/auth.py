import traceback

import jwt
from redis_om import NotFoundError

import config
from errors import SERVICE_ERROR_NONE
from errors import SERVICE_ERROR_BAD_REQUEST
from errors import SERVICE_ERROR_NOT_FOUND
from errors import SERVICE_ERROR_SERVER_ERROR

from models.quota import QUOTA_STATUS_ACTIVE
from models.quota import QUOTA_STATUS_ENDED
from models.quota import Quota
from models.token import TOKEN_STATUS_AVAILABLE
from models.token import Token

def token_validate (token_reference: str):
	error = SERVICE_ERROR_NONE

	try:
		token = Token.get (token_reference)

		if (token.status != TOKEN_STATUS_AVAILABLE):
			error = SERVICE_ERROR_BAD_REQUEST

	except NotFoundError:
		print ("Failed to get token!")
		error = SERVICE_ERROR_NOT_FOUND

	return error

def quota_update (quota_reference: str):
	error = SERVICE_ERROR_NONE

	try:
		quota = Quota.get (quota_reference)

		if (quota.status == QUOTA_STATUS_ACTIVE):
			quota.used += 1

			if (quota.used >= quota.quantity):
				quota.status = QUOTA_STATUS_ENDED

			quota.save ()

		else:
			error = SERVICE_ERROR_BAD_REQUEST

	except NotFoundError:
		print ("Failed to get quota!")
		error = SERVICE_ERROR_NOT_FOUND

	return error

def auth_check (data: dict):
	error = SERVICE_ERROR_BAD_REQUEST

	try:
		api_key: str = data["key"]

		payload = jwt.decode (api_key, config.app_data["JWT_PUBLIC_KEY"])

		if (token_validate (payload["reference"]) == SERVICE_ERROR_NONE):
			error = quota_update (payload["quota"])

	except:
		traceback.print_exc ()
		error = SERVICE_ERROR_SERVER_ERROR

	return error
