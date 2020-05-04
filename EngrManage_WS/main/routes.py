from flask import render_template,url_for,flash,redirect,request, Blueprint
from EngrManage_WS.main.forms import LoginForm,RegistrationForm
from EngrManage_WS.models import User,Role
from flask_login import login_user,current_user,logout_user,login_required
from EngrManage_WS import bcrypt,db

main_blueprint = Blueprint('main', __name__,template_folder='templates')

@main_blueprint.route("/")
@main_blueprint.route("/home")
def home():
    # if no admistrator, then go straight to the first_admistration page
    admin = User.query.join(Role,User.roles).filter_by(tag='Admin').first()
    if not admin:
        return redirect(url_for('first_administrator'))
    elif not current_user.is_authenticated:
        return redirect(url_for('login'))
    return render_template('main/home.html',title='Home')

@main_blueprint.route("/Startup", methods=['GET', 'POST'])
def first_administrator():
    form = RegistrationForm()
    admin = User.query.join(Role,User.roles).filter_by(tag='Admin').first()
    if admin:
        flash('Admistrator already exists, please ask admistrator to register new user')
        return redirect(url_for('login'))
    elif form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        admin = User(username=form.username.data, email=form.email.data, password=hashed_password)
        
        role = Role.query.filter_by(tag='Admin').first()
        # role = Role(tag='Admin')

        admin.roles.append(role)
        db.session.add(admin)
        db.session.commit()
        flash('Admistrator Created','success')
        return redirect(url_for('login'))
        
    return render_template('main/first_administrator.html', title='Startup', form=form)

@main_blueprint.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password,form.password.data):
            login_user(user,remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password','danger')
    return render_template('main/login.html', title='Login', form=form)

@main_blueprint.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))
