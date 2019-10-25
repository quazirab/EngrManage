from flask_sqlalchemy import SQLAlchemy
#====================Logger========================
import logging
logger = logging.getLogger(__name__)
#====================Logger========================
from EngrManage import app
db = SQLAlchemy(app)

from EngrManage.models.user_model import User,Role,UserRoles
from EngrManage.models.project_model import Project,Client,Invoice,PO,BOM,ProjectClients,ProjectVendors