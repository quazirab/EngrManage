from flask import render_template,url_for,flash,redirect,request,Blueprint
from EngrManage_WS import bcrypt,db
from EngrManage_WS.adminstration.forms import AddUserForm,AddUserGroup,EditUser
from EngrManage_WS.models import User,Role
from flask_login import login_user,current_user,logout_user,login_required
from EngrManage_WS.special_functions import login_role_required


adminstration_blueprint = Blueprint('adminstration', __name__,template_folder='templates')

@adminstration_blueprint.route("/adminstration")
@login_role_required(roles=['Admin'])
def adminstration():
    return render_template('administration/home.html', title='Adminstration')

@adminstration_blueprint.route("/adminstration/add_user",methods=['GET', 'POST'])
@login_role_required(roles=['Admin'])
def adminstration_adduser():
    form = AddUserForm()
    roles = Role.query.all()
    if form.validate_on_submit():
        # Get all the roles first 
        user_role = [Role.query.filter_by(tag=tag).first() for tag in request.form.getlist('user_role')]
        
        # Add the User
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        new_user = User(username=form.username.data, 
                    email=form.email.data, 
                    password=hashed_password, 
                    roles=user_role)
        db.session.add(new_user)
        db.session.commit()
        flash('User Added','success')

        # Redirect to the admistration page
        return redirect(url_for('adminstration'))

    return render_template('administration/adduser.html',roles=roles,form=form, title='Add User')


@adminstration_blueprint.route("/add_user_group",methods=['GET', 'POST'])
@login_role_required(roles=['Admin'])
def adminstration_addusergroup():
    roles = Role.query.all()
    form=AddUserGroup()
    if form.validate_on_submit():
        role = Role(tag=form.role.data)
        db.session.add(role)
        db.session.commit()
        flash('Role Created','success')
        return redirect(url_for('adminstration_addusergroup'))
    return render_template('administration/addusergroup.html',roles=roles, form=form, title='User Group')

@adminstration_blueprint.route("/user_list")
@login_role_required(roles=['Admin'])
def adminstration_userlist():
    users = User.query.all()
    form=AddUserForm()
    return render_template('administration/userlist.html',users=users, form=form, title='User List')

@adminstration_blueprint.route("/user_list/<int:user_id>/details", methods=['GET', 'POST'])
@login_role_required(roles=['Admin'])
def user_details(user_id):
    user = User.query.filter_by(id=user_id).first()
    roles = Role.query.all()
    user_roles = user.roles

    form = EditUser(user)

    if request.method =='GET':
        form.username.data = user.username
        form.email.data = user.email

    elif request.method =='POST' and form.validate_on_submit():
        user.username = form.username.data
        user.email = form.email.data
        new_user_role = [Role.query.filter_by(tag=tag).first() for tag in request.form.getlist('user_role')]
        user.roles = new_user_role
        db.session.commit()
        return redirect(url_for('adminstration_userlist'))

    return render_template('administration/userdetails.html',
                            form=form, roles=roles, user_roles=user_roles, 
                            title='User List')
 

@login_role_required(roles=['Admin'])
def delete_user(username):
    user = User.query.filter_by(username=username).first()
    user.delete()
    db.session.commit()
    return redirect(url_for('adminstration_userlist'))