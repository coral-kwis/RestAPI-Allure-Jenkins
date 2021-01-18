from configparser import ConfigParser
import os

#  Create object of ConfigParser class
config = ConfigParser()

#  To read data from config file
config_file = os.path.join(os.path.dirname(__file__), '..', 'config.cfg')
config.read(config_file)

print(config.get('Section1', 'username'))
