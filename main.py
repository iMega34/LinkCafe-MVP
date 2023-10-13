
import flet as ft

from views.router import Router


def main(page: ft.Page) -> None:
    # Propiedades de la página
    page.title = "eTrigali"
    page.bgcolor = "#1F2129"
    page.fonts = {
        "Arbutus Slab" : "/fonts/ArbutusSlab-Regular.ttf",
        "Tenor Sans" : "/fonts/TenorSans-Regular.ttf",
        "Forum" : "/fonts/Forum-Regular.ttf"
    }

    # Declara del router de la clase Router para redireccionar 
    # a otras páginas del sitio
    router: Router = Router(page)

    # Asignación de la ruta a la que se va a acceder
    page.on_route_change = router.route_change

    # Se añade la página accedida por el router a la vista actual
    page.add(router.view)

    # Se accede a la pagina de inicio
    page.go('/cashier')


if __name__ == "__main__":
    ft.app(target = main, view = ft.AppView.WEB_BROWSER, assets_dir = "assets")
