from flet import (
    TextButton, Text, Row, Dropdown, PopupMenuButton, PopupMenuItem, icons, colors,
    Column, MainAxisAlignment, AlertDialog, dropdown, Icon, Theme, Checkbox, TextField,
    Divider, RadioGroup, Radio, ThemeMode
)
import json
import os

class SetGeneralConfig(AlertDialog):
    def __init__(self, route):
        super().__init__()
        self.route = route
        self.modal = True
        self.title=Row(expand=True, alignment='center', controls=[Text("Configurações", width=700, text_align='center')])

        self.dd_color_theme = Dropdown(dense=True, expand=True, label="Tema",value="Claro", options=[dropdown.Option('Claro'), dropdown.Option('Escuro')], on_change=self.theme_mode_changed)
        self.pmbtn_color_seed = PopupMenuButton(
            icon=icons.COLOR_LENS_OUTLINED,
            tooltip="Trocar cor do tema",
            items=[
                PopupMenuItem(
                    content=Row(
                        controls=[
                            Icon(icons.COLOR_LENS_OUTLINED, color=colors.PURPLE_300),
                            Text('Roxo')
                        ]
                    ),
                    on_click=self.change_color_seed,          
                ),
                PopupMenuItem(
                    content=Row(
                        controls=[
                            Icon(icons.COLOR_LENS_OUTLINED, color=colors.ORANGE_300),
                            Text('Laranja')
                        ]
                    ),
                    on_click=self.change_color_seed,           
                ),
                PopupMenuItem(
                    content=Row(
                        controls=[
                            Icon(icons.COLOR_LENS_OUTLINED, color=colors.GREEN_300),
                            Text('Verde')
                        ]
                    ),
                    on_click=self.change_color_seed,           
                ),
                PopupMenuItem(
                    content=Row(
                        controls=[
                            Icon(icons.COLOR_LENS_OUTLINED, color=colors.RED_300),
                            Text('Vermelho')
                        ]
                    ),
                    on_click=self.change_color_seed,           
                ),
                PopupMenuItem(
                    content=Row(
                        controls=[
                            Icon(icons.COLOR_LENS_OUTLINED, color=colors.BLUE_300),
                            Text('Azul')
                        ]
                    ),
                    on_click=self.change_color_seed,         
                ),
                PopupMenuItem(
                    content=Row(
                        controls=[
                            Icon(icons.COLOR_LENS_OUTLINED, color=colors.YELLOW_300),
                            Text('Amarelo')
                        ]
                    ),
                    on_click=self.change_color_seed,          
                ),
                PopupMenuItem(
                    content=Row(
                        controls=[
                            Icon(icons.COLOR_LENS_OUTLINED, color=colors.INDIGO_300),
                            Text('Indigo')
                        ]
                    ),
                    on_click=self.change_color_seed,          
                ),
                PopupMenuItem(
                    content=Row(
                        controls=[
                            Icon(icons.COLOR_LENS_OUTLINED, color=colors.TEAL_300),
                            Text('Teal')
                        ]
                    ),
                    on_click=self.change_color_seed,          
                ),
                PopupMenuItem(
                    content=Row(
                        controls=[
                            Icon(icons.COLOR_LENS_OUTLINED, color=colors.LIME_300),
                            Text('Lime')
                        ]
                    ),
                    on_click=self.change_color_seed,          
                ),
                PopupMenuItem(
                    content=Row(
                        controls=[
                            Icon(icons.COLOR_LENS_OUTLINED, color=colors.BROWN_400),
                            Text('Marrom')
                        ]
                    ),
                    on_click=self.change_color_seed,          
                ),
            ]
        )
        self.extend_menu = Checkbox(value=False, label="Menu lateral extendido", on_change=self.extended_menu_changed)

        self.tf_company_name = TextField(label='Nome da Empresa', dense=True, expand=True)
        self.tf_adress = TextField(label='Endereço', dense=True, expand=4)
        self.tf_tel = TextField(label='Telefone', dense=True, expand=1)
        self.tf_email = TextField(label='Email', dense=True, expand=True)
        
        self.btn_back = TextButton(text="Voltar", on_click=self.back_clicked)
        self.btn_save = TextButton(text="Salvar Configurações", tooltip='Salvar configurações como "default"')

        self.actions=[
            Column(
                width=700,
                expand=True,
                controls=[
                    Text(value='Configurações Gerais:'),
                    Row(
                        controls=[
                            self.dd_color_theme,
                            self.pmbtn_color_seed,
                            self.extend_menu,
                        ]
                    ),
                    Divider(height=1, color='transparent'),
                    Text(value='Dados da Empresa:'),
                    Column(controls=[
                        Row(controls=[
                            self.tf_company_name,
                            self.tf_email,
                        ]),
                        Row(controls=[
                            self.tf_adress,
                            self.tf_tel,
                        ]),
                    ]),
                    Divider(height=1, color='transparent'),
                    Text(value='Filtros de Venda:'),
                    RadioGroup(
                        content=Column(
                            spacing=0,
                            controls=[
                                Radio(value='today', label='Exibir vendas do dia'),
                                Radio(value='seven', label='Exibir vendas dos últimos sete dias'),
                                Radio(value='thirty', label='Exibir vendas dos últimos trinta dias'),
                                Radio(value='all', label='Exibir todas as vendas'),
                            ]
                        ),
                        on_change=self.change_radio_group
                    ),
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

    def change_color_seed(self, e):
        self.route.page.theme = Theme(
            color_scheme_seed=e.control.content.controls[0].color
        )
        self.route.page.update()

    def change_radio_group(self, e):
        buttons = {
            "today": self.route.sales.btn_filter_today,
            "seven": self.route.sales.btn_filter_previous_seven,
            "thirty": self.route.sales.btn_filter_previous_thirty,
            "all": self.route.sales.btn_filter_all,
        }
        
        for key in buttons:
            buttons[key].selected = False
        buttons[e.control.value].selected = True
        if self.route.bar.text_title.value == "Vendas":
            self.route.sales.fill_in_table_sales()
            self.route.sales.update()

    def theme_mode_changed(self, e):
        if self.dd_color_theme.value == "Claro":
            self.route.page.theme_mode = ThemeMode.LIGHT
            self.route.bar.btn_change_theme.icon = icons.DARK_MODE_OUTLINED
        else:
            self.route.page.theme_mode = ThemeMode.DARK
            self.route.bar.btn_change_theme.icon = icons.WB_SUNNY_OUTLINED
        
        self.route.page.update()

    def extended_menu_changed(self, e):
        self.route.menu.nnrail.extended = e.control.value
        self.route.menu.update()
