from flask import Flask

from routes.auth import auth

PORT = 5000

app = Flask (__name__)

app.register_blueprint (auth)

if __name__ == "__main__":
	app.run (debug=True, host="0.0.0.0", port=PORT)
