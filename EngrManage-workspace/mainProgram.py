import sys
#====================Logger========================
import logging, logging.config
logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)
#====================Logger========================




if __name__ == "__main__":
    if "install" in sys.argv:
        from EngrManage import install
        install()
    elif "reinstall" in sys.argv:
        from EngrManage import reinstall
        reinstall()
    else:
        from EngrManage import run
        run()
    