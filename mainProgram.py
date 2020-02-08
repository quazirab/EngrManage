import sys
#====================Logger========================
import logging, logging.config
logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)
#====================Logger========================




if __name__ == "__main__":
    from EngrManage import run
    run()
    