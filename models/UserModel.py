from sqlalchemy import Column, Integer, String, Boolean
from models.BaseModel import BaseModel, db
from werkzeug.security import generate_password_hash, check_password_hash

class User(BaseModel):
    __tablename__ = 'users'

    email = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)  # Adjust size if needed
    is_admin = db.Column(db.Boolean, default=False)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)

    def __init__(self, email, password, first_name, last_name, is_admin=False):
        super().__init__()
        self.email = email
        self.set_password(password)
        self.first_name = first_name
        self.last_name = last_name
        self.is_admin = is_admin

    def __str__(self):
        return f"User(email={self.email}, name={self.first_name} {self.last_name})"

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
