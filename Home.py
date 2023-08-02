
from flet import (UserControl, Row, Column, Container, Text, border, colors, margin, ChartAxisLabel, Card, alignment, 
                  border_radius, LineChartDataPoint, LineChartData, Border, ChartGridLines, icons, 
                  ChartAxis, LineChart, BorderSide, TextThemeStyle, BarChartGroup, BarChart, BarChartRod, Icon,
                  TextSpan, PieChart, PieChartSection, TextStyle, FontWeight, PieChartEvent,
                  BoxShadow, LineChartEvent, Offset, ShadowBlurStyle, BarChartEvent, OutlinedButton)
from datetime import date, timedelta

from Database import DashboardDatabase
from Validator import Validator

class Home(UserControl):
    def __init__(self, route):
        super().__init__()
        self.route = route
        self.COLOR = [colors.PRIMARY, colors.SECONDARY, colors.ON_PRIMARY_CONTAINER, colors.TERTIARY, colors.ON_SURFACE_VARIANT]

        ###### LineChart: ######
        self.linechart_data = [
            LineChartData(
                data_points=[
                    LineChartDataPoint(0, 18),
                    LineChartDataPoint(3, 10),
                    LineChartDataPoint(6, 20),
                    LineChartDataPoint(9, 29),
                ],
                stroke_width=4,
                color=colors.PRIMARY,
                curved=True,
                stroke_cap_round=True,
                point=True,
            ),
        ]
        self.line_chart = LineChart(
            data_series=self.linechart_data,
            min_y=0,
            max_y=0,
            min_x=0,
            max_x=9,
            animate=200,
            horizontal_grid_lines=ChartGridLines( width=0.5, dash_pattern=[5, 5], color=colors.with_opacity(0.4, colors.ON_SURFACE)),
            border=Border(
                bottom=BorderSide(2, colors.with_opacity(0.5, colors.ON_SURFACE))
            ),
            top_axis=ChartAxis(
                title=Text("Evolução das Vendas (R$)",style=TextThemeStyle.TITLE_MEDIUM),
                title_size=30,
                labels=[
                    ChartAxisLabel(
                        value=9,
                        label=Text("")
                    )
                ]
            ),
            left_axis=ChartAxis(
                labels_size=40,
            ),
            bottom_axis=ChartAxis(
                labels=[
                    ChartAxisLabel(
                        value=0,
                        label=Container(
                            Text(
                                "SET",
                                size=14,
                                color=colors.ON_SURFACE,
                            ),
                            margin=margin.only(top=10),
                        ),
                    ),
                    ChartAxisLabel(
                        value=3,
                        label=Container(
                            Text(
                                "OUT",
                                size=14,
                                color=colors.ON_SURFACE,
                            ),
                            margin=margin.only(top=10),
                        ),
                    ),
                    ChartAxisLabel(
                        value=6,
                        label=Container(
                            Text(
                                "NOV",
                                size=14,
                                color=colors.ON_SURFACE,
                            ),
                            margin=margin.only(top=10),
                        ),
                    ),
                    ChartAxisLabel(
                        value=9,
                        label=Container(
                            Text(
                                "DEC",
                                size=14,
                                color=colors.ON_SURFACE,
                            ),
                            margin=margin.only(top=10),
                        ),
                    ),
                ],
                labels_size=32,
            ),
            tooltip_bgcolor=colors.with_opacity(1, colors.ON_PRIMARY),
            on_chart_event=self.on_line_chart_event,
        )

        ###### BarChart: ######
        self.bar_chart = BarChart(
            max_y = 0,
            interactive=True,
            animate=150,
            bar_groups=[
                BarChartGroup(
                    x=0,
                    bar_rods=[
                        BarChartRod(
                            from_y=0,
                            to_y=0,
                            width=40,
                            color=colors.PRIMARY,
                            tooltip="",
                            border_radius=border_radius.vertical(top=5, bottom=0),
                        ),
                    ],
                ),
                BarChartGroup(
                    x=1,
                    bar_rods=[
                        BarChartRod(
                            from_y=0,
                            to_y=0,
                            width=40,
                            color=colors.SECONDARY,
                            tooltip="",
                            border_radius=border_radius.vertical(top=5, bottom=0),
                        ),
                    ],
                ),
                BarChartGroup(
                    x=2,
                    bar_rods=[
                        BarChartRod(
                            from_y=0,
                            to_y=0,
                            width=40,
                            color=colors.ON_PRIMARY_CONTAINER,
                            tooltip="",
                            border_radius=border_radius.vertical(top=5, bottom=0),
                        ),
                    ],
                ),
                BarChartGroup(
                    x=3,
                    bar_rods=[
                        BarChartRod(
                            from_y=0,
                            to_y=0,
                            width=40,
                            color=colors.TERTIARY,
                            tooltip="",
                            border_radius=border_radius.vertical(top=5, bottom=0),
                        ),
                    ],
                ),
                BarChartGroup(
                    x=4,
                    bar_rods=[
                        BarChartRod(
                            from_y=0,
                            to_y=0,
                            width=40,
                            color=colors.INVERSE_PRIMARY,
                            tooltip="",
                            border_radius=border_radius.vertical(top=5, bottom=0),
                        ),
                    ],
                ),
            ],
            border=border.only(
                bottom=BorderSide(2, colors.with_opacity(0.5, colors.ON_SURFACE)),
            ),
            left_axis=ChartAxis(
                labels_size=40, title_size=40
            ),
            top_axis=ChartAxis(
                title=Text("Produtos mais lucrativos", tooltip="Produtos que geraram mais lucros", style=TextThemeStyle.TITLE_MEDIUM),
                title_size=30,
                labels=[
                    ChartAxisLabel(
                        value=9,
                        label=Text("")
                    )
                ]
            ),
            bottom_axis=ChartAxis(
                labels=[
                    ChartAxisLabel(
                        value=0, label=Container(Text(value="", size=14), padding=10)
                    ),
                    ChartAxisLabel(
                        value=1, label=Container(Text(value="", size=14), padding=10)
                    ),
                    ChartAxisLabel(
                        value=2, label=Container(Text(value="", size=14), padding=10)
                    ),
                    ChartAxisLabel(
                        value=3, label=Container(Text(value="", size=14), padding=10)
                    ),
                    ChartAxisLabel(
                        value=4, label=Container(Text(value="", size=14), padding=10)
                    ),
                ],
                labels_size=40,
            ),
            horizontal_grid_lines=ChartGridLines(
                color=colors.with_opacity(0.4, colors.ON_SURFACE), width=1, dash_pattern=[5, 5]
            ),
            tooltip_bgcolor=colors.with_opacity(1, colors.SURFACE),
            on_chart_event=self.on_bar_char_event,
        )

        ###### Indicator of Stock ######
        self.pie_stock = PieChart(
            animate=200,
            start_degree_offset=270,
            sections_space=0,
            #center_space_radius=50,
            expand=True,
            on_chart_event=self.on_pie_chart_event,
            sections=[
                PieChartSection(
                    value=40,
                    title_style=TextStyle(size=16, color=colors.WHITE),
                    color=colors.with_opacity(0.8, colors.PRIMARY),
                    radius=42,
                    border_side=border.BorderSide(0, color=colors.ON_PRIMARY_CONTAINER),
                    badge=Container(
                            alignment= alignment.center,
                            width=40,
                            height=40,
                            border=border.all(1, colors.PRIMARY),
                            border_radius=20,
                            bgcolor=colors.with_opacity(0.7, colors.SURFACE),
                            content=Text("40%", weight=FontWeight.BOLD),
                        ),
                    badge_position=1,
                ),
                PieChartSection(
                    value=60,
                    title_style=TextStyle(size=16, color=colors.WHITE, weight=FontWeight.BOLD),
                    color=colors.with_opacity(0.5,colors.SECONDARY_CONTAINER),
                    #radius=30,
                ),
            ]
        )

        ###### Cards: ######
        self.line_chart_card = Card(
            expand=5,
            surface_tint_color=colors.SURFACE_VARIANT,
            elevation=10.0,
            content=Container(
                padding=25,
                ink=True,
                content=self.line_chart,
            )
        )

        self.gauge_card = Card(
            expand=3,
            surface_tint_color=colors.SURFACE_VARIANT,
            elevation=10.0,
            content=Container(
                padding=20,
                ink=True,
                content=Column(
                    spacing=15,
                    horizontal_alignment='center',
                    alignment='center',
                    controls=[
                        Text("Estoque (%)", tooltip="Capacidade / Quantidade", style=TextThemeStyle.TITLE_MEDIUM),
                        self.pie_stock,
                    ]
                )
            )
        )

        self.bar_chart_card = Card(
            expand=5,
            surface_tint_color=colors.SURFACE_VARIANT,
            elevation=10.0,
            content=Container(
                padding=20,
                ink=True,
                content=self.bar_chart,
            )
        )

        self.text_registered_customers = Text(value="25", style=TextThemeStyle.DISPLAY_LARGE, color=colors.PRIMARY, weight=FontWeight.BOLD)
        self.text_variation_customers = Text("5%", color=colors.GREEN, size=22)
        self.btn_add_customer = OutlinedButton(text="Ad. Cliente", icon=icons.ADD_OUTLINED, on_click=self.add_customer_clicked)
        self.icon = Icon(name=icons.ARROW_DROP_UP, color='green')
        self.customer_card = Card(
            expand=True,
            surface_tint_color=colors.SURFACE_VARIANT,
            elevation=10,
            content=Container(
                padding=20,
                ink=True,
                content=Column(
                    alignment='center',
                    horizontal_alignment='center',
                    expand=True,
                    spacing=15,
                    controls=[
                        Column(
                            alignment='center',
                            horizontal_alignment='center',
                            spacing=0,
                            controls=[
                                Row(alignment='center', controls=[Icon(name=icons.PERM_CONTACT_CALENDAR_OUTLINED, color='primary', size=24), Text(value="Clientes Cadastrados", size=16)]),
                                self.text_registered_customers,
                            ]
                        ),
                        Column(
                            alignment='center',
                            horizontal_alignment='center',
                            spacing=0,
                            controls=[
                                Text('No mês', size=16),
                                Row(alignment='center', spacing=0, controls=[self.text_variation_customers, self.icon]),
                            ]
                        ),
                        self.btn_add_customer,
                    ]
                )
            )
        )

        self.text_today_sales = Text(value="10", style=TextThemeStyle.DISPLAY_LARGE, color=colors.PRIMARY, weight=FontWeight.BOLD)
        self.text_today_billing = Text(value="R$0,00", color=colors.GREEN, size=22)
        self.btn_add_sale = OutlinedButton(text="Nova Venda", icon=icons.ADD_OUTLINED, on_click=self.add_sale_clicked)
        self.sales_card = Card(
            expand=True,
            surface_tint_color=colors.SURFACE_VARIANT,
            elevation=10,
            content=Container(
                padding=20,
                ink=True,
                content=Column(
                    alignment='center',
                    horizontal_alignment='center',
                    expand=True,
                    spacing=15,
                    controls=[
                        Column(
                            alignment='center',
                            horizontal_alignment='center',
                            spacing=0,
                            controls=[
                                Row(alignment='center', controls=[Icon(name=icons.SHOPPING_CART_OUTLINED, color='primary', size=24), Text(value="Pedidos Hoje", size=16)]),
                                self.text_today_sales,
                            ]
                        ),
                        Column(
                            alignment='center',
                            horizontal_alignment='center',
                            spacing=0,
                            controls=[
                                Text('Faturamento', size=16),
                                Row(
                                    alignment='center',
                                    spacing=0,
                                    controls=[
                                        self.text_today_billing,
                                    ]
                                ),
                            ]
                        ),
                        self.btn_add_sale,
                    ]
                )
            )
        )

        self.text_numb_of_products = Text(value="105", style=TextThemeStyle.DISPLAY_LARGE, color=colors.PRIMARY, weight=FontWeight.BOLD)
        self.text_low_stock = Text(color=colors.GREEN, size=22, spans=[TextSpan(text="", style=TextStyle(size=16, color="green"), on_click=self.see_low_stock_clicked)])
        self.btn_add_product = OutlinedButton(text="Ad. Produto", icon=icons.ADD_OUTLINED, on_click=self.add_product_clicked)
        self.products_card = Card(
            expand=True,
            surface_tint_color=colors.SURFACE_VARIANT,
            elevation=10,
            content=Container(
                padding=20,
                ink=True,
                content=Column(
                    alignment='center',
                    horizontal_alignment='center',
                    expand=True,
                    spacing=15,
                    controls=[
                        Column(
                            alignment='center',
                            horizontal_alignment='center',
                            spacing=0,
                            controls=[
                                Row(alignment='center', controls=[Icon(name=icons.INVENTORY_2_OUTLINED, color='primary', size=24), Text(value="Produtos Cadastrados", size=16)]),
                                self.text_numb_of_products,
                            ]
                        ),
                        Column(
                            alignment='center',
                            horizontal_alignment='center',
                            spacing=0,
                            controls=[
                                Text('Produtos com estoque baixo', size=16),
                                Row(
                                    alignment='center',
                                    spacing=0,
                                    controls=[
                                        self.text_low_stock,
                                    ]
                                ),
                            ]
                        ),
                        self.btn_add_product,
                    ]
                )
            )
        )

    def build(self):
        self.home_content = Container(
            expand=True,
            margin=35,
            content=Column(    
                expand=True,
                spacing=40,                                                            
                controls=[
                    Row(
                        expand=4,
                        spacing=40,
                        controls=[
                            self.line_chart_card,
                            self.gauge_card,
                            self.bar_chart_card,
                        ],
                    ),
                    Row(
                        expand=5,
                        spacing=40,
                        controls=[
                            self.customer_card,
                            self.sales_card,
                            self.products_card,
                        ],
                    )
                ]
            )
        )

        self.content = Row(
            expand=True,
            spacing=10,
            controls=[                
                self.home_content,             
            ]
        )
        return self.content    

    def initialize(self):
        print("Initializing Home Page")

        self.route.menu.nnrail.selected_index = 0
        self.route.menu.update()

        self.update_stock_pie(self.get_percent_stock())

        data_id, data_value, data_descr = self.get_most_profitable_products()
        self.update_bar_chart(data_id, data_value, data_descr)

        sum_of_sales, months = self.get_data_from_sales()
        self.update_line_chart(sum_of_sales, months)

        numb_of_customers, numb_of_customers_past = self.get_numb_of_customers()
        self.update_customer_card(numb_of_customers, numb_of_customers_past)

        sales, billing = self.get_today_sales_billing()
        self.update_sales_card(sales, billing)

        numb_of_products, low_stock = self.get_numb_of_products_and_stock()
        self.update_products_card(numb_of_products, low_stock)

    def on_pie_chart_event(self, e: PieChartEvent):
        if e.type == "PointerHoverEvent":
            self.pie_stock.sections[0].color = colors.PRIMARY
            self.pie_stock.sections[0].radius = 40
        else:
            self.pie_stock.sections[0].color = colors.with_opacity(0.8, colors.PRIMARY)
            self.pie_stock.sections[0].radius = 42

        self.pie_stock.update()

    def on_line_chart_event(self, e: LineChartEvent):
        for serie in self.line_chart.data_series:
            serie.shadow = BoxShadow(spread_radius=8, blur_radius=5, color=colors.PRIMARY, offset=Offset(1, 1), blur_style=ShadowBlurStyle.NORMAL) if e.type == "PointerHoverEvent" else None
        self.line_chart.update()

    def on_bar_char_event(self, e: BarChartEvent):
        for group_index, group in enumerate(self.bar_chart.bar_groups):
            for rod in group.bar_rods:
                # rod.border_radius = border_radius.vertical(top=20, bottom=0) if e.group_index == group_index and e.type == "PointerHoverEvent" else border_radius.vertical(top=6, bottom=0)
                rod.color = colors.with_opacity(0.5, self.COLOR[group_index]) if e.group_index == group_index and e.type == "PointerHoverEvent" else colors.with_opacity(1, self.COLOR[group_index])
                if e.type == "PointerHoverEvent":
                    rod.width = 42
                else:
                    rod.width = 40
        self.bar_chart.update()

    def update_stock_pie(self, value):
        self.pie_stock.sections[0].value = value
        self.pie_stock.sections[0].badge.content.value = f"{int(value)}%"
        self.pie_stock.sections[1].value = 100 - value
        self.pie_stock.update()

    def update_line_chart(self, data, time):
        self.linechart_data = [
            LineChartData(
                data_points=[
                    LineChartDataPoint(0, data[0]),
                    LineChartDataPoint(3, data[1]),
                    LineChartDataPoint(6, data[2]),
                    LineChartDataPoint(9, data[3]),
                ],
                stroke_width=4,
                color=colors.PRIMARY,
                curved=True,
                stroke_cap_round=True,
                point=True,
            ),
        ]
        max_y = (int(max(data) / 10) + 1) * 10
        self.line_chart.max_y = max_y
        self.line_chart.data_series = self.linechart_data

        self.line_chart.bottom_axis.labels[0].label.content.value = time[0]
        self.line_chart.bottom_axis.labels[1].label.content.value = time[1]
        self.line_chart.bottom_axis.labels[2].label.content.value = time[2]
        self.line_chart.bottom_axis.labels[3].label.content.value = time[3]

        self.line_chart.update()

    def update_bar_chart(self, data_id, data_value, data_descr):
        if len(data_id) < 1:
            self.bar_chart.bar_groups.clear()
            self.bar_chart.top_axis.title.value = "Produtos mais lucrativos - não há dados"
            self.bar_chart.update()
            return
        
        self.bar_chart.top_axis.title.value = "Produtos mais lucrativos"
        max_y = (int(max(data_value) / 10) + 1) * 10 # round to multiples of 10
        self.bar_chart.max_y = max_y

        self.bar_chart.bar_groups.clear()
        for rod, data in enumerate(data_value):
            self.bar_chart.bar_groups.append(
                BarChartGroup(
                    x=rod,
                    bar_rods=[
                        BarChartRod(
                            from_y=0,
                            to_y=data,
                            width=40,
                            color=self.COLOR[rod],
                            tooltip=data_descr[rod],
                            border_radius=border_radius.vertical(top=5, bottom=0),
                        ),
                    ],
                ),    
            )

            self.bar_chart.bottom_axis.labels.append(
                ChartAxisLabel(value=rod, label=Container(Text(value=data_id[rod], size=14), padding=10)),
            )
        self.bar_chart.bottom_axis.labels_size = 40
        self.bar_chart.update()

    def get_percent_stock(self):
        mydb = DashboardDatabase(self.route)
        mydb.connect()
        result = mydb.select_percent_stock()
        mydb.close()
        return result

    def get_most_profitable_products(self):
        mydb = DashboardDatabase(self.route)
        mydb.connect()
        result = mydb.select_most_profitable()
        mydb.close
        
        data_id = []
        data_value = []
        data_descr = []
        for data in result:
            data_id.append(data[0])
            data_value.append(data[1])
            data_descr.append(data[2])

        return data_id, data_value, data_descr

    def get_first_last_day_of_months(self, number_of_months):
        months_list = {
            1: "Jan",
            2: "Fev",
            3: "Mar",
            4: "Abr",
            5: "Mai",
            6: "Jun",
            7: "Jul",
            8: "Ago",
            9: "Set",
            10: "Out",
            11: "Nov",
            12: "Dez",
        }

        dates = [
            (
                date(date.today().year, date.today().month, 1), # first day of the current month
                date.today()                                    # today
            )
        ]
        months = []

        for _ in range(number_of_months):
            last_day = dates[-1][0] - timedelta(days=1)         # get the last day of the previous month
            first_day = date(last_day.year, last_day.month, 1)  # get the first day of the previous month
            tup = (first_day, last_day)
            dates.append(tup)
            months.append(months_list[first_day.month])

        dates.pop(0)
        dates.reverse()
        months.reverse()
        return dates, months

    def get_data_from_sales(self):
        dates, months = self.get_first_last_day_of_months(4)
        mydb = DashboardDatabase(self.route)
        mydb.connect()
        result = mydb.select_sales_by_months(dates)
        mydb.close()
        return result, months

    def get_numb_of_customers(self):
        mydb = DashboardDatabase(self.route)
        mydb.connect()
        numb_of_customers, numb_of_customers_past = mydb.select_numb_of_customers()
        mydb.close
        return numb_of_customers, numb_of_customers_past

    def update_customer_card(self, numb_of_customers, numb_of_customers_past):
        if numb_of_customers_past > 0:
            variation = (numb_of_customers - numb_of_customers_past) / numb_of_customers_past * 100
        elif numb_of_customers > 0:
            variation = 100
        else:
            variation = 0

        self.text_registered_customers.value = numb_of_customers
        self.text_variation_customers.value = f"{Validator.format_to_currency(variation)}%"
        if variation == 0:
            self.text_variation_customers.color = "on_surface_variant"
            self.icon.color = "on_surface_variant"
            self.icon.name = icons.ARROW_RIGHT_OUTLINED
        else:
            self.text_variation_customers.color = "green"
            self.icon.color = "green"
            self.icon.name = icons.ARROW_DROP_UP_OUTLINED
        self.update()
        
    def get_today_sales_billing(self):
        mydb = DashboardDatabase(self.route)
        mydb.connect()
        result = mydb.select_today_sales_billing()
        mydb.close()
        return result

    def update_sales_card(self, sales, billing):
        self.text_today_sales.value = int(sales)
        self.text_today_billing.value = "R$0,00" if billing is None else f"R${Validator.format_to_currency(billing)}"
        self.update()

    def get_numb_of_products_and_stock(self):
        mydb = DashboardDatabase(self.route)
        mydb.connect()
        result = mydb.select_numb_of_products_and_stock()
        mydb.close()
        return result

    def update_products_card(self, numb_of_products, low_stock):
        self.text_numb_of_products.value = numb_of_products
        self.text_low_stock.value = low_stock
        if low_stock > 0:
            self.text_low_stock.spans[0].text = " (Ver)"
        else:
            self.text_low_stock.spans[0].text = ""
        self.update()

    def add_customer_clicked(self, e):
        self.route.page.go("/register_customer")
        self.route.bar.set_title('Cadastrar Novo Cliente')
        self.route.page.update()
        self.route.menu.nnrail.selected_index = 1
        self.route.menu.update()
    
    def add_sale_clicked(self, e):
        self.route.page.go("/register_sales")
        self.route.bar.set_title('Nova Venda')
        self.route.page.update()
        self.route.menu.nnrail.selected_index = 4
        self.route.menu.update()

    def add_product_clicked(self, e):
        self.route.page.go("/register_product")
        self.route.bar.set_title('Cadastrar Novo Produto')
        self.route.page.update()
        self.route.menu.nnrail.selected_index = 3
        self.route.menu.update()

    def see_low_stock_clicked(self, e):
        self.route.page.go("/products")
        self.route.bar.set_title("Produtos")
        self.route.page.update()

        result = self.route.products.get_low_stock()
        self.route.products.fill_in_table_products(result)
        self.route.menu.nnrail.selected_index = 3
        self.route.menu.update()
        
