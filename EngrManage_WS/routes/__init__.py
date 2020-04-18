from flask_bcrypt import Bcrypt
from EngrManage_WS import app
bcrypt = Bcrypt(app)

from EngrManage_WS.routes import main_routes,admistration_routes,project_routes,account_routes