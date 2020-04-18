from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField 
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from EngrManage_WS.models import User,Role

class AddUserForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self,username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already exists')
    
    def validate_email(self,email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email already registered')

class AddUserGroup(FlaskForm):
    role = StringField('Role',
                           validators=[DataRequired(), Length(min=2, max=50)])
    submit = SubmitField('Add Role')

    def validate_role(self,role):
        role = Role.query.filter_by(tag=role.data).first()
        if role:
            raise ValidationError('Role already exists')
    
class EditUser(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    # password = PasswordField('New Password', validators=[DataRequired()])
    # confirm_password = PasswordField('Confirm New Password',
    #                                  validators=[DataRequired(), EqualTo('password')])
    
    submit = SubmitField('Save Edits')

    def __init__(self,old_user):
        FlaskForm.__init__(self)
        self.old_user=old_user
     
    def validate_username(self,username):
        if username.data != self.old_user.username:
            print (username.data)
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('Username already exists')
    
    def validate_email(self,email):
        if email.data != self.old_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Email already registered')