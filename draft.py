from flet import (UserControl, Row, Column, Container, VerticalDivider, CrossAxisAlignment, MainAxisAlignment)

class ClassName(UserControl):
    def __init__(self, route):
        super().__init__()
        self.route = route

    def build(self):
        page_content = Container(
            #bgcolor='red',
            padding=0,
            border_radius=5,
            expand=True,
            content=Column(
                controls=[
                    # main body
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
                                    #content=

                                    #
                                    #Insert controls here
                                    #


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
                                            
                                            #
                                            #Insert controls here
                                            #

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
        print("Initializing 'YourClassName'")
        # Implement initializing of the page here
