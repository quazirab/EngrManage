from flask import abort
from flask_login import current_user
from EngrManage.session_manager import login_manager
from EngrManage.models import Role
from functools import wraps
#====================Logger========================
import logging
logger = logging.getLogger(__name__)
#====================Logger========================

def login_role_required(roles=["ANY"]):
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            if not current_user.is_authenticated:
               return login_manager.unauthorized()
            special_roles = []
            for role in roles:
                special_roles.append(Role.query.filter_by(tag=role).first())
            if not any(elem in current_user.roles for elem in special_roles):
                abort(403)
                return login_manager.unauthorized()      
            return fn(*args, **kwargs)
        return decorated_view
    return wrapper