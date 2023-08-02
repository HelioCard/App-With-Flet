from flet import (Row, MainAxisAlignment, TextField, TextButton, Column, Text, DataColumn, DataTable,
                  DataCell, ListView, AlertDialog, DataRow, IconButton, colors, icons)
from Database import ProductsDatabase

class SelectProduct(AlertDialog):
    def __init__(self, route):
        super().__init__()
        self.route = route
        self.modal = True
        self.title=Row(alignment=MainAxisAlignment.CENTER, controls=[Text("Lista de Produtos:", width=840)])

        self.tf_find_product = TextField(label="Buscar", width=840, on_change=self.find_product)
        self.dt_products = DataTable(
            expand=True,
            columns=[
                DataColumn(label=Text("ID")),
                DataColumn(label=Text("DESCRIÇÃO")),
                DataColumn(label=Text("MARCA")),
                DataColumn(label=Text("PREÇO")),
                DataColumn(label=Text("SELECIONAR")),
            ]
        )
        self.btn_back = TextButton(text="Voltar", on_click=self.back_clicked)

        self.actions=[
            Column(
                width=840,
                controls=[
                    self.tf_find_product,
                    ListView(
                        height=400,
                        controls=[
                            self.dt_products,
                        ]
                    ),
                    Row(alignment=MainAxisAlignment.END, width=840, controls=[self.btn_back]),
                ]
            )
        ]
        self.initialize()

    def build(self):
        return self

    def back_clicked(self, e):
        self.open = False
        self.route.page.update()

    def get_data_from_db(self):
        mydb = ProductsDatabase(self.route)
        mydb.connect()
        result = mydb.select_products()
        mydb.close()
        return result
    
    def fill_in_table_products(self, fulldata):
        self.dt_products.rows.clear()
        for data in fulldata:
            self.dt_products.rows.append(
                DataRow(
                    cells=[
                        DataCell(Text(value=data[0])),
                        DataCell(Text(value=data[1])),
                        DataCell(Text(value=data[3])),
                        DataCell(Text(value=f"R${data[4]}")),
                        DataCell(IconButton(icon=icons.SENSOR_OCCUPIED_ROUNDED, icon_color=colors.PRIMARY, tooltip="Selecionar", data=data[0], on_click=self.select_product)),
                    ]
                )
            )

    def initialize(self):
        fulldata = self.get_data_from_db()
        self.fill_in_table_products(fulldata)

    def find_product(self, e):
        if self.tf_find_product.value == "":
            self.initialize()
            return
        
        mydb = ProductsDatabase(self.route)
        mydb.connect()
        result = mydb.find_product(self.tf_find_product.value)
        mydb.close()

        if result:
            self.fill_in_table_products(result)
        else:
            self.dt_products.rows.clear()

        self.route.page.update()

    def select_product(self, e):
        mydb = ProductsDatabase(self.route)
        mydb.connect()
        result = mydb.find_product_by_code(int(e.control.data))
        mydb.close()
        
        if result:
            self.route.register_sales.load_card(result)
            self.open = False
            self.update()
        else:
            self.route.register_sales.clear_card()
        
        self.route.register_sales.validate_fields(e)
