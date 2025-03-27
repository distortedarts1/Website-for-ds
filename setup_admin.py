import os
from werkzeug.security import generate_password_hash
from models import User
from extensions import db

def setup_admin():
    admin_email = os.environ.get("ADMIN_EMAIL")
    admin_password = os.environ.get("ADMIN_PASSWORD")
    
    admin = User.query.filter_by(email=admin_email).first()
    if not admin:
        admin = User(email=admin_email, password_hash=generate_password_hash(admin_password))
        db.session.add(admin)
        db.session.commit()
