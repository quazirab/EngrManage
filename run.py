import sys
import os

def first_run_check():
    if not os.path.exists(os.environ['EM_DBDIR']):
        os.makedirs(os.environ['EM_DBDIR'])
    if not os.path.exists(os.path.join(os.environ['EM_DBDIR'],"engrmanage.db")):
        from EngrManage_WS.models import db,Role
        db.create_all()
        db.session.add(Role(tag='Admin'))
        db.session.commit()

if __name__ == "__main__":
    # check for if 
    first_run_check()


    from EngrManage_WS import run
    run()
    