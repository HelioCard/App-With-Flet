from flet import (
    TextButton, TextField, Text, Row, 
    Column, MainAxisAlignment, AlertDialog,
)
import json
from cryptography.fernet import Fernet
import mysql.connector

from Notification import Notification

class CreateConfig(AlertDialog):
    def __init__(self, route):
        super().__init__()
        self.route = route
        self.modal = True
        self.title=Row(expand=True, controls=[Text("Configurar conexão ao banco de dados:", width=500)])

        self.tf_host = TextField(label = "Host", value="localhost")
        self.tf_user = TextField(label = "User", value="root")
        self.tf_passwd = TextField(label = "Password", value="")
        self.tf_database = TextField(label = "Database", value="")
        self.tf_port = TextField(label = "Port", value="3306")
        self.btn_back = TextButton(text="Voltar", on_click=self.back_clicked)
        self.btn_save = TextButton(text="Salvar", on_click=self.save_bd_config)

        self.actions=[
            Column(
                width=500,
                expand=True,
                controls=[
                    self.tf_host,
                    self.tf_user,
                    self.tf_passwd,
                    self.tf_database,
                    self.tf_port,
                    Row(
                        alignment=MainAxisAlignment.END,
                        controls=[
                            self.btn_back,
                            self.btn_save
                        ]
                    )
                ]
            )
        ]

    def build(self):
        return(self)
    
    def back_clicked(self, e):
        self.open = False
        self.route.page.update()

    def generate_key(self):
        return Fernet.generate_key()

    def encrypt_data(self, data, key):
        fernet = Fernet(key)
        return fernet.encrypt(data.encode())

    def write_file(self, key, encrypted_data):
        try:
            with open("data.bin", "wb") as file:
                file.write(key)
                file.write(b"\n")
                file.write(encrypted_data)
            Notification(self.route.page, "Configuração realizada com sucesso!", "green").show_message()
        except Exception as e:
            Notification(self.route.page, f"Erro ao salvar a conexão. Tente reiniciar o sistema! {e}", "red").show_message()

    def test_connection(self, config_dict):
        config = json.loads(config_dict)
        try:
            connection = mysql.connector.connect(
                host=config["host"],
                user=config["user"],
                passwd=config["passwd"],
                database=config["database"],
                port=config["port"]
            )
            connection.close()
            return True
        except Exception as e:
            Notification(self.route.page, f"Erro ao criar a conexão. Verifique os dados inseridos! {e}", "red").show_message()
            return False
        
    def save_bd_config(self, e):
        config_dict = f'''
            {{"host": "{self.tf_host.value}", "user": "{self.tf_user.value}", "passwd": "{self.tf_passwd.value}", "database": "{self.tf_database.value}", "port": "{self.tf_port.value}"}}
        '''
        if self.test_connection(config_dict):
            key = self.generate_key()
            encrypted_data = self.encrypt_data(config_dict, key)
            self.write_file(key, encrypted_data)
            self.back_clicked(e)

        