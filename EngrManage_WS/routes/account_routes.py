from flask import render_template,request,flash
from EngrManage_WS import app
from EngrManage_WS.forms import UpdateAccountForm
from flask_login import login_required, current_user
from EngrManage_WS.models import db

@app.route("/account",methods=['GET', 'POST'])
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

    return render_template('account.html', title='Account',form=form)
