from flask_login import LoginManager
from EngrManage_WS import app
from EngrManage_WS.models import User,db

#====================Logger========================
import logging
logger = logging.getLogger(__name__)
#====================Logger========================

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))