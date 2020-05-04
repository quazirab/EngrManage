import os

def environment_check():
    required_envs = ['EM_SECRET','EM_DBDIR']
    
    for required_env in required_envs:
        try:
            os.environ[required_env]
        except KeyError:
            raise KeyError(f'Need to setup {required_env} environment')

def db_check():
    if not os.path.exists(os.environ['EM_DBDIR']):
        os.makedirs(os.environ['EM_DBDIR'])
    if not os.path.exists(os.path.join(os.environ['EM_DBDIR'],"engrmanage.db")):
        from EngrManage_WS.models import db,Role
        db.create_all()
        db.session.add(Role(tag='Admin'))
        db.session.commit()