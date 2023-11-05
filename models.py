from flask_login import UserMixin 
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin):
    def __init__(self, id, name, email, password):
        self.id = id
        self.name = name
        self.email = email
        self.password = generate_password_hash(password)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):  #method for representing the objects in a class as a string, returns the printable representation of the specified object as a string.
        return '<User {}>'.format(self.email)

users = []

def get_user(email):
    for user in users:
        if user.email == email:
            return user
    return None