from flask import Flask

from routes.tokens import tokens

PORT = 5002

app = Flask (__name__)

app.register_blueprint (tokens)

if __name__ == "__main__":
	app.run (debug=True, host="0.0.0.0", port=PORT)
