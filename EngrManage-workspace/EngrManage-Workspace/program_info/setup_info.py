import os
from configparser import ConfigParser

#====================Logger========================
import logging
logger = logging.getLogger(__name__)
#====================Logger========================


info = {}

def setup_ini():
    if 'EngrManage.ini' in os.listdir(os.getcwd()):
        try:
            systemFile = ConfigParser()
            systemFile.read('EngrManage.ini')
            systemDict = {s:dict(systemFile.items(s)) for s in systemFile.sections()}
            add_info(systemDict)
        except Exception as E:
            logger.error(f'Problem Reading Ini file, Error : {E}')

#setup used to add more dict to info
def add_info(Dict):
    for key in Dict:
        info[key] = Dict[key]
    logger.debug(f'New Info Dictionary : {info}')