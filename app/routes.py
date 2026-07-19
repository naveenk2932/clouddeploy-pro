from flask import Blueprint
import platform
import socket
import os

api = Blueprint("api", __name__)


@api.route("/")
def home():
    return {
        "application": "CloudDeploy Pro",
        "status": "running"
    }


@api.route("/health")
def health():
    return {
        "status": "healthy"
    }


@api.route("/version")
def version():
    return {
        "version": "1.0.0"
    }


@api.route("/info")
def info():
    return {
        "hostname": socket.gethostname(),
        "platform": platform.system(),
        "python": platform.python_version(),
        "environment": os.getenv("APP_ENV", "development")
    }