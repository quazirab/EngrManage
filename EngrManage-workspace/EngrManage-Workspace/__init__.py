# assign all the program information
from EngrManage.program_info.setup_info import setup_ini
setup_ini()

from flask import Flask
import sys
from time import sleep
import atexit
#====================Logger========================
import logging
logger = logging.getLogger(__name__)
#====================Logger========================

from EngrManage.database import DBManager

app = Flask(__name__)
from EngrManage.program_info.flask_config import ConfigClass
app.config.from_object(ConfigClass)
from EngrManage import routes,models
from EngrManage import session_manager


def run():
    DBManager.start_db()
    atexit.register(DBManager.stop_db)
    sleep(2)
    app.run(debug=True)

def install():
    from EngrManage import installation

def uninstallation():
    from EngrManage.installer import uninstallation

def reinstall():
    from EngrManage.installer import reinstallation