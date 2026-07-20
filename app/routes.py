from flask import Blueprint, current_app, request
import platform
import socket

from app.extensions import db
from app.models import Deployment

api = Blueprint("api", __name__)


@api.route("/")
def home():
    return {
        "message": "Welcome to CloudDeploy Pro 🚀"
    }


@api.route("/health")
def health():
    return {
        "status": "healthy"
    }


@api.route("/version")
def version():
    return {
        "application": current_app.config["APP_NAME"],
        "version": current_app.config["APP_VERSION"],
        "environment": current_app.config["APP_ENV"]
    }


@api.route("/info")
def info():
    return {
        "hostname": socket.gethostname(),
        "platform": platform.system(),
        "python_version": platform.python_version()
    }


@api.route("/deployments", methods=["POST"])
def create_deployment():
    data = request.get_json()

    if not data:
        return {"error": "Request body must be JSON"}, 400

    required_fields = [
        "application",
        "version",
        "environment",
        "status"
    ]

    for field in required_fields:
        if field not in data:
            return {
                "error": f"Missing required field: {field}"
            }, 400

    deployment = Deployment(
        application=data["application"],
        version=data["version"],
        environment=data["environment"],
        status=data["status"]
    )

    db.session.add(deployment)
    db.session.commit()

    return deployment.to_dict(), 201


@api.route("/deployments", methods=["GET"])
def get_deployments():

    status = request.args.get("status")
    environment = request.args.get("environment")

    query = Deployment.query

    if status:
        query = query.filter(Deployment.status == status)

    if environment:
        query = query.filter(Deployment.environment == environment)

    deployments = query.all()

    return [deployment.to_dict() for deployment in deployments]

@api.route("/deployments/<int:deployment_id>", methods=["GET"])
def get_deployment(deployment_id):
    deployment = Deployment.query.get_or_404(deployment_id)

@api.route("/deployments/<int:deployment_id>", methods=["PUT"])
def update_deployment(deployment_id):
    deployment = Deployment.query.get_or_404(deployment_id)

    data = request.get_json()

    if not data:
        return {"error": "Request body must be JSON"}, 400

    if "application" in data:
        deployment.application = data["application"]

    if "version" in data:
        deployment.version = data["version"]

    if "environment" in data:
        deployment.environment = data["environment"]

    if "status" in data:
        deployment.status = data["status"]

    db.session.commit()

@api.route("/deployments/<int:deployment_id>", methods=["DELETE"])
def delete_deployment(deployment_id):
    deployment = Deployment.query.get_or_404(deployment_id)

    db.session.delete(deployment)
    db.session.commit()

    return {
        "message": f"Deployment {deployment_id} deleted successfully."
    }, 200

    return deployment.to_dict()