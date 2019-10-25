from time import sleep
#====================Logger========================
import logging
logger = logging.getLogger(__name__)
#====================Logger========================

logger.debug("Starting Reinstallation")

#initiated DB
from EngrManage.database import DBManager
DBManager.init_db()
DBManager.start_db()
sleep(10)
try :
    from EngrManage.models import db
    db.drop_all()
except :
    logger.warning(f'Database Doesnt Exist')

logger.debug(f'Creating Database')
DBManager.create_db("EngrManage")

#create Model
logger.debug(f'Creating Models')
from EngrManage.models import db
db.create_all()

#Add Admistration and User in Role Model 
from EngrManage.models import Role
role_admin = Role(tag='Admin')
role_user = Role(tag='User')
db.session.add(role_admin)
db.session.add(role_user)
db.session.commit()
sleep(5)
DBManager.stop_db()