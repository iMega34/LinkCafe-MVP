
import flet as ft

from styles.styles import Styles


# Propiedades de estilo de la página de inicio, se obtienen de la clase
# Styles del archivo styles.py
styles: dict[str] = Styles.home_styles()

class SHome:
    """
    Propiedades de los controles utilizados por la función :function:`Home`
    del archivo :file:`welcome.py` para la creación de la página de inicio.
    """

    def logo() -> ft.Container:
        """
        Logo de la empresa

        Regresa un objeto de la clase :class:`ft.Container`
        """

        logo_content: ft.Container = ft.Container(
            border = ft.border.all(1, "#FF0000"),
            width = styles["logo"]["width"],
            height = styles["logo"]["height"],
            content = ft.Image(
                src = "logo.png",
            )
        )

        return logo_content
    

    def button_row(page: ft.Page) -> ft.Container:
        """
        Fila de botones para el redireccionamiento de la ventana

        Recibe un objeto de la clase :class:`ft.Page` para poder
        realizar el redireccionamiento de vistas

        Regresa un objeto de la clase :class:`ft.Container`
        """

        button_row_content: ft.Container = ft.Container(
            width = styles["button_row"]["width"],
            height = styles["button_row"]["height"],
            border = ft.border.all(1, "#FF0000"),
            content = ft.Row(
                alignment = ft.MainAxisAlignment.SPACE_EVENLY,
                spacing = styles["button_row"]["spacing"],
                controls = [
                    # Botón hacia a la vista de caja
                    ft.Container(
                        width = 350,
                        height = 100,
                        alignment = ft.alignment.center,
                        border = ft.border.all(1, "#FF0000"),
                        content = ft.Text(
                            "Caja",
                            font_family = styles["button_row"]["font"],
                            size = styles["button_row"]["font_size"],
                            color = styles["button_row"]["font_color"],
                            weight = ft.FontWeight.W_300,
                            text_align = ft.TextAlign.CENTER
                        ),
                        on_click = lambda _: page.go("/cashier")
                    ),
                    # Botón hacia a la vista de órdenes
                    ft.Container(
                        width = 350,
                        height = 100,
                        alignment = ft.alignment.center,
                        border = ft.border.all(1, "#FF0000"),
                        content = ft.Text(
                            "Comandas",
                            font_family = styles["button_row"]["font"],
                            size = styles["button_row"]["font_size"],
                            color = styles["button_row"]["font_color"],
                            weight = ft.FontWeight.W_300,
                            text_align = ft.TextAlign.CENTER
                        ),
                        on_click = lambda _: page.go("/orders")
                    )
                ]
            )
        )

        return button_row_content

