from flet import (UserControl, Row, Column, Container, Text, TextField, IconButton, DataTable, MainAxisAlignment,
                  DataRow, DataColumn, DataCell, icons, colors, TextStyle, Card, FontWeight, TextAlign, Divider,
                  ListView, border_radius, padding, border, FilePickerResultEvent, CrossAxisAlignment)

from Validator import Validator
from Database import SalesDatabase, ProductsDatabase, CustomerDatabase
from Notification import Notification
from ConfirmDialog import ConfirmDialog
from Reports import SaleReport
import contextlib

class Sales(UserControl):
    def __init__(self, route):
        super().__init__()
        self.route = route

        self.tf_find_sale = TextField(label="Buscar...", expand=True, dense=True, prefix_icon=icons.SEARCH_ROUNDED, on_submit=self.find_sale)
        self.btn_new_sale = IconButton(icon=icons.ADD_SHOPPING_CART_ROUNDED, icon_color=colors.PRIMARY, tooltip="Nova Venda", icon_size=36, on_click=self.new_sale_clicked)
        self.btn_filter_today = IconButton(icon=icons.TODAY_ROUNDED, selected_icon=icons.TODAY_ROUNDED, selected_icon_color=colors.PRIMARY, data="select_sales_from_today", tooltip="Vendas de Hoje", on_click=self.filter_buttons_clicked)
        self.btn_filter_previous_seven = IconButton(icon=icons.DATE_RANGE_ROUNDED, selected_icon=icons.DATE_RANGE_ROUNDED, selected_icon_color=colors.PRIMARY, selected=True, data="select_sales_from_previous_seven", tooltip="Vendas dos Últimos Sete Dias", on_click=self.filter_buttons_clicked)
        self.btn_filter_previous_thirty = IconButton(icon=icons.CALENDAR_MONTH_ROUNDED, selected_icon=icons.CALENDAR_MONTH_ROUNDED, selected_icon_color=colors.PRIMARY, data="select_sales_from_previous_tirthy", tooltip="Vendas dos Últimos Trinta Dias", on_click=self.filter_buttons_clicked)
        self.btn_filter_all = IconButton(icon=icons.APPS_ROUNDED, selected_icon=icons.APPS_ROUNDED, selected_icon_color=colors.PRIMARY, tooltip="Mostrar Todas as Vendas", data="select_all_sales", on_click=self.filter_buttons_clicked)
        self.row_sales = Row(wrap=False, scroll="auto", expand=True, spacing=25)
        
        self.tf_id_sale = TextField(border="none", expand=3, label="Pedido nº:", value="Automático", text_size=16, read_only=True, text_style=TextStyle(weight=FontWeight.BOLD))
        self.tf_customer = TextField(border="none", expand=9, label="Cliente:", value="ALEXANDER GRAHAN BELL DA SILVA SAURO", multiline=True, text_size=16, read_only=True, text_style=TextStyle(weight=FontWeight.BOLD))
        self.tf_CPF = TextField(border="none", expand=4, label="CPF:", value="92.791.243/0001-03", text_size=16, read_only=True, text_style=TextStyle(weight=FontWeight.BOLD))
        self.tf_date = TextField(border="none", expand=3, label="Data:", value="20/02/2020", text_size=16, read_only=True, text_style=TextStyle(weight=FontWeight.BOLD))
        self.tf_total_sale = TextField(border="none", expand=3, label="Total:", value="1.000.000,00", text_size=16, prefix_text="R$", read_only=True, text_style=TextStyle(weight=FontWeight.BOLD))
        self.btn_print = IconButton(icon=icons.PICTURE_AS_PDF_OUTLINED, tooltip="Gerar arquivo .pdf", icon_color="primary", on_click=self.pdf_clicked)
        self.dt_products_sold = DataTable(                                            
            expand=True,
            column_spacing=5,
            divider_thickness=0.4,
            #heading_row_color=colors.ON_INVERSE_SURFACE,
            border_radius=border_radius.all(5),
            columns=[
                DataColumn(Text('ID')), 
                DataColumn(Text('CÓD. PR.')), 
                DataColumn(Text('DESCRIÇÃO')), 
                DataColumn(Text('MARCA')),
                DataColumn(Text('QUANT.')),
                DataColumn(Text('V. UNIT.')),
                DataColumn(Text('CUSTO')),
                DataColumn(Text('V. TOTAL')),
            ],
        )

    def build(self):
        page_content = Container(
            #bgcolor='red',
            padding=5,
            border_radius=5,
            expand=True,
            content=Column(
                expand=True,
                controls=[
                    Row(
                        height=250,
                        spacing=0,
                        controls=[
                            Card(
                                expand=True,
                                surface_tint_color=colors.INVERSE_PRIMARY,
                                elevation = 1.5,
                                content=Container(
                                    padding=padding.all(10),
                                    content=Column(
                                        expand=True,
                                        controls=[
                                            Row(
                                                spacing=20,
                                                controls=[
                                                    Row(
                                                        spacing=5,
                                                        controls=[
                                                            self.btn_filter_today,
                                                            self.btn_filter_previous_seven,
                                                            self.btn_filter_previous_thirty,
                                                            self.btn_filter_all,
                                                        ]
                                                    ),
                                                    self.tf_find_sale,
                                                    self.btn_new_sale,
                                                ]
                                            ),
                                            self.row_sales,
                                        ]
                                    )
                                )
                            )
                        ]
                    ),
                    Row(
                        expand=True,
                        controls=[
                            Card(
                                expand=True,
                                surface_tint_color=colors.INVERSE_PRIMARY,
                                elevation = 1.5,
                                content=Column(
                                    spacing=0,
                                    expand=True,
                                    controls=[
                                        Container(
                                            padding=padding.only(left=10, right=10),
                                            border=border.only(bottom=border.BorderSide(1, colors.OUTLINE_VARIANT)),
                                            content=Row(
                                                controls=[
                                                    self.tf_id_sale,
                                                    self.tf_customer,
                                                    self.tf_CPF,
                                                    self.tf_date,
                                                    self.tf_total_sale,
                                                    self.btn_print,
                                                ]
                                            ),
                                        ),
                                        Container(
                                            expand=True,
                                            padding=padding.all(10),
                                            content=ListView(
                                                expand=True,
                                                controls=[
                                                    self.dt_products_sold,
                                                ]
                                            )
                                        ),

                                        
                                    ]
                                )
                            )
                        ]
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
    
    def initialize(self):
        print("Initializing Sales Page")
        self.tf_id_sale.value = ""
        self.tf_customer.value = ""
        self.tf_CPF.value = ""
        self.tf_date.value = ""
        self.tf_total_sale.value = ""
        self.tf_find_sale.value = ""
        self.btn_print.disabled = True
        self.dt_products_sold.rows.clear()
        self.update()
        self.fill_in_table_sales()
    
    def new_sale_clicked(self, _):
        self.route.page.go("/register_sales")
        self.route.bar.set_title("Nova Venda")
        self.route.page.update()

    def get_sales_by_date(self, func_name):
        mydb = SalesDatabase(self.route)
        mydb.connect()
        func = getattr(mydb, func_name)
        result = func()
        mydb.close()
        return result

    def fill_in_table_sales(self, data=None):
        if data is None:
            for control in [self.btn_filter_today, self.btn_filter_previous_seven,
                            self.btn_filter_previous_thirty, self.btn_filter_all]:
                if control.selected:
                    func = control.data
            fulldata = self.get_sales_by_date(func)
        else:
            fulldata = data
        
        if fulldata is None:
            Notification(self.page, "Erro ao carregar tabela de vendas. Reinicie o sistema.", "red").show_message()
            return

        self.row_sales.controls.clear()
        for data in fulldata:
            self.row_sales.controls.append(
                Card(
                    width=450,
                    height=120,
                    elevation=4,
                    content=Container(
                        padding=10,
                        content=Column(
                            expand=True,
                            alignment=MainAxisAlignment.SPACE_BETWEEN,
                            horizontal_alignment=CrossAxisAlignment.START,
                            controls=[
                                Row(
                                    spacing=5,
                                    alignment="center",
                                    controls=[
                                        IconButton(data=data[0], icon=icons.EDIT_OUTLINED,icon_color=colors.PRIMARY, tooltip="Editar Venda", scale=0.9, on_click=self.edit_sale_clicked),
                                        Text(f"Pedido n. {data[0]}", weight=FontWeight.BOLD, data=data[0]),
                                        IconButton(data=data[0], icon=icons.DELETE_OUTLINED, icon_color=colors.ERROR, tooltip="Excluir Venda", scale=0.9, on_click=self.delete_clicked),
                                    ],
                                ),
                                Divider(height=1, color=colors.PRIMARY, opacity=0.5),
                                Row(
                                    spacing=15,
                                    alignment="start",
                                    controls=[
                                        Text(f"Data: {data[2]}"),
                                        Text(f"Total: R${Validator.format_to_currency(data[3])}"),
                                        Text(f"CPF: {data[5]}"),
                                    ]
                                ),
                                Text(f"Cliente: {data[4]}", text_align=TextAlign.CENTER),    
                            ]
                        ),
                        ink=True,
                        on_click=lambda e: self.select_sale_clicked(e.control.content.controls[0].controls[1].data),
                    )
                ),
            )
            self.tf_find_sale.focus()
            self.row_sales.update()

    def get_one_sale_from_db(self, id_sale):
        mydb = SalesDatabase(self.route)
        mydb.connect()
        result = mydb.select_one_sale(id_sale)
        mydb.close()
        return result

    def get_all_sold_from_db(self, id_sale):
        mydb = SalesDatabase(self.route)
        mydb.connect()
        result = mydb.select_all_sold(id_sale)
        mydb.close()
        return result

    def fill_in_sale_panel(self, data):
        self.tf_id_sale.value = str(data[0])
        self.tf_customer.value = data[4]
        self.tf_CPF.value = data[5]
        self.tf_date.value = data[2]
        self.tf_total_sale.value = Validator.format_to_currency(data[3])
        self.route.page.update()

    def fill_in_table_solds(self, fulldata):
        self.dt_products_sold.rows.clear()
        for data in fulldata:
            self.dt_products_sold.rows.append(
                DataRow(
                    cells=[
                        DataCell(Text(str(data[0]))), # id_product_sold
                        DataCell(Text(str(data[1]))), # id_product
                        DataCell(Text(data[2])), # description of product
                        DataCell(Text(data[3])), # brand
                        DataCell(Text(str(data[4]))), #quantity
                        DataCell(TextField(border="none", prefix_text="R$", value=Validator.format_to_currency(data[5]), read_only=True)), # unit price
                        DataCell(TextField(border="none", prefix_text="R$", value=Validator.format_to_currency(data[6]), read_only=True)), # cost
                        DataCell(TextField(border="none", prefix_text="R$", value=Validator.format_to_currency(data[7]), read_only=True)), # total
                    ]
                )
            )
        self.dt_products_sold.update()

    def select_sale_clicked(self, idsale):
        with contextlib.suppress(Exception):
            data_sale = self.get_one_sale_from_db(idsale) 
            data_sold_products = self.get_all_sold_from_db(idsale)
            if data_sale and data_sold_products:
                self.fill_in_sale_panel(data_sale)
                self.fill_in_table_solds(data_sold_products)
                self.btn_print.disabled = False
            else:
                Notification(self.page, "Erro ao carregar venda. Reinicie o sistema!", "red").show_message()
                self.btn_print.disabled = True
            self.update()

    def edit_sale_clicked(self, e):
        self.route.page.go("/register_sales")
        self.route.bar.set_title("Editar Venda")
        self.route.page.update()

        self.route.register_sales.sale_list_to_register = list(self.get_one_sale_from_db(e.control.data))
        self.route.register_sales.products_in_table = self.get_all_sold_from_db(e.control.data)
        self.route.register_sales.load_data_for_update()

    def delete_clicked(self, e):
        dialog = ConfirmDialog(self.delete_sale, "Por favor, confirme:", "Tem certeza que deseja apagar a venda? As informações não poderão ser recuperadas!")
        dialog.data = e.control.data
        self.route.page.dialog = dialog
        dialog.open = True
        self.route.page.update()
    
    def delete_sale(self, id_sale):        
        mydb = SalesDatabase(self.route)
        mydb.connect()
        result_to_update_stock = mydb.select_all_sold(id_sale)
        result = mydb.delete_products_sold(id_sale)

        if result == "success":
            final_result = mydb.delete_sale(id_sale)
            mydb.close()
        else:
            Notification(self.page, f"Erro ao ecluir a venda (exclusão de produtos vendidos): {result}", "red").show_message()
            mydb.close()
            return

        if final_result == "success":
            Notification(self.page, "Venda excluída com sucesso!", "green").show_message()
            self.initialize()
        else:
            Notification(self.page, f"Erro ao ecluir a venda: {result}", "red").show_message()
            return

        dialog = ConfirmDialog(self.update_stock, "Deseja retornar os produtos ao estoque?", "Em caso positivo, os produtos desta venda serão novamente adicionados ao estoque.")
        dialog.data = result_to_update_stock
        self.route.page.dialog = dialog
        dialog.open = True
        self.route.page.update()

        self.initialize()

    def find_sale(self, _):
        if self.tf_find_sale.value == "":
            self.fill_in_table_sales()
            return
        mydb = SalesDatabase(self.route)
        mydb.connect()
        result = mydb.find_sale(self.tf_find_sale.value)
        mydb.close()

        self.fill_in_table_sales(result)

    def update_stock(self, data_to_update):
        mydb = ProductsDatabase(self.route)
        mydb.connect()
        result = []
        for temp_data in data_to_update:
            result.append(mydb.update_stock([temp_data[1], temp_data[4]]))
        mydb.close()
        if len(result) == len(data_to_update):
            Notification(self.page, f"Sucesso! {len(result)} produto(s) com estoque atualizado!", "green").show_message()
        else:
            Notification(self.page, f"Não foi possível atualizar o estoque. Erro: {result[-1]}", "red").show_message()

    def get_products_data(self):
        data = []
        for row in range(len(self.dt_products_sold.rows)):
            text = []
            for col in range(len(self.dt_products_sold.columns)):
                text.append(self.dt_products_sold.rows[row].cells[col].content.value) if col not in [6, 0] else None
            data.append(text)
        return data
    
    def get_header_data(self):
        return ["EMPRESA TESTE ABC", "Rua do Abecedário, 1000, Vila das Letras, Letrario/SP", "(99) 99999 9999", "letras@abc.com"]
    
    def get_sale_data(self):
        return [self.tf_id_sale.value, self.tf_date.value]
    
    def get_customer_data(self):
        mydb = CustomerDatabase(self.route)
        mydb.connect()
        result_data = mydb.select_one_customer(self.tf_CPF.value)
        result_adress = mydb.select_adresses(self.tf_CPF.value)
        mydb.close()
        
        tel, email = result_data[0][3], result_data[0][4]
        if len(result_adress) > 0:
            adress = f"{result_adress[0][0]}, {result_adress[0][1]}/{result_adress[0][2]} - CEP {result_adress[0][3]}"
        else:
            adress = "Endereço: N/C"

        return [self.tf_customer.value, self.tf_CPF.value, tel, email, adress]

    def create_report_sales(self, e: FilePickerResultEvent):
        if e.path is None:
            return
        filename = f"{e.path}.{e.control.allowed_extensions[0]}"
        header_data = self.get_header_data()
        sale_data = self.get_sale_data()
        customer_data = self.get_customer_data()
        products_data = self.get_products_data()
        total = 0.0
        for value in products_data:
            total += Validator.format_to_float(value[5])
        products_data.append(["", "", "", "", "Total:", Validator.format_to_currency(total)])
        
        report = SaleReport(filename, header_data, sale_data, customer_data, products_data)
        result, error = report.create_pdf()
        if result == "success":
            Notification(self.route.page, f"Arquivo gerado com sucesso: {filename}", "green").show_message()
        else:
            Notification(self.route.page, f"Erro ao gerar o arquivo {filename}: {error}", "red").show_message()

    def pdf_clicked(self, e):
        self.route.save_file_dialog.on_result = self.create_report_sales
        self.route.save_file_dialog.save_file(dialog_title="Salvar como ...", allowed_extensions=["pdf"])
        self.update()

    def filter_buttons_clicked(self, e):
        buttons = [self.btn_filter_today, self.btn_filter_previous_seven,
                  self.btn_filter_previous_thirty, self.btn_filter_all]
        for control in buttons:
            control.selected = False
        e.control.selected = True
        e.control.update()
        
        mydb = SalesDatabase(self.route)
        mydb.connect()
        result = self.get_sales_by_date(e.control.data)
        mydb.close()
        self.fill_in_table_sales(result)
        self.tf_find_sale.value = ""
        self.update()
        
