from flask import render_template,request,flash,Blueprint
from EngrManage_WS.account.forms import UpdateAccountForm
from flask_login import login_required, current_user
from EngrManage_WS import db


account_blueprint = Blueprint('account', __name__,template_folder='templates')

@account_blueprint.route("/account",methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()

    if request.method =='GET':
        form.username.data = current_user.username
        form.email.data = current_user.email

    elif request.method =='POST' and form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Account Updated','success')

    return render_template('account/account.html', title='Account',form=form)
