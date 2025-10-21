from config import Config

class APIServices():

    config: Config

    def __init__(self, config_file : str):
        self.config = Config(config_file)