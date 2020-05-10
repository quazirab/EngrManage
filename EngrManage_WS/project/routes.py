from flask import render_template,url_for,flash,redirect,request,Blueprint
from EngrManage_WS.project.forms import ProjectFrom
from EngrManage_WS.models import Project,User
from flask_login import login_user,current_user,logout_user,login_required
from EngrManage_WS.special_functions import login_role_required
from EngrManage_WS import db
#====================Logger========================
import logging
logger = logging.getLogger(__name__)
#====================Logger========================

project_blueprint = Blueprint('project', __name__,template_folder='templates')

@project_blueprint.route("/project",methods=['GET','POST'])
@login_role_required(roles=['Admin','User'])
def project():
    
    form = ProjectFrom()
    if form.validate_on_submit():
        new_project = Project(created_by=current_user.id, name=form.name.data, description=form.description.data)
        db.session.add(new_project)
        db.session.commit()
        return redirect(url_for('project.project'))
    projects = Project.query.all()
    return render_template('project/home.html',projects = projects, form=form, title='Project')

@project_blueprint.route("/project/create_project",methods=['GET','POST'])
@login_role_required(roles=['Admin','User'])
def project_creator():
    form = ProjectFrom()
    if form.validate_on_submit():
        new_project = Project(created_by=current_user.id, name=form.name.data, description=form.description.data)
        db.session.add(new_project)
        db.session.commit()
        return redirect(url_for('project.project'))
    return render_template('project/projectcreator.html', form=form, title='Create Project')

@project_blueprint.route("/project/<int:project_id>/details", methods=['GET', 'POST'])
@login_role_required(roles=['Admin'])
def project_details(project_id):
    project = Project.query.filter_by(id=project_id).first()
    creator = User.query.filter_by(id=project.created_by).first()
    return render_template('project/projectdetails.html',project=project, creator=creator, title=project.name)