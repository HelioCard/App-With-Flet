from flet import (UserControl, Container, IconButton, icons, NavigationRail, NavigationRailLabelType,
                  NavigationRailDestination, Icon, padding, border_radius)

class SideMenu(UserControl):
    ext = False
    def __init__(self, route):
        super().__init__()
        self.route = route
        
        self.cont = Container(            
            padding=padding.all(5),
            #bgcolor=colors.ON_INVERSE_SURFACE,                       
            border_radius=border_radius.all(5),
            visible=False,
        )        
        self.nnrail = NavigationRail(
            extended=self.ext,
            label_type=NavigationRailLabelType.NONE,
            min_width=56,                
            min_extended_width=160, 
            bgcolor='transparent',
            leading=IconButton(icon=icons.SWAP_HORIZ_ROUNDED, icon_size=40, tooltip="Mostrar/Ocultar Opções", on_click=self.menu_clicked),
            group_alignment=-0.95,
            destinations=[
                NavigationRailDestination(
                    icon=icons.COTTAGE_OUTLINED, selected_icon=icons.COTTAGE, label='Home',
                ),
                NavigationRailDestination(
                    icon_content=Icon(icons.PERM_CONTACT_CALENDAR_OUTLINED), selected_icon_content=Icon(icons.PERM_CONTACT_CALENDAR), label='Clientes'
                ),
                NavigationRailDestination(
                    icon_content=Icon(icons.PERSON_OUTLINED), selected_icon_content=Icon(icons.PERSON_ROUNDED), label='Usuários'
                ),
                NavigationRailDestination(
                    icon_content=Icon(icons.INVENTORY_2_OUTLINED), selected_icon_content=Icon(icons.INVENTORY), label='Produtos'
                ),
                NavigationRailDestination(
                    icon_content=Icon(icons.SHOPPING_CART_OUTLINED), selected_icon_content=Icon(icons.SHOPPING_CART), label='Vendas'
                ),
                # NavigationRailDestination(
                #     icon=icons.SETTINGS_OUTLINED, selected_icon_content=Icon(icons.SETTINGS), label='Configurações',
                # ),
            ],
            on_change=self.nav_clicked,
        )  
        self.cont.content=self.nnrail

    def build(self):     
        return self.cont

    def menu_clicked(self, e):
        self.nnrail.extended = not self.nnrail.extended        
        self.ext = self.nnrail.extended
        self.update()

    def nav_clicked(self, e):
        if e.control.selected_index == 0:            
            self.page.go("/home")
            self.route.bar.set_title('Pagina Inicial')
            self.route.page.update()
            self.update()
            return
        elif e.control.selected_index == 1:
            self.page.go("/customers")
            self.route.bar.set_title('Clientes')
            self.route.page.update()
            self.update()
            return
        elif e.control.selected_index == 2:            
            self.page.go("/users")
            self.route.bar.set_title('Controle de Usuários')
            self.route.page.update()
            self.update()
            return
        elif e.control.selected_index == 3:            
            self.page.go("/products")
            self.route.bar.set_title('Produtos')
            self.route.page.update()
            self.update()
            return
        elif e.control.selected_index == 4:
            self.page.go("/sales")
            self.route.bar.set_title('Vendas')
            self.route.page.update()
            self.update()

