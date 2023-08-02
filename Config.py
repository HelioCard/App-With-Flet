from cryptography.fernet import Fernet
import os
import json

from CreateConfig import CreateConfig

class Config:
    def __init__(self, route) -> None:
        self.route = route
        self.host = None
        self.user = None
        self.passwd = None
        self.database = None
        self.port = None

        self.user_name = None
        self.permission = None

    def file_exists(self, file):
        if os.path.exists(file):
            return True
        return False

    def read_file(self):
        with open("data.bin", "rb") as file:
            readed_key = file.readline().rstrip()
            readed_data = file.read()
        return readed_data, readed_key

    def decrypt_data(self, encrypted_data, key):
        fernet = Fernet(key)
        return fernet.decrypt(encrypted_data).decode()

    def set_config_data(self, data):
        self.host = data["host"]
        self.user = data["user"]
        self.passwd = data["passwd"]
        self.database = data["database"]
        self.port = data["port"]

    def set_permissions(self, name, permission):
        self.route.config.user_name = name
        self.route.config.permission = permission
        
        self.route.menu.nnrail.destinations[2].visible = (
            self.route.config.permission == "Admin"
        )
        self.route.menu.nnrail.update()

    def open_config_db(self):
        dialog = CreateConfig(self.route)
        self.route.page.dialog = dialog
        dialog.open = True
        self.route.page.update()

    def initialize(self):
        if self.file_exists("data.bin"):
            readed_data, readed_key = self.read_file()
            decrypted_data = self.decrypt_data(readed_data, readed_key)
            config_dict = json.loads(decrypted_data)
            self.set_config_data(config_dict)
        else:
            self.open_config_db()
            

    