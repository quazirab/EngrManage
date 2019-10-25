from flask import render_template,url_for,flash,redirect,request,Blueprint
from flask_bcrypt import Bcrypt
from EngrManage import app
from EngrManage.forms import ProjectFrom
from EngrManage.models import db, Project,User
from flask_login import login_user,current_user,logout_user,login_required
from EngrManage.special_functions import login_role_required
from EngrManage.routes import bcrypt
#====================Logger========================
import logging
logger = logging.getLogger(__name__)
#====================Logger========================

@app.route("/projects")
@login_role_required(roles=['Admin','User'])
def projects():
    projects = Project.query.all()
    return render_template('project/home.html',projects = projects, title='Projects')

@app.route("/projects/create_project",methods=['GET','POST'])
@login_role_required(roles=['Admin','User'])
def project_creator():
    form = ProjectFrom()
    if form.validate_on_submit():
        new_project = Project(created_by=current_user.id, name=form.name.data, description=form.description.data)
        db.session.add(new_project)
        db.session.commit()
        return redirect(url_for('projects'))
    return render_template('project/projectcreator.html', form=form, title='Create Projects')

@app.route("/project/<int:project_id>/details", methods=['GET', 'POST'])
@login_role_required(roles=['Admin'])
def project_details(project_id):
    project = Project.query.filter_by(id=project_id).first()
    creator = User.query.filter_by(id=project.created_by).first()
    return render_template('project/projectdetails.html',project=project, creator=creator, title=project.name)