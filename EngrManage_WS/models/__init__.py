from EngrManage_WS import login_manager
from EngrManage_WS.models.user_model import User,Role,UserRoles
from EngrManage_WS.models.project_model import Project,Client,Invoice,PO,BOM,ProjectClients,ProjectVendors

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))