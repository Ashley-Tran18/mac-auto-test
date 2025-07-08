import json
import os

class ConfigReader:
    _config = None

    @staticmethod
    def load_config():
        if ConfigReader._config is None:
            config_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'testsetting.json')
            # Load config.json
            with open(config_path, 'r') as config_file:
                ConfigReader._config = json.load(config_file)
        return ConfigReader._config

    @staticmethod
    def get_base_url():
        return ConfigReader.load_config()['base_url']
    
    @staticmethod
    def get_timeout():
        return ConfigReader.load_config()['timeout']

    # Cách 2
    # @staticmethod
    # def get_username():
    #   return ConfigReader.load_config()['username']
    # @staticmethod
    # def get_password():
    #   return ConfigReader.load_config()['password']
    
    # Cách 3
    @staticmethod
    def get_username_password():
        config = ConfigReader.load_config()
        return config['username'], config['password']
    
    
    @staticmethod
    def get_vacancy_info():
        return ConfigReader.load_config()['new-user']

        
        



