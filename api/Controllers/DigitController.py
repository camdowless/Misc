from requests.auth import HTTPBasicAuth
import requests
from flask import Blueprint, request, jsonify, current_app


Digit_bp = Blueprint('Digit', __name__)


@Digit_bp.get("/Digit")
def classify():
    return "Hello"
