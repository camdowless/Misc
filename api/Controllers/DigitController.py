from requests.auth import HTTPBasicAuth
import requests
from flask import Blueprint, request, jsonify, current_app



# sys.path.append("..")
# from Models import Countries
Digit_bp = Blueprint('Digit', __name__)


@Digit_bp.get("/Digit")
def classify():
    return "Hello"
