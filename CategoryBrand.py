from flet import (
    DataTable, TextButton, TextField, IconButton, Text, Row, 
    Column, ListView, MainAxisAlignment, AlertDialog, DataColumn,
    DataRow, DataCell, SnackBar, icons, colors
)
from Database import ProductsDatabase

class Category(AlertDialog):
    def __init__(self, products):
        super().__init__()
        self.products = products
        self.modal = True
        self.title=Row(expand=True, controls=[Text("Gerenciar Categorias:", width=400)])

        self.tf_new_category = TextField(label="Insira a nova categoria", dense=True, expand=True)
        self.btn_save = IconButton(icon=icons.SAVE_OUTLINED, icon_color=colors.PRIMARY, icon_size=32, on_click=self.register_category)
        self.btn_back = TextButton(text="Voltar", on_click=self.back_clicked)
        self.dt_category = DataTable(
            expand=True,
            columns=[
                DataColumn(Text('ID')), 
                DataColumn(Text('CATEGORIAS')), 
                DataColumn(Text('EXCLUIR')), 
            ],
        )

        self.actions=[
                Column(
                    width=400,
                    expand=True,
                    controls=[
                        Row(
                            controls=[
                                self.tf_new_category,
                                self.btn_save,
                            ]
                        ),
                        ListView(
                            height=240,
                            controls=[
                                self.dt_category,
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
    
    def build(self):
        return self

    def back_clicked(self, e):
        self.products.load_categories()
        self.open = False
        self.update()

    def load_category(self):
        mydb = ProductsDatabase(self.products.route)
        mydb.connect()
        result = mydb.select_category()
        mydb.close()

        self.dt_category.rows.clear()
        for data in result:
            self.dt_category.rows.append(
                DataRow(
                    cells=[
                        DataCell(Text(str(data[0]))),
                        DataCell(Text(data[1])),
                        DataCell(Row([IconButton(icon=icons.DELETE_OUTLINED, icon_color='red', data=data[0], on_click=self.delete_category)])),
                    ]
                )
            )
        self.dt_category.update()

    def register_category(self, e):
        if self.tf_new_category.value.strip() == "":
            return
        mydb = ProductsDatabase(self.products.route)
        mydb.connect()
        result = mydb.register_category(self.tf_new_category.value)
        mydb.close()

        if result == 'success':
            self.page.snack_bar = SnackBar(content=Text("Categoria registrada com sucesso!", color='green'))
        else:
            self.page.snack_bar = SnackBar(content=Text(f"Erro ao registrar a categoria: {result}", color='red'))
        self.page.snack_bar.open = True
        
        self.load_category()

        self.tf_new_category.value = ""
        self.page.update()

    def delete_category(self, e):
        mydb = ProductsDatabase(self.products.route)
        mydb.connect()
        result = mydb.delete_category(e.control.data)
        mydb.close()

        if result == 'success':
            self.page.snack_bar = SnackBar(content=Text("Categoria deletada com sucesso!", color='green'))
        else:
            self.page.snack_bar = SnackBar(content=Text(f"Erro ao deletar a categoria: {result}", color='red'))
        self.page.snack_bar.open = True
        
        self.load_category()
        self.page.update()

class Brand(AlertDialog):
    def __init__(self, products):
        super().__init__()
        self.products = products
        self.modal = True
        self.title=Row(expand=True, controls=[Text("Gerenciar Marcas:", width=400)])

        self.tf_new_brand = TextField(label="Insira a nova marca", dense=True, expand=True)
        self.btn_save = IconButton(icon=icons.SAVE_OUTLINED, icon_color=colors.PRIMARY, icon_size=32, on_click=self.register_brand)
        self.btn_back = TextButton(text="Voltar", on_click=self.back_clicked)
        self.dt_brand = DataTable(
            expand=True,
            columns=[
                DataColumn(Text('ID')), 
                DataColumn(Text('MARCAS')), 
                DataColumn(Text('EXCLUIR')), 
            ],
        )

        self.actions=[
                Column(
                    width=400,
                    expand=True,
                    controls=[
                        Row(
                            controls=[
                                self.tf_new_brand,
                                self.btn_save,
                            ]
                        ),
                        ListView(
                            height=240,
                            controls=[
                                self.dt_brand,
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
    
    def build(self):
        return self

    def back_clicked(self, e):
        self.products.load_brands()
        self.open = False
        self.update()

    def load_brand(self):
        mydb = ProductsDatabase(self.products.route)
        mydb.connect()
        result = mydb.select_brand()
        mydb.close()

        self.dt_brand.rows.clear()
        for data in result:
            self.dt_brand.rows.append(
                DataRow(
                    cells=[
                        DataCell(Text(str(data[0]))),
                        DataCell(Text(data[1])),
                        DataCell(Row([IconButton(icon=icons.DELETE_OUTLINED, icon_color='red', data=data[0], on_click=self.delete_brand)])),
                    ]
                )
            )
        self.dt_brand.update()

    def register_brand(self, e):
        if self.tf_new_brand.value.strip() == "":
            return
        mydb = ProductsDatabase(self.products.route)
        mydb.connect()
        result = mydb.register_brand(self.tf_new_brand.value)
        mydb.close()

        if result == 'success':
            self.page.snack_bar = SnackBar(content=Text("Marca registrada com sucesso!", color='green'))
        else:
            self.page.snack_bar = SnackBar(content=Text(f"Erro ao registrar a marca: {result}", color='red'))
        self.page.snack_bar.open = True
        
        self.load_brand()

        self.tf_new_brand.value = ""
        self.page.update()

    def delete_brand(self, e):
        mydb = ProductsDatabase(self.products.route)
        mydb.connect()
        result = mydb.delete_brand(e.control.data)
        mydb.close()

        if result == 'success':
            self.page.snack_bar = SnackBar(content=Text("Marca deletada com sucesso!", color='green'))
        else:
            self.page.snack_bar = SnackBar(content=Text(f"Erro ao deletar a marca: {result}", color='red'))
        self.page.snack_bar.open = True
        
        self.load_brand()
        self.page.update()
