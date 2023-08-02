from flet import Page, app, Theme, ThemeMode, colors

from InfostoreApp import InfostoreApp

def main(page: Page):
    page.title='Infostore'
    page.window_min_height = 700
    page.window_min_width = 1360

    page.theme_mode=ThemeMode.LIGHT
    page.theme = Theme(color_scheme_seed=colors.BLUE_300)

    infostore_app = InfostoreApp(page)
    page.on_route_change = infostore_app.route_change    

    page.add(
        infostore_app.body
    )
    
    page.go("/")
    page.update()

if __name__ == "__main__":
    app(target=main)