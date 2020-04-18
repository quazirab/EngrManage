# assign all the program information

from flask import Flask

app = Flask(__name__)
from EngrManage_WS.program_info.flask_config import ConfigClass
app.config.from_object(ConfigClass)
from EngrManage_WS import routes,models
from EngrManage_WS import session_manager


def run():
    app.run(debug=True)
