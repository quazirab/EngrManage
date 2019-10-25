from flask_login import UserMixin
from datetime import datetime
#====================Logger========================
import logging
logger = logging.getLogger(__name__)
#====================Logger========================
from EngrManage.models import db

class User(db.Model,UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    active = db.Column('is_active', db.Boolean(), nullable=False, server_default='1')
    created_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    # Define required information
    username = db.Column(db.String(20), index=True, unique=True,nullable=False)
    email = db.Column(db.String(120),unique=True,nullable=False)
    password = db.Column(db.String(60),nullable=False)

    # Define optional information
    first_name = db.Column(db.String(120))
    last_name = db.Column(db.String(120))
    phone_number = db.Column(db.String(20))

    # Define the relationship to Role via UserRoles
    roles = db.relationship('Role', lazy=True, secondary='user_roles')

    # # Define the relationship to Projects
    # projects_created = db.relationship('Projects',lazy=True)

    # # Define the relationship to Client
    # clients_added = db.relationship('Client',lazy=True)

    def __repr__(self):
        return f"User: {self.username},{self.email},{self.roles}"
        
# Define the Role data-model
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer(), primary_key=True)
    tag = db.Column(db.String(50), unique=True, nullable=False)
    created_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Role Tag: {self.tag}"

# Define the UserRoles association table
class UserRoles(db.Model):
    __tablename__ = 'user_roles'
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id', ondelete='CASCADE'))
    role_id = db.Column(db.Integer(), db.ForeignKey('roles.id', ondelete='CASCADE'))
    
    def __repr__(self):
        return f"User: {self.user_id},{self.role_id}"

