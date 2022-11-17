SERVICE_ERROR_NONE = 200
SERVICE_ERROR_BAD_REQUEST = 400
SERVICE_ERROR_MISSING_VALUES = 400
SERVICE_ERROR_UNAUTHORIZED = 401
SERVICE_ERROR_NOT_FOUND = 404
SERVICE_ERROR_SERVER_ERROR = 500

def response_from_error (error: int):
	result = None
	if (error == SERVICE_ERROR_NONE):
		result = {"oki": "doki"}

	elif (error == SERVICE_ERROR_NOT_FOUND):
		result = {"error": "not found!"}

	elif (error == SERVICE_ERROR_SERVER_ERROR):
		result = {"error": "failed!"}

	return result
