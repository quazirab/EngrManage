#====================Logger========================
import logging
logger = logging.getLogger(__name__)
#====================Logger========================

from EngrManage_WS.forms.user_forms import RegistrationForm,LoginForm
from EngrManage_WS.forms.adminstration_forms import AddUserForm,AddUserGroup,EditUser
from EngrManage_WS.forms.project_forms import ProjectFrom
from EngrManage_WS.forms.account_forms import UpdateAccountForm