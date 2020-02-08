#====================Logger========================
import logging
logger = logging.getLogger(__name__)
#====================Logger========================

from EngrManage.forms.user_forms import RegistrationForm,LoginForm
from EngrManage.forms.adminstration_forms import AddUserForm,AddUserGroup,EditUser
from EngrManage.forms.project_forms import ProjectFrom