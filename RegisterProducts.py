from flet import (UserControl, Row, Column, Container, Text, TextField, IconButton, DataTable, Dropdown,OutlinedButton, 
                  DataRow, DataColumn, DataCell, icons, colors, TextThemeStyle, TextAlign, CrossAxisAlignment,
                  VerticalDivider, ListView, MainAxisAlignment, dropdown)

from Notification import Notification
from CategoryBrand import Category, Brand
from Database import ProductsDatabase, SalesDatabase
from Validator import Validator

class RegisterProducts(UserControl):
    def __init__(self, route):
        super().__init__()
        self.route = route

        self.text_label = Text(value="Novo Produto:", style=TextThemeStyle.TITLE_LARGE)
        self.tf_id = TextField(label="ID (Aut)", read_only=True, dense=True, expand=1, text_size=24)
        self.tf_descr = TextField(label="Descrição", expand=4, text_size=24, dense=True, on_change=self.analyze_fields)
        self.dp_category = Dropdown(label="Categoria", expand=2, on_change=self.analyze_fields)
        self.btn_manage_categories = IconButton(icon=icons.ADD_CIRCLE_OUTLINE, icon_color=colors.PRIMARY, icon_size=32, on_click=self.manage_categories_clicked)
        self.dp_brand = Dropdown(label="Marca", expand=2, on_change=self.analyze_fields)
        self.btn_manage_brands = IconButton(icon=icons.ADD_CIRCLE_OUTLINE, icon_color=colors.PRIMARY, icon_size=32, on_click=self.manage_brands_clicked)
        self.tf_stock = TextField(label="Estoque", expand=1, text_align=TextAlign.CENTER, on_change=self.analyze_fields)
        self.tf_min_stock = TextField(label="Est. Mínimo", expand=1, text_align=TextAlign.CENTER, on_change=self.analyze_fields)
        self.tf_max_stock = TextField(label="Est. Máximo", expand=1, text_align=TextAlign.CENTER, on_change=self.analyze_fields)
        self.tf_observ = TextField(label="Observação", expand=3, on_change=self.analyze_fields)
        self.tf_costs = TextField(label="Custo", expand=2, prefix_text="R$", text_size=24, dense=True,  on_change=self.analyze_fields, on_blur=self.calc_margin)
        self.tf_selling_price = TextField(label="Preço de Venda", expand=2, prefix_text="R$", text_size=24, dense=True,  on_change=self.analyze_fields, on_blur=self.calc_margin)
        self.tf_margin = TextField(label="Margem", expand=1, suffix_text="%", text_align=TextAlign.RIGHT, text_size=24, dense=True,  on_change=self.analyze_fields, on_blur=self.calc_selling_price)
        self.btn_add_save_products = OutlinedButton(text='Salvar', icon=icons.SAVE_OUTLINED, on_click=self.add_save_clicked)
        self.btn_back = IconButton(tooltip='Voltar para "Produtos"', icon=icons.ARROW_BACK_OUTLINED, icon_size=32, on_click=self.back_clicked)

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

        self.text_total = Text(value="R$ 350,00", style=TextThemeStyle.TITLE_MEDIUM)

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
                                        expand=True,
                                        
                                        horizontal_alignment=CrossAxisAlignment.CENTER,
                                        controls=[
                                            Row(
                                                controls=[
                                                    self.text_label,
                                                    Row(expand=True), #spacer
                                                    self.btn_back,
                                                ]
                                            ),
                                            Row(
                                                controls=[
                                                    self.tf_id,
                                                    self.tf_descr,
                                                ]
                                            ),
                                            Row(
                                                controls=[
                                                    self.dp_category,
                                                    self.btn_manage_categories,
                                                    Column(),
                                                    self.dp_brand,
                                                    self.btn_manage_brands,
                                                ]
                                            ),
                                            Row(
                                                controls=[
                                                    Text(value="Estoque:", style=TextThemeStyle.TITLE_LARGE),
                                                ]
                                            ),
                                            Row(
                                                controls=[
                                                    self.tf_stock,
                                                    self.tf_min_stock,
                                                    self.tf_max_stock,
                                                    self.tf_observ,
                                                ]
                                            ),
                                            Row(
                                                controls=[
                                                    Text(value="Preços:", style=TextThemeStyle.TITLE_LARGE),
                                                ]
                                            ),
                                            Row(
                                                controls=[
                                                    self.tf_costs,
                                                    self.tf_selling_price,
                                                    self.tf_margin,
                                                ]
                                            ),
                                            Column(expand=True),
                                            Row(
                                                alignment=MainAxisAlignment.END,
                                                controls=[
                                                    self.btn_add_save_products,
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
                                            Text(value="Histórico de Vendas", style=TextThemeStyle.TITLE_MEDIUM),
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
    
    def initialize(self):
        print("Initializing Register Products Page")
        self.load_categories()
        self.load_brands()
        self.clear_fields()
        self.text_label.value = "Novo Produto:"
        self.update()

    def back_clicked(self, e):
        self.route.page.go("/products")
        self.route.bar.set_title("Produtos")
        self.route.page.update()

    def manage_categories_clicked(self, e):
        dialog = Category(self)
        self.route.page.dialog = dialog
        dialog.open = True
        self.route.page.update()
        dialog.load_category()
    
    def manage_brands_clicked(self, e):
        dialog = Brand(self)
        self.route.page.dialog = dialog
        dialog.open = True
        self.route.page.update()
        dialog.load_brand()

    def load_categories(self):
        mydb = ProductsDatabase(self.route)
        mydb.connect()
        result = mydb.select_category()
        mydb.close()

        self.dp_category.options.clear()
        for data in result:
            self.dp_category.options.append(dropdown.Option(data[1]))
        self.dp_category.update()

    def load_brands(self):
        mydb = ProductsDatabase(self.route)
        mydb.connect()
        result = mydb.select_brand()
        mydb.close()
        
        self.dp_brand.options.clear()
        for data in result:
            self.dp_brand.options.append(dropdown.Option(data[1]))
        self.dp_brand.update()
    
    def validate_int_fields(self, e):
        fields = [self.tf_stock, self.tf_min_stock, self.tf_max_stock]
        for control in fields:
            if control.value != "":
                value = Validator.format_to_int(control.value)
                if value is not None and value >= 0:
                    control.error_text = ""    
                else:
                    control.error_text = "Valor inválido!"
                    self.btn_add_save_products.disabled = True         
        self.update()

    def validate_float_fields(self, e):
        fields = [self.tf_costs, self.tf_margin, self.tf_selling_price]
        for control in fields:
            if control.value != "":
                value = Validator.format_to_float(control.value)
                if value is not None and value >= 0:
                    control.error_text = ""    
                else:
                    control.error_text = "Valor inválido!"
                    self.btn_add_save_products.disabled = True         
        self.update()

    def calc_margin(self, e):
        cost = Validator.format_to_float(self.tf_costs.value)
        selling_price = Validator.format_to_float(self.tf_selling_price.value)

        if not all(isinstance(value, float) for value in [cost, selling_price]):
            return

        if cost != 0:
            margin = (selling_price - cost) / cost * 100
        else:
            margin = 100
        self.tf_costs.value = Validator.format_to_currency(cost)
        self.tf_selling_price.value = Validator.format_to_currency(selling_price)
        self.tf_margin.value = Validator.format_to_currency(margin)
        self.tf_margin.update()
        self.analyze_fields(e)

    def calc_selling_price(self, e):
        cost = Validator.format_to_float(self.tf_costs.value)
        margin = Validator.format_to_float(self.tf_margin.value)

        if not all(isinstance(value, float) for value in [cost, margin]):
            return

        if cost != 0:
            selling_price = margin / 100 * cost + cost
        else:
            Notification(self.route.page, "Não é possível calcular o preço de venda com base na margem, pois o custo é R$0,00!", "red").show_message()
            return

        self.tf_costs.value = Validator.format_to_currency(cost)
        self.tf_margin.value = Validator.format_to_currency(margin)
        self.tf_selling_price.value = Validator.format_to_currency(selling_price)
        self.tf_selling_price.update()
        
        self.analyze_fields(e)

    def clear_fields(self):
        for control in [self.tf_id, self.tf_descr, 
                        self.tf_stock, self.tf_min_stock,
                        self.tf_max_stock, self.tf_observ, self.tf_costs,
                        self.tf_selling_price, self.tf_margin]:
            control.value = ""
            control.error_text = ""
        self.dp_category.value = ""
        self.dp_brand.value = ""
        self.dt_order_history.rows.clear()
        self.text_total.value = ""
        self.btn_add_save_products.disabled = True
        self.tf_descr.focus()
        self.update()

    def analyze_fields(self, e):
        
        required_fields = [
            self.tf_descr, self.dp_category, self.dp_brand, self.tf_stock, self.tf_min_stock,
            self.tf_max_stock, self.tf_costs, self.tf_selling_price,
            self.tf_margin
        ]

        all_fields_filled = all(control.value != "" for control in required_fields)
        all_fields_empty = all(control.value == "" or None for control in required_fields)

        for control in required_fields:
            control.error_text = "" if control.value != "" else "Campo obrigatório"

        if all_fields_empty:
            for control in required_fields:
                control.error_text = ""

        self.btn_add_save_products.disabled = not all_fields_filled
        self.validate_int_fields(e)
        self.validate_float_fields(e)
        self.update()

    def load_product(self, id):
        mydb = ProductsDatabase(self.route)
        mydb.connect()
        result = mydb.select_products_full(id)
        mydb.close()

        for index, control in enumerate([self.tf_id, self.tf_descr, self.dp_category, self.dp_brand,
                        self.tf_stock, self.tf_min_stock, self.tf_max_stock, self.tf_observ,
                        self.tf_costs, self.tf_selling_price, self.tf_margin]):
            control.value = result[index]
            if index in [8, 9, 10]:
                control.value = Validator.format_to_currency(float(control.value))
        self.update()

    def add_save_clicked(self, e):
        if self.tf_id.value == "":
            self.register_product(e)
        else:
            self.update_product(e)

    def register_product(self, e):
        fulldataset = [
            self.tf_descr.value.upper(),
            self.dp_category.value,
            self.dp_brand.value,
            int(self.tf_stock.value),
            int(self.tf_min_stock.value),
            int(self.tf_max_stock.value),
            self.tf_observ.value,
            Validator.format_to_float(self.tf_costs.value),
            Validator.format_to_float(self.tf_selling_price.value),
            Validator.format_to_float(self.tf_margin.value),
        ]
        
        mydb = ProductsDatabase(self.route)
        mydb.connect()
        result = mydb.register_products(fulldataset)
        mydb.close()

        if result == "success":
            Notification(self.page, "Produto registrado com sucesso", "green").show_message()
        else:
            Notification(self.page, f"Erro ao atualizar o produto: {result}", "red").show_message()
        
        self.clear_fields()

    def update_product(self, e):
        fulldataset = [
            int(self.tf_id.value),
            self.tf_descr.value.upper(),
            self.dp_category.value,
            self.dp_brand.value,
            int(self.tf_stock.value),
            int(self.tf_min_stock.value),
            int(self.tf_max_stock.value),
            self.tf_observ.value,
            Validator.format_to_float(self.tf_costs.value),
            Validator.format_to_float(self.tf_selling_price.value),
            Validator.format_to_float(self.tf_margin.value),
        ]
        
        mydb = ProductsDatabase(self.route)
        mydb.connect()
        result = mydb.update_products(fulldataset)
        mydb.close()

        if result == "success":
            Notification(self.page, "Produto atualizado com sucesso", "green").show_message()
        else:
            Notification(self.page, f"Erro ao atualizar o produto: {result}", "red").show_message()

        self.back_clicked(e)

    def get_sold_from_db(self):
        mydb = SalesDatabase(self.route)
        mydb.connect()
        result = mydb.select_sold_history(self.tf_id.value)
        mydb.close()

        total = sum(map(lambda x: x[2], result))
        self.text_total.value = f"R${Validator.format_to_currency(total)}"
        self.update()
        self.fill_in_history_table(result)

    def fill_in_history_table(self, fulldata):
        self.dt_order_history.rows.clear()
        for data in fulldata:
            self.dt_order_history.rows.append(
                DataRow(
                    cells=[
                        DataCell(Text(data[0])),
                        DataCell(Text(data[1])),
                        DataCell(Text(value=f"R${Validator.format_to_currency(data[2])}")),
                        DataCell(IconButton(icon=icons.VISIBILITY_OUTLINED, icon_color="blue", tooltip="Ver pedido", data=data[0], on_click=self.see_sale_clicked)),
                    ]
                )
            )
        self.dt_order_history.update()

    def see_sale_clicked(self, e):
        self.route.page.go("/sales")
        self.route.bar.set_title("Vendas")
        self.route.menu.nnrail.selected_index = 4
        self.route.menu.update()
        self.route.page.update()

        self.route.sales.select_sale_clicked(e.control.data)
