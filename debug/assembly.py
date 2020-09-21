from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///assembly.db'
db = SQLAlchemy(app)

assembly_sub = db.Table(
    'assembly_sub', 
    db.Column('parent_id', db.Integer, db.ForeignKey('assembly.id')),
    db.Column('children_id', db.Integer, db.ForeignKey('assembly.id'))
)

class Assembly(db.Model):
    __tablename__ = 'assembly'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20), index=True, unique=True,nullable=False)
    sub = db.relationship('Assembly', 
                            secondary=assembly_sub,
                            primaryjoin=id==assembly_sub.c.parent_id,
                            secondaryjoin=id==assembly_sub.c.children_id)
    part = db.relationship('Part',lazy=True,secondary='assembly_part')

class Part(db.Model):
    __tablename__ = 'part'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20), index=True, unique=True,nullable=False)

# Define the ProjectClient association table
class AssemlyPart(db.Model):
    __tablename__ = 'assembly_part'
    id = db.Column(db.Integer(), primary_key=True)
    assembly_id = db.Column(db.Integer(), db.ForeignKey('assembly.id', ondelete='CASCADE'))
    part_id = db.Column(db.Integer(), db.ForeignKey('part.id', ondelete='CASCADE'))