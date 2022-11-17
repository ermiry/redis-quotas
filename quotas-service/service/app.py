from flask import Flask

from routes.quotas import quotas

PORT = 5000

app = Flask (__name__)

app.register_blueprint (quotas)

if __name__ == "__main__":
	app.run (debug=True, host="0.0.0.0", port=PORT)
