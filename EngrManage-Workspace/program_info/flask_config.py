from EngrManage import app
from EngrManage.program_info.setup_info import info

class ConfigClass(object):
    """ Flask application config """

    # Flask settings
    SECRET_KEY = info['app']['secret_key']

    # Flask-SQLAlchemy settings
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:123456@localhost:5532/EngrManage'    # File-based SQL database
    SQLALCHEMY_TRACK_MODIFICATIONS = False    # Avoids SQLAlchemy warning

    # Flask-Mail SMTP server settings
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USE_TLS = False
    MAIL_USERNAME = 'email@example.com'
    MAIL_PASSWORD = 'password'
    MAIL_DEFAULT_SENDER = '"MyApp" <noreply@example.com>'

    # Flask-User settings
    USER_APP_NAME = "Engr Manage"   # Shown in and email templates and page footers
    USER_ENABLE_EMAIL = False        # Enable email authentication
    USER_ENABLE_USERNAME = False    # Disable username authentication
    USER_EMAIL_SENDER_NAME = USER_APP_NAME
    USER_EMAIL_SENDER_EMAIL = "noreply@example.com"
