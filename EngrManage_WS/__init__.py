# assign all the program information

# check for all the requirements/ rasie exceptions
from EngrManage_WS.program_info.requirement_check import environment_check,db_check
from EngrManage_WS.program_info.flask_config import ConfigClass


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


bcrypt = Bcrypt()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

def create_app():
    environment_check()
    app = Flask(__name__)
    app.config.from_object(ConfigClass)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    from EngrManage_WS.main.routes import main_blueprint
    from EngrManage_WS.account.routes import account_blueprint
    from EngrManage_WS.adminstration.routes import adminstration_blueprint
    from EngrManage_WS.project.routes import project_blueprint

    app.register_blueprint(main_blueprint)
    app.register_blueprint(account_blueprint)
    app.register_blueprint(adminstration_blueprint)
    app.register_blueprint(project_blueprint)


    return app