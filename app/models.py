from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


class v15_11(db.Model):
    project_name = db.Column(db.String(30), nullable=False)

    def __str__(self):
        return f"{self.project_name}"