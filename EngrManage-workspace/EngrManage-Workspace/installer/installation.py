from time import sleep
#====================Logger========================
import logging
logger = logging.getLogger(__name__)
#====================Logger========================

logger.debug("Starting Installation")

#initiated DB
from EngrManage.database import DBManager
DBManager.init_db()
DBManager.start_db()
sleep(5)
logger.debug(f'Creating Database')
DBManager.create_db("EngrManage")
sleep(5)

#create Model
logger.debug(f'Creating Models')
from EngrManage.models import db
db.create_all()

#Add Admistration and User in Role Model 
# from EngrManage.model import Role
# role_admin = Role(tag='Admin')
# role_user = Role(tag='User')
# db.session.add(role_admin)
# db.session.add(role_user)
# db.session.commit()
# sleep(5)
DBManager.stop_db()

