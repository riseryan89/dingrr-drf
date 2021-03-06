from configparser import ConfigParser


conf = ConfigParser()
conf.read('.key_store')
CONST_DB_HOST_DEBUG = conf['DB']['HOST_DEBUG']
CONST_DB_HOST_PROD = conf['DB']['HOST_PROD']
CONST_DB_PORT = int(conf['DB']['PORT'])
CONST_DB_USER = conf['DB']['USER']
CONST_DB_PW = conf['DB']['PW']
CONST_DB_NAME = conf['DB']['DB_NAME']
CONST_DB_CHARSET = conf['DB']['CHARSET']
