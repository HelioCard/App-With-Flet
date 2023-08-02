from flet import (UserControl, Row, Column, Container, Text, TextField, IconButton, DataTable, OutlinedButton, 
                  DataRow, DataColumn, DataCell, icons, AlertDialog, TextThemeStyle, TextAlign,
                  VerticalDivider, ListView, TextButton, MainAxisAlignment, CrossAxisAlignment)
from PYBRDOC import CPF, Cnpj
from datetime import date

from Database import CustomerDatabase, SalesDatabase
from Notification import Notification
from Validator import Validator

class RegisterCustomer(UserControl):
    def __init__(self, route):
        super().__init__()
        self.route = route

        self.adress_list = []

        self.text_new_customer = Text('Novo Cliente:', style=TextThemeStyle.TITLE_LARGE)
        self.tf_id = TextField(label='ID (Aut.)', read_only=True, expand=1, text_align=TextAlign.CENTER, value='515')
        self.tf_name = TextField(label='Nome', expand=4, autofocus=True, on_change=self.analyze_register_customer)
        self.tf_CPF = TextField(label='CPF', expand=2, on_blur=self.check_cpf_cnpj, on_change=self.analyze_register_customer)
        self.tf_phone = TextField(label='Telefone', expand=2, on_change=self.analyze_register_customer)
        self.tf_email = TextField(label='E-mail', expand=3, on_change=self.analyze_register_customer)
        self.tf_observ = TextField(label='Observação', expand=True, on_change=self.analyze_register_customer)
        self.btn_add_adress = IconButton(tooltip='Adicionar Endereço', icon=icons.ADD_ROAD_OUTLINED, icon_size=32, on_click=self.add_adress_clicked)
        self.btn_add_save_customer = OutlinedButton(text='Salvar', icon=icons.SAVE_OUTLINED, on_click=self.add_save_clicked)
        self.btn_back = IconButton(tooltip='Voltar', icon=icons.ARROW_BACK_OUTLINED, icon_size=32, on_click=self.back_clicked)
        self.text_total = Text('R$ 350,00', style=TextThemeStyle.TITLE_MEDIUM)
        
        # Dialog to register adress:
        self.tf_adress = TextField(label='Rua, número, bairro', autofocus=True,)
        self.tf_city = TextField(label='Cidade', expand=3)
        self.tf_UF = TextField(label='UF', expand=1)
        self.tf_CEP = TextField(label='CEP', expand=1)
        self.btn_ok = TextButton('Inserir', on_click=self.ok_clicked)
        self.btn_cancel = TextButton('Cancelar', on_click=self.cancel_clicked)
        self.dialog = AlertDialog(
            modal=True,
            title=Row(expand=True, controls=[Text("Novo endereço:", expand=True, width=800)]),
            actions=[
                Column(
                    controls=[
                        self.tf_adress,
                        Row(
                            controls=[
                                self.tf_city,
                                self.tf_UF,
                                self.tf_CEP,
                            ]
                        )
                    ]
                ),
                Row(height=10), # Spacer
                Row(
                    alignment=MainAxisAlignment.END,
                    controls=[
                        self.btn_cancel,
                        self.btn_ok,
                    ]
                )
            ],
            actions_alignment=MainAxisAlignment.END,
        )

        self.dt_adress = DataTable(                                            
            expand=True,
            divider_thickness=0.4,
            columns=[
                DataColumn(Text('Endereço')), 
                DataColumn(Text('Cidade')), 
                DataColumn(Text('UF')), 
                DataColumn(Text('CEP')), 
                DataColumn(Text('Excluir')), 
            ],
        )

        self.dt_order_history = DataTable(
            column_spacing=15,
            divider_thickness=0.4,
            #heading_row_color=colors.ON_INVERSE_SURFACE,
            expand=True,
            columns=[
                DataColumn(Text('Pedido')), 
                DataColumn(Text('Data')), 
                DataColumn(Text('Valor')),
                DataColumn(Text('Ver')),                                                 
            ],
        )

    def build(self):
        page_content = Container(
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
                                        alignment=MainAxisAlignment.START,
                                        expand=True,
                                        horizontal_alignment=CrossAxisAlignment.CENTER,
                                        controls=[
                                            Row(
                                                alignment=MainAxisAlignment.START,
                                                controls=[
                                                    self.text_new_customer,
                                                    Row(expand=True), # Spacer
                                                    self.btn_back,
                                                ]
                                            ),
                                            Row(
                                                controls=[
                                                    self.tf_id,
                                                    self.tf_name,
                                                ]
                                            ),
                                            Row(
                                                controls=[
                                                    self.tf_CPF,
                                                    self.tf_phone,
                                                    self.tf_email,
                                                ]
                                            ),
                                            Row(
                                                controls=[
                                                    self.tf_observ,
                                                    self.btn_add_adress,
                                                ]
                                            ),
                                            ListView(
                                                expand=True,
                                                controls=[
                                                    self.dt_adress,
                                                ]
                                            ),
                                            Row(
                                                alignment=MainAxisAlignment.END,
                                                controls=[
                                                    self.btn_add_save_customer,
                                                ]
                                            ),
                                        ]
                                    )
                                ),

                                VerticalDivider(width=1),

                                Container(
                                    #bgcolor='red',
                                    expand=2,
                                    border_radius=5,
                                    padding=15,
                                    content=Column(
                                        alignment=MainAxisAlignment.START,
                                        horizontal_alignment=CrossAxisAlignment.CENTER,
                                        spacing=20,
                                        controls=[
                                            Text('Histórico de Pedidos', style=TextThemeStyle.TITLE_MEDIUM),
                                            ListView(
                                                expand=True,
                                                controls=[
                                                    self.dt_order_history,
                                                ]
                                            ),
                                            Row(
                                                alignment=MainAxisAlignment.END,
                                                controls=[
                                                    Text('Total:', style=TextThemeStyle.TITLE_MEDIUM),
                                                    self.text_total,
                                                ]
                                            )
                                        ]
                                    )
                                )
                            ]
                        )
                    )
                ]
            )
        )

        content = Row(
            expand=True,
            spacing=10,
            controls=[
                page_content,
            ]
        )
        return content
    
    def add_adress_clicked(self, e):
        for control in [self.tf_adress, self.tf_city, self.tf_UF, self.tf_CEP]:
            control.value = ''
        self.route.page.dialog = self.dialog
        self.dialog.open = True
        self.route.page.update()
    
    def ok_clicked(self, e):
        data = (str(self.tf_CPF.value), self.tf_adress.value, self.tf_city.value, self.tf_UF.value, self.tf_CEP.value)
        self.adress_list.append(data)
        self.dt_adress.rows.append(
            DataRow(
                cells=[
                    DataCell(Text(value=self.tf_adress.value)),
                    DataCell(Text(value=self.tf_city.value)),
                    DataCell(Text(value=self.tf_UF.value)),
                    DataCell(Text(value=self.tf_CEP.value)),
                    DataCell(Row([IconButton(icon=icons.DELETE_OUTLINED, icon_color='red', data=len(self.adress_list)-1, on_click=self.delete_adress)])),
                ],
            ),
        )
        
        self.dt_adress.update()
        self.dialog.open = False
        self.analyze_register_customer(e)
        self.route.page.update()

    def cancel_clicked(self, e):
        self.dialog.open = False
        self.route.page.update()

    def delete_adress(self, e):
        del self.adress_list[e.control.data]
        self.load_adresses(self.adress_list)
        self.analyze_register_customer(e)

    def load_adresses(self, adress_list):
        self.dt_adress.rows.clear()
        for row, data in enumerate(adress_list):
            self.dt_adress.rows.append(
                DataRow(
                    cells=[
                        DataCell(Text(value=data[1])),
                        DataCell(Text(value=data[2])),
                        DataCell(Text(value=data[3])),
                        DataCell(Text(value=data[4])),
                        DataCell(Row([IconButton(icon=icons.DELETE_OUTLINED, icon_color='red', data=row, on_click=self.delete_adress)])),
                    ],
                ),
            )
        self.dt_adress.update()
        self.route.page.update()
    
    def initialize(self):
        print("Initializing Register Customer's Page")
        self.adress_list = []
        self.clear_fields()
        self.text_new_customer.value = "Novo Cliente:"
        self.update()

    def back_clicked(self, e):
        self.route.page.go("/customers")
        self.route.bar.set_title('Clientes')
        self.route.page.update

    def check_cpf_cnpj(self, e):
        if self.tf_CPF.value == "":
            self.tf_CPF.error_text = ""
            self.tf_CPF.update()
            return False

        cpf = CPF(self.tf_CPF.value)
        if cpf.isValid:
            self.tf_CPF.value = cpf
            self.tf_CPF.error_text = ""
            self.tf_CPF.update()
            return True
        
        cnpj = Cnpj(self.tf_CPF.value)
        if cnpj.isValid:
            self.tf_CPF.value = cnpj
            self.tf_CPF.error_text = ""
            self.tf_CPF.update()
            return True
        
        self.tf_CPF.error_text = "CPF ou CNPJ inválido!"
        self.update()
        self.route.page.update()
        return False

    def analyze_register_customer(self, e):
        if (
            self.tf_name.value == ""
            and self.tf_CPF.value == ""
            and self.tf_phone.value == ""
            and self.tf_email.value == ""
        ):
            self.btn_add_save_customer.disabled = True
            for control in [self.tf_name, self.tf_CPF, self.tf_phone, self.tf_email]:
                control.error_text = ""
            self.update()
            return
        

        if (
            self.tf_name.value != ""
            and self.tf_CPF.value != ""
        ):
            if self.check_cpf_cnpj(e) == False:
                self.tf_CPF.error_text = 'CPF ou CNPJ inválido!'
                self.btn_add_save_customer.disabled = True
                self.update()
                return
            self.btn_add_save_customer.disabled = False
            for control in [self.tf_name, self.tf_CPF, self.tf_phone, self.tf_email]:
                control.error_text = ""
                control.update()
            self.update()
            return
        

        for control in [self.tf_name, self.tf_CPF]:
            if control.value == "":
                control.error_text = "Campo Obrigatório!"
                self.btn_add_save_customer.disabled = True
            else:
                control.error_text = ""
        self.update()

    def clear_fields(self):
        for control in [self.tf_id, self.tf_name, self.tf_CPF, self.tf_phone, self.tf_email, self.tf_observ]:
            control.value = ""
            control.error_text = ""
        self.btn_add_save_customer.disabled = True
        self.dt_adress.rows.clear()
        self.dt_order_history.rows.clear()
        self.text_total.value = ""
        self.tf_name.focus()
        self.update()
        self.route.page.update()

    def register_customer(self, e):
        today = date.today()
        data_customer = [self.tf_name.value.upper(),  str(self.tf_CPF.value), self.tf_phone.value, self.tf_email.value, self.tf_observ.value, today.strftime('%Y-%m-%d')]
        mydb = CustomerDatabase(self.route)
        mydb.connect()
        result = mydb.register_customer(data_customer)

        if result != 'success':
            Notification(self.page, f'Erro ao registrar o cliente: "{data_customer[0]}"! Erro: {result}', "red").show_message()
            return
        
        if len(self.adress_list) > 0:
            for data in self.adress_list:
                result = mydb.register_adress(data)
        mydb.close()

        if result == 'success':
            Notification(self.page, "Cliente registrado com sucesso!", "green").show_message()
        else:
            Notification(self.page, f"Erro ao registrar cliente: {result}", "red").show_message()
        
        self.clear_fields()
        self.route.page.update()

    def load_customer(self, cpf_cnpj):
        mydb = CustomerDatabase(self.route)
        mydb.connect()
        data_customer = mydb.select_one_customer(cpf_cnpj)
        data_adress = mydb.select_adresses(cpf_cnpj)
        mydb.close()
        self.adress_list = [(cpf_cnpj,) + tupla for tupla in data_adress] # inserts cpf_cnpj in the 0 index of each tuple

        self.tf_id.value = str(data_customer[0][0])
        self.tf_name.value = data_customer[0][1]
        self.tf_CPF.value = data_customer[0][2]
        self.tf_phone.value = data_customer[0][3]
        self.tf_email.value = data_customer[0][4]
        self.tf_observ.value = data_customer[0][5]
        self.update()
        self.load_adresses(self.adress_list)

    def update_customer(self, e):
        data_customer = [int(self.tf_id.value), self.tf_name.value, str(self.tf_CPF.value), self.tf_phone.value, self.tf_email.value, self.tf_observ.value,]

        mydb = CustomerDatabase(self.route)
        mydb.connect()
        result = mydb.update_customer(data_customer)
        
        if result != 'success':
            Notification(self.page, f'Erro ao atualizar o cliente: "{data_customer[1]}"! Erro: {result}', 'red').show_message()
            return
        
        if len(self.adress_list) > 0:
            for data in self.adress_list:
                result = mydb.register_adress(data)
        mydb.close()

        if result == 'success':
            Notification(self.page, f'Cliente "{data_customer[1]}" atualizado com sucesso!', 'green').show_message()
        else:
            Notification(self.page, f'Erro ao atualizar o cliente: "{data_customer[1]}"! Erro: {result}', 'red').show_message()
            
        self.clear_fields()
        self.route.page.update()

    def add_save_clicked(self, e):
        if self.tf_id.value == "":
            self.register_customer(e)
        else:
            self.update_customer(e)

    def fill_in_history_table(self, fulldata):
        self.dt_order_history.rows.clear()
        for data in fulldata:
            self.dt_order_history.rows.append(
                DataRow(
                    cells=[
                        DataCell(Text(data[0])),
                        DataCell(Text(data[1])),
                        DataCell(Text(f"R${Validator.format_to_currency(data[2])}")),
                        DataCell(IconButton(icon=icons.VISIBILITY_OUTLINED, icon_color="blue", data=data[0], tooltip="Visualizar pedido", on_click=self.see_sale_clicked))
                    ]
                )
            )
        self.dt_order_history.update()

    def get_sales_data_from_db(self):
        mydb = SalesDatabase(self.route)
        mydb.connect()
        result = mydb.select_sales_history(self.tf_id.value)
        mydb.close()
        total = sum(map(lambda x: x[2], result))
        self.text_total.value = f"R${Validator.format_to_currency(total)}"
        self.update()
        self.fill_in_history_table(result)
    
    def see_sale_clicked(self, e):
        self.route.page.go("/sales")
        self.route.bar.set_title("Vendas")
        self.route.menu.nnrail.selected_index = 4
        self.route.menu.update()
        self.route.page.update()

        self.route.sales.select_sale_clicked(e.control.data)
