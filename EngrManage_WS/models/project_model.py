from datetime import datetime
#====================Logger========================
import logging
logger = logging.getLogger(__name__)
#====================Logger========================
from EngrManage_WS import db

# Project Model - It is the main model, the project will be created with client(s) informantion
# Once Project is Created, it will append the client(s) and the client_handler will keep the infornmation
# 
class Project(db.Model):
    __tablename__ = 'projects'
    id = db.Column(db.Integer,primary_key=True)
    active = db.Column('is_active', db.Boolean(), nullable=False, server_default='1')
    created_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    # Define required information
    created_by = db.Column(db.Integer(), db.ForeignKey('users.id'), nullable=False)
    name = db.Column(db.String(20), index=True, unique=True,nullable=False)
    description = db.Column(db.String(120),nullable=False)

    # Client Information - Many Projects share Many Clients
    clients = db.relationship('Client',lazy=True,secondary='project_clients')

    # Invoice Information - One project has Many Invoices 
    invoices = db.relationship('Invoice',backref='project',lazy=True)
 
    # Vendor Information - Many Projects share Many Vendors
    vendors = db.relationship('Vendor',lazy=True,secondary='project_vendors')

    # Purchase Order (PO) Information - One project has Many POs 
    pos = db.relationship('PO',backref='project',lazy=True)

    # Bill of Materials(BOM) Information - One project has Many BOMs 
    boms = db.relationship('BOM',backref='project',lazy=True)

    def __repr__(self):
        return f"Project : Name:{self.name}, Created By (user_id):{self.created_by}, Created Date:{self.created_date}, Clients:{self.clients}, Invoices:{self.invoices}, POs:{self.pos}, BOMs:{self.boms}"

# Many Clients share Many Vendors
class Client(db.Model):
    __tablename__ = 'clients'
    id = db.Column(db.Integer,primary_key=True)
    active = db.Column('is_active', db.Boolean(), nullable=False, server_default='1')
    created_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    # required Information
    created_by = db.Column(db.Integer(), db.ForeignKey('users.id'), nullable=False)
    name = db.Column(db.String(20), index=True, unique=True, nullable=False)
    description = db.Column(db.String(120))

    def __repr__(self):
        return f"Client : Name:{self.name}, Created By (user_id):{self.created_by}, Created Date:{self.created_date}"

# One Invoice can have one client
class Invoice(db.Model):
    __tablename__='invoices'
    id = db.Column(db.Integer,primary_key=True)
    active = db.Column('is_active', db.Boolean(), nullable=False, server_default='1')
    created_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    #required Information
    created_by = db.Column(db.Integer(), db.ForeignKey('users.id'), nullable=False)
    client_id = db.Column(db.Integer(), db.ForeignKey('clients.id'), nullable=False)
    project_id = db.Column(db.Integer(), db.ForeignKey('projects.id'), nullable=False)
    name = db.Column(db.String(20), index=True, unique=True,nullable=False)
    description = db.Column(db.String(120))

    # Optional
    Tax =  db.Column(db.Float())

    def __repr__(self):
        return f"Invoice : Name:{self.name}, Created By (user_id):{self.created_by}, Created Date:{self.created_date}"

# Many Projects share Many Vendors 
class Vendor(db.Model):
    __tablename__ = 'vendors'
    id = db.Column(db.Integer,primary_key=True)
    active = db.Column('is_active', db.Boolean(), nullable=False, server_default='1')
    created_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    # required Information
    created_by = db.Column(db.Integer(), db.ForeignKey('users.id'), nullable=False)
    name = db.Column(db.String(20), index=True, unique=True, nullable=False)
    description = db.Column(db.String(120))

    def __repr__(self):
        return f"Vendor : Name:{self.name}, Created By (user_id):{self.created_by}, Created Date:{self.created_date}"

class PO(db.Model):
    __tablename__='pos'
    id = db.Column(db.Integer,primary_key=True)
    active = db.Column('is_active', db.Boolean(), nullable=False, server_default='1')

    # Required Information
    created_by = db.Column(db.Integer(), db.ForeignKey('users.id'), nullable=False)
    project_id = db.Column(db.Integer(), db.ForeignKey('projects.id'), nullable=False)
    name = db.Column(db.String(20), index=True, unique=True,nullable=False)
    description = db.Column(db.String(120))


    def __repr__(self):
        return f"Invoice : Name:{self.name}, Created By (user_id):{self.created_by}, Created Date:{self.created_date}"

class BOM(db.Model):
    __tablename__='boms'
    id = db.Column(db.Integer,primary_key=True)
    active = db.Column('is_active', db.Boolean(), nullable=False, server_default='1')

    # Required Information
    created_by = db.Column(db.Integer(), db.ForeignKey('users.id'), nullable=False)
    project_id = db.Column(db.Integer(), db.ForeignKey('projects.id'), nullable=False)
    name = db.Column(db.String(20), index=True, unique=True,nullable=False)
    description = db.Column(db.String(120))
    
    def __repr__(self):
        return f"Invoice : Name:{self.name}, Created By (user_id):{self.created_by}, Created Date:{self.created_date}"

# Define the ProjectClient association table
class ProjectClients(db.Model):
    __tablename__ = 'project_clients'
    id = db.Column(db.Integer(), primary_key=True)
    project_id = db.Column(db.Integer(), db.ForeignKey('projects.id', ondelete='CASCADE'))
    client_id = db.Column(db.Integer(), db.ForeignKey('clients.id', ondelete='CASCADE'))

    def __repr__(self):
        return f"Project handler : Project ID:{self.project_id}, Client ID:{self.client_id}"

# Define the ProjectVendors association table
class ProjectVendors(db.Model):
    __tablename__ = 'project_vendors'
    id = db.Column(db.Integer(), primary_key=True)
    project_id = db.Column(db.Integer(), db.ForeignKey('projects.id', ondelete='CASCADE'))
    vendor_id = db.Column(db.Integer(), db.ForeignKey('vendors.id', ondelete='CASCADE'))

    def __repr__(self):
        return f"Project handler : Project ID:{self.project_id}, Client ID:{self.vendor_id}"