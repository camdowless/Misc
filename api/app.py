from importlib import resources
from flask import Flask, request, jsonify
from authlib.integrations.flask_client import OAuth
from flask_cors import CORS, cross_origin
import json
from Controllers.DigitController import Digit_bp
app = Flask(__name__)
app.config.from_file("appsettings.json", load=json.load)
app.register_blueprint(Digit_bp, url_prefix='/')

CORS(app, resources={
    '/Digit': {"origins":  app.config['CORS_ORIGIN']},
})



if __name__ == "__main__":
    app.run(debug=True)