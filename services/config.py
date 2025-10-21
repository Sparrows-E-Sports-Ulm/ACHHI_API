from pyhocon import ConfigFactory

class Config():
    def __init__(self, config_file):
        conf = ConfigFactory.parse_file("resources/application.conf")
