import os
import logging
import json

from dotenv import load_dotenv


class Settings:
    """Class for reading setting from envieroment"""

    _GIGACHAT_TOKEN = "GIGA_TOKEN"
    _BOT_TOKEN = "BOT_TOKEN"
    _ADMIN = "ADMIN_ID"
    CONFIG_FILE = "configs.json"

    @classmethod
    def load_data_from_file(cls):
        """tries to read data from file into environment"""
        dotenv_path = os.path.join(os.getcwd(), ".env")
        if os.path.exists(dotenv_path):
            load_dotenv(dotenv_path)
            logging.info("Data from env has been uploaded to environment")
        else:
            logging.warning(
                "Script didn't find .env file to upload file to environment"
            )

    @classmethod
    def get_token(cls):
        return os.getenv(cls._BOT_TOKEN)

    @classmethod
    def get_gigachat_token(cls):
        return os.getenv(cls._GIGACHAT_TOKEN)
    
    @classmethod
    def get_admin_id(cls):
        return os.getenv(cls._ADMIN)
    
    @classmethod
    def get_database_path(cls):
        with open(cls.CONFIG_FILE, 'r') as f:
            data = json.load(f)
        return data["database_path"]