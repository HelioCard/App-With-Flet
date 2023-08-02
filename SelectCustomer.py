from flet import (
    DataTable, TextButton, TextField, IconButton, Text, Row, 
    Column, ListView, MainAxisAlignment, AlertDialog, DataColumn,
    DataRow, DataCell, icons,
)
from Database import CustomerDatabase

import asyncio

class SelectCustomer(AlertDialog):
    def __init__(self, route):
        super().__init__()
        self.route = route
        self.modal = True
        self.title=Row(expand=True, controls=[Text("Selecione o Cliente:", width=600)])

        self.tf_find_customer = TextField(label="Buscar...", expand=True, prefix_icon=icons.SEARCH_OUTLINED, on_change=self.find_customer)
        self.btn_back = TextButton(text="Voltar", on_click=self.back_clicked)
        self.dt_customer = DataTable(
            expand=True,
            columns=[
                DataColumn(Text('ID')), 
                DataColumn(Text('CLIENTE')), 
                DataColumn(Text('CPF')), 
                DataColumn(Text('SELEC.')), 
            ],
        )

        self.actions=[
                Column(
                    width=600,
                    expand=True,
                    controls=[
                        Row(
                            controls=[
                                self.tf_find_customer,
                            ]
                        ),
                        ListView(
                            height=240,
                            controls=[
                                self.dt_customer,
                            ]
                        ),
                        Row(
                            alignment=MainAxisAlignment.END,
                            controls=[
                                self.btn_back,
                            ]
                        )
                    ]
                )
            ]
        self.load_table(self.get_customer_data())
    
    def build(self):
        return self

    def back_clicked(self, e):
        self.data = "back"
        self.open = False
        self.update()

    def get_customer_data(self):
        mydb = CustomerDatabase(self.route)
        mydb.connect()
        result = mydb.select_customers()
        mydb.close()
        return result

    def load_table(self, fulldata):
        self.dt_customer.rows.clear()
        for data in fulldata:
            self.dt_customer.rows.append(
                DataRow(
                    cells=[
                        DataCell(Text(str(data[0]))),
                        DataCell(Text(data[1])),
                        DataCell(Text(data[2])),
                        DataCell(Row([IconButton(icon=icons.SENSOR_OCCUPIED_OUTLINED, icon_color="blue", data=data, tooltip="Selecionar", on_click=self.select_customer)])),
                    ]
                )
            )

    def find_customer(self, e):
        if self.tf_find_customer.value == "":
            self.load_table(self.get_customer_data())
            self.update()
            return
        
        mydb = CustomerDatabase(self.route)
        mydb.connect()
        result = mydb.find_customer(self.tf_find_customer.value)
        mydb.close()
        if result:
            self.load_table(result)
        self.update()

    def select_customer(self, e):
        self.data = e.control.data
        self.open = False
        self.update()

    async def verify_data(self):
        while self.data is None:
            await asyncio.sleep(0.5)

