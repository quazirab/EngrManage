# assign all the program information
from EngrManage.program_info.setup_info import setup_ini
setup_ini()

from flask import Flask

app = Flask(__name__)
from EngrManage.program_info.flask_config import ConfigClass
app.config.from_object(ConfigClass)
from EngrManage import routes,models
from EngrManage import session_manager


def run():
    app.run(debug=True)
