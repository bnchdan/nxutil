#import ConfigParser
from configparser import ConfigParser
import logging



class NxConfig(object):
    def __init__(self, path):
        self.path = path
        self.data_dir = ""
        self.db_dir = ""
        self.core_rules = "/etc/nginx/naxsi_core.rules"
    def parse(self):
        config = ConfigParser()
        config.read_file(open(self.path))
        try:
            self.data_dir = config.get("nx_util", "data_dir")
            self.db_dir = config.get("nx_util", "database_dir")
            self.core_rules = config.get("nx_util", "naxsi_core_rules")
        except:
            logging.critical("Unable to parse configuration file :"+self.path)
            return 0
        return 1
