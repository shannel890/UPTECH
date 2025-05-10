from app import db,login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    
    return User.query.get(int(user_id))

class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(50), nullable=False)

    @property
    def is_active(self):
        
        return True

    def __repr__(self):
        return f"{self.first_name} {self.last_name}"