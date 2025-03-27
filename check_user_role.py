import os
from app import create_app
from models import User

def check_admin_users():
    app = create_app()
    with app.app_context():
        target_email = os.environ.get("ADMIN_EMAIL")
        super_admin = User.query.filter_by(email=target_email).first()
        if super_admin:
            print(f"Super Admin: {super_admin.username}")
