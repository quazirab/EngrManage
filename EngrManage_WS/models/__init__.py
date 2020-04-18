from flask_sqlalchemy import SQLAlchemy
#====================Logger========================
import logging
logger = logging.getLogger(__name__)
#====================Logger========================
from EngrManage_WS import app
db = SQLAlchemy(app)

from EngrManage_WS.models.user_model import User,Role,UserRoles
from EngrManage_WS.models.project_model import Project,Client,Invoice,PO,BOM,ProjectClients,ProjectVendors