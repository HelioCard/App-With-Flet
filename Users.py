from flet import (UserControl, Row, Column, Container, Text, TextField, IconButton, DataTable, 
                  DataRow, DataColumn, DataCell, icons, VerticalDivider, ListView, Dropdown, dropdown,
                  OutlinedButton, FontWeight, CrossAxisAlignment, MainAxisAlignment, KeyboardEvent)
from Database import UserDatabase
from datetime import date
import bcrypt
from ConfirmDialog import ConfirmDialog
from Notification import Notification

class Users(UserControl):
    def __init__(self, route):
        super().__init__()
        self.route = route

        self.tf_find_user = TextField(label="Buscar...", on_change=self.find_user)

        self.dt_users = DataTable(                                            
            expand=True,
            columns=[
                DataColumn(Text('ID'), numeric=True), 
                DataColumn(Text('NOME')), 
                DataColumn(Text('USUÁRIO')), 
                DataColumn(Text('ACESSO')), 
                DataColumn(Text('AÇÕES')), 
            ],
            rows=[
                DataRow(
                    cells=[
                        DataCell(Text('01')),
                        DataCell(Text("John Player Special")),
                        DataCell(Text("JPS_Special")),
                        DataCell(Text("Admin")),
                        DataCell(Row([IconButton(icon=icons.EDIT, icon_color='blue'), IconButton(icon=icons.DELETE, icon_color='red')])),
                    ],
                ),
            ],
        )

        self.new_user_text = Text('Novo Usuário', size=18, weight=FontWeight.W_500)
        self.tf_name = TextField(autofocus=True, label='Nome', prefix_icon=icons.PERSON_2_ROUNDED, on_change=self.analyze_register_user, on_focus=self.on_enter_fields)
        self.tf_user = TextField(label='Usuário', prefix_icon=icons.ASSIGNMENT_IND_ROUNDED, on_change=self.analyze_register_user, on_focus=self.on_enter_fields)
        self.dp_access = Dropdown(label='Acesso', options=[dropdown.Option('Usuario'), dropdown.Option('Admin')], value="Admin", prefix_icon=icons.MANAGE_ACCOUNTS_ROUNDED, on_change=self.analyze_register_user, on_focus=self.on_enter_fields)
        self.tf_pass1 = TextField(label='Insira a senha', password=True, prefix_icon=icons.PASSWORD, on_change=self.analyze_register_user, on_focus=self.on_enter_fields)
        self.tf_pass2 = TextField(label='Repita a senha', password=True, prefix_icon=icons.PASSWORD, on_change=self.analyze_register_user, on_focus=self.on_enter_fields)
        self.btn_register_user = OutlinedButton(text='Cadastrar', disabled=True, icon=icons.ADD_OUTLINED, width=140, on_click=self.btn_save_edit_clicked)
        self.btn_cancel_edition = OutlinedButton(text='Cancelar',icon=icons.CANCEL_OUTLINED, visible=False, width=140, on_click=self.edit_cancelled)

        # Sequencia de tabulação do formulário:
        self.route.page.on_keyboard_event = self.on_keyboard
        self.next_field = {
            "Nome": self.tf_user.focus,
            "Usuário": self.dp_access.focus,
            "Acesso": self.tf_pass1.focus,
            "Insira a senha": self.tf_pass2.focus,
            "Repita a senha": self.btn_register_user.focus,
        }
        self.label = ""

    def build(self):        
        self.users_content = Container(
            #bgcolor='red',        
            padding=0,
            border_radius=5,
            expand=True,
            content=Column(
                controls=[
                    # Corpo principal
                    Container(
                        #bgcolor='white',
                        expand=True,
                        content=Row(                        
                            vertical_alignment=CrossAxisAlignment.START,
                            controls=[
                                Container(
                                    #bgcolor='red',                              
                                    expand=5,
                                    border_radius=5,
                                    padding=15,
                                    content=Column(                                    
                                        expand=True,                                    
                                        horizontal_alignment=CrossAxisAlignment.CENTER,
                                        controls=[
                                            self.tf_find_user,
                                            ListView(
                                                expand=True,                                            
                                                controls=[
                                                    self.dt_users, 
                                                ]
                                            )
                                        ]
                                    ),
                                ),
                                VerticalDivider(width=1),
                                Container(
                                    #bgcolor='white',                                
                                    expand=2,
                                    border_radius=5,
                                    padding=15,
                                    content=Column(
                                        horizontal_alignment=CrossAxisAlignment.CENTER,
                                        spacing=20,
                                        controls=[
                                            self.new_user_text,
                                            self.tf_name,
                                            self.tf_user,
                                            self.dp_access,
                                            self.tf_pass1,
                                            self.tf_pass2,
                                            Row(alignment=MainAxisAlignment.CENTER, controls=[self.btn_cancel_edition, self.btn_register_user])
                                        ]
                                    )
                                )
                            ]
                        )
                    )
                ]
            )
        )

        self.content = Row(
            expand=True,
            spacing=10,
            controls=[                
                self.users_content,        
            ]
        )

        return self.content

    def on_keyboard(self, e: KeyboardEvent):
        if e.key == "Tab" and self.route.page.route == "/users":
            self.next_field[self.label]()
    
    def clean_text_fields(self):
        for control in [self.tf_name, self.tf_user, self.tf_pass1, self.tf_pass2, self.dp_access]:
            control.value = ""
            control.error_text = ""
        self.dp_access.value = 'Usuario'
        self.dp_access.update()
        self.btn_register_user.disabled = True
        self.update()

    def create_hash(self, password):
        salt = bcrypt.gensalt()
        hashed_pass = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_pass.decode('utf-8')

    def register_user(self, e):        
        today = date.today()
        form_date = today.strftime('%Y-%m-%d')
        hashed_pass = self.create_hash(self.tf_pass1.value)

        mydb = UserDatabase(self.route)
        mydb.connect()
        fulldataset = [self.tf_name.value, self.tf_user.value, hashed_pass, form_date, self.dp_access.value]
        result = mydb.register_user(fulldataset)
        mydb.close()

        if result == 'success':
            Notification(self.route.page, 'Usuário cadastrado com sucesso!', 'green').show_message()
            self.fill_in_table_users()
            self.clean_text_fields()
        else:
            Notification(self.route.page, f'Erro ao cadastrar o usuário: {result}', 'red').show_message()
            
        self.route.page.update()

    def fill_in_table_users(self):
        self.dt_users.rows.clear()
        mydb = UserDatabase(self.route)
        mydb.connect()
        result = mydb.select_all_users()
        mydb.close()

        for data in result:        
            self.dt_users.rows.append(
                DataRow(
                    cells=[
                        DataCell(Text(data[0])),
                        DataCell(Text(data[1])),
                        DataCell(Text(data[2])),
                        DataCell(Text(data[3])),
                        DataCell(Row([IconButton(icon=icons.EDIT_OUTLINED, icon_color='blue', tooltip="Editar", data=data, on_click=self.edit_clicked), IconButton(icon=icons.DELETE_OUTLINED, icon_color='red', tooltip="Excluir", data=data, on_click=self.delete_clicked)])),
                    ],
                )
            )
        self.dt_users.update()

    def initialize(self):
        print("Initializing Users's Page")
        self.btn_register_user.disabled = True
        self.tf_find_user.value = ""
        self.tf_name.value = ""
        self.tf_user.value = ""
        self.tf_pass1.value = ""
        self.tf_pass2.value = ""
        self.dp_access.value = "Usuario"
        self.fill_in_table_users()
        self.clean_text_fields()
        self.update()

    def analyze_register_user(self, e):        
        if (
            self.tf_name.value == ""
            and self.tf_user.value == ""
            and self.tf_pass1.value == ""
            and self.tf_pass2.value == ""            
        ):
            self.btn_register_user.disabled = True
            self.tf_name.error_text = ""
            self.tf_user.error_text = ""
            self.tf_pass1.error_text = ""
            self.tf_pass2.error_text = ""            
            self.update()            
            return
        
        if (
            self.tf_name.value != ""
            and self.tf_user.value != ""
            and self.tf_pass1.value != ""
            and self.tf_pass2.value != ""            
        ):  
            if self.tf_pass1.value != self.tf_pass2.value:
                self.tf_pass1.error_text = "Senhas não conferem!"
                self.tf_pass2.error_text = "Senhas não conferem!"
                self.btn_register_user.disabled = True
                self.update()
                return
            self.btn_register_user.disabled = False
            self.tf_name.error_text = ""
            self.tf_user.error_text = ""
            self.tf_pass1.error_text = ""
            self.tf_pass2.error_text = ""
            self.update()
            return
        
        for control in [self.tf_name, self.tf_user, self.tf_pass1, self.tf_pass2]:
            if control.value == "":
                control.error_text = "Campos Obrigatórios!"
                self.btn_register_user.disabled = True
            else:
                control.error_text = ""
        self.update()

    def edit_clicked(self, e):
        mydb = UserDatabase(self.route)
        mydb.connect()
        result = mydb.select_one_user(e.control.data[0])
        mydb.close()

        self.new_user_text.value = 'Editar Usuário'
        self.tf_name.value = result[1]
        self.tf_user.value = result[2]
        self.dp_access.value = result[5]
        
        self.btn_register_user.text = 'Salvar'
        self.btn_register_user.data = result[0]
        self.btn_cancel_edition.visible=True
        self.update()

    def btn_save_edit_clicked(self, e):
        if not self.btn_cancel_edition.visible:
            self.register_user(e)
        else:
            self.update_user(e)

    def update_user(self, e):
        t = date.today()
        today = t.strftime('%Y-%m-%d')
        hashed_pass = self.create_hash(self.tf_pass1.value)
        fulldata = [self.btn_register_user.data, self.tf_name.value, self.tf_user.value, hashed_pass, today, self.dp_access.value]
        mydb = UserDatabase(self.route)
        mydb.connect()
        result = mydb.update_user(fulldata)
        mydb.close()
        if result == 'success':
            Notification(self.page, 'Usuário atualizado com sucesso!', 'green').show_message()
            self.edit_cancelled(e)
            self.fill_in_table_users()
        else:
            Notification(self.page, "Erro ao atualizar o usuário. Verifique dos dados inseridos!", "red").show_message()
        
        self.new_user_text.value = 'Novo Usuário'
        self.route.page.update()

    def edit_cancelled(self, e):
        self.new_user_text.value = 'Novo Usuário'
        self.btn_register_user.text = 'Cadastrar'
        self.btn_cancel_edition.visible=False
        self.btn_register_user.disabled = True
        self.clean_text_fields()
        self.update()

    def get_user_to_be_deleted(self, e):
        return e.control.data[1]

    def delete_clicked(self, e):
        name = self.get_user_to_be_deleted(e).upper()
        if name == self.route.config.user_name:
            Notification(self.route.page, "Não é possível excluir o próprio cadastro de administrador!", "orange").show_message()
            return
        self.get_user_to_be_deleted(e)
        dialog = ConfirmDialog(self.delete_user, "Por favor, confirme:", 'Tem certeza que deseja excluir o usuário?')
        dialog.data = e.control.data[0]
        self.page.dialog = dialog
        dialog.open = True
        self.edit_cancelled(e)
        self.route.page.update()

    def delete_user(self, id):
        mydb = UserDatabase(self.route)
        mydb.connect()
        result = mydb.delete_user(id)
        mydb.close()
        
        if result == 'success':
            Notification(self.page, 'Usuário excluído com sucesso!', 'green').show_message()
            self.fill_in_table_users()
        else:
            Notification(self.page, 'Erro ao excluir o usuário!', 'red').show_message()
        
    def on_enter_fields(self, e):
        self.label = e.control.label
        
    def find_user(self, e):
        if self.tf_find_user.value == "":
            self.fill_in_table_users()
            return
        mydb = UserDatabase(self.route)
        mydb.connect()
        result = mydb.find_user(self.tf_find_user.value)
        mydb.close()

        self.dt_users.rows.clear()
        for data in result:        
            self.dt_users.rows.append(
                DataRow(
                    cells=[
                        DataCell(Text(data[0])),
                        DataCell(Text(data[1])),
                        DataCell(Text(data[2])),
                        DataCell(Text(data[3])),
                        DataCell(Row([IconButton(icon=icons.EDIT_OUTLINED, icon_color='blue', tooltip="Editar", data=data, on_click=self.edit_clicked), IconButton(icon=icons.DELETE_OUTLINED, icon_color='red', tooltip="Excluir", data=data, on_click=self.delete_clicked)])),
                    ],
                )
            )
        self.dt_users.update()

