import json
import datetime
import requests
import time
import traceback
import uuid

import jwt
from redis_om import NotFoundError

import config
from errors import SERVICE_ERROR_NONE
from errors import SERVICE_ERROR_NOT_FOUND
from errors import SERVICE_ERROR_SERVER_ERROR

from models.token import TOKEN_STATUS_AVAILABLE
from models.token import TOKEN_STATUS_REVOKED
from models.token import Token

def tokens_get_all ():
	tokens = Token.find ().all ()
	# print (tokens)

	return tokens

def token_generate (token_reference: str, quota_id: str):
	payload = {
		"iat": datetime.datetime.now (),
		"quota": quota_id,
		"reference": token_reference
	}

	return jwt.encode (
		payload, config.app_data["JWT_SECRET_KEY"], config.app_data["JWT_ALGORITHM"]
	)

def token_create (data: dict):
	error = SERVICE_ERROR_NONE
	result = None

	try:
		quota: str = data["quota"]

		token_reference = str (uuid.uuid4 ())

		token_value = token_generate (token_reference, quota)

		token = Token (
			reference=token_reference,
			name=data["name"],
			quota=quota,
			value=token_value,
			status=TOKEN_STATUS_AVAILABLE,
			created=time.time ()
		)

		token.save ()
		token_id = token.pk
		# print (token_id)

		result = token_value

	except:
		traceback.print_exc ()
		error = SERVICE_ERROR_SERVER_ERROR

	return error, result

def token_info (token_id):
	error = SERVICE_ERROR_NONE
	result = None

	try:
		result = Token.get (token_id)

	except NotFoundError:
		print ("Failed to get token!")
		error = SERVICE_ERROR_NOT_FOUND
	except:
		traceback.print_exc ()
		error = SERVICE_ERROR_SERVER_ERROR

	return error, result

def token_revoke (token_id):
	error = SERVICE_ERROR_NONE

	try:
		token = Token.get (token_id)

		token.status = TOKEN_STATUS_REVOKED
		token.save ()

	except NotFoundError:
		print ("Failed to get token!")
		error = SERVICE_ERROR_NOT_FOUND
	except:
		traceback.print_exc ()
		error = SERVICE_ERROR_SERVER_ERROR

	return error
