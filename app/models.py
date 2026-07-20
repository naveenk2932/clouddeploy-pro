from datetime import datetime
from app.extensions import db


class Deployment(db.Model):
    __tablename__ = "deployments"

    id = db.Column(db.Integer, primary_key=True)

    application = db.Column(
        db.String(100),
        nullable=False
    )

    version = db.Column(
        db.String(50),
        nullable=False
    )

    environment = db.Column(
        db.String(50),
        nullable=False
    )

    status = db.Column(
        db.String(50),
        nullable=False
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    def to_dict(self):
        return {
            "id": self.id,
            "application": self.application,
            "version": self.version,
            "environment": self.environment,
            "status": self.status,
            "created_at": self.created_at.isoformat()
        }