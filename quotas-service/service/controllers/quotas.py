import json
import requests
import traceback

from redis_om import NotFoundError

from errors import SERVICE_ERROR_NONE
from errors import SERVICE_ERROR_NOT_FOUND
from errors import SERVICE_ERROR_SERVER_ERROR

from models.quota import QUOTA_STATUS_ACTIVE
from models.quota import Quota

def quotas_get_all ():
	quotas = Quota.find ().all ()
	# print (quotas)

	return quotas

def quota_create (data: dict):
	error = SERVICE_ERROR_NONE

	try:
		quota = Quota (
			name=data["name"],
			value=data["value"],
			status=QUOTA_STATUS_ACTIVE,
			quantity=data["quantity"],
			used=0,
			last_time=None
		)

		quota.save ()
		quota_id = quota.pk
		# print (quota_id)

	except:
		traceback.print_exc ()
		error = SERVICE_ERROR_SERVER_ERROR

	return error, quota_id

def quota_info (quota_id):
	error = SERVICE_ERROR_NONE
	result = None

	try:
		result = Quota.get (quota_id)

	except NotFoundError:
		print ("Failed to get quota!")
		error = SERVICE_ERROR_NOT_FOUND
	except:
		traceback.print_exc ()
		error = SERVICE_ERROR_SERVER_ERROR

	return error, result

def quota_remove (quota_pk: str):
	error = SERVICE_ERROR_NONE

	try:
		Quota.delete (quota_pk)

	except NotFoundError:
		print ("Failed to get quota!")
		error = SERVICE_ERROR_NOT_FOUND
	except:
		traceback.print_exc ()
		error = SERVICE_ERROR_SERVER_ERROR

	return error
