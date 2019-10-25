from time import sleep
#====================Logger========================
import logging
logger = logging.getLogger(__name__)
#====================Logger========================

logger.debug("Starting Uninstallation")

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
DBManager.stop_db()

logger.debug(f'Completed Uninstallation')