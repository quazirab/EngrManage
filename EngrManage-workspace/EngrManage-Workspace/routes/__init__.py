#====================Logger========================
import logging
logger = logging.getLogger(__name__)
#====================Logger========================

from flask_bcrypt import Bcrypt
from EngrManage import app
bcrypt = Bcrypt(app)

from EngrManage.routes import main_routes,admistration_routes,project_routes