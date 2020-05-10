from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from EngrManage_WS.models import Project 

#====================Logger========================
import logging
logger = logging.getLogger(__name__)
#====================Logger========================


class ProjectFrom(FlaskForm):
    name = StringField('Name',
                           validators=[DataRequired(), Length(min=2, max=20)])
    description = StringField('Description',
                        validators=[DataRequired(), Length(min=2, max=120)])
    submit = SubmitField('Create')

    def validate_name(self,name):
        name = Project.query.filter_by(name=name.data).first()
        if name:
            raise ValidationError('Project already exists')
