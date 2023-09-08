
import flet as ft

from styles.s_home import SHome


def Home(page: ft.Page) -> ft.Column:
    """
    Página de inicio.

    Se muestra el logo de la empresa y dos botones que redireccionan a las
    páginas de caja y órdenes.

    Utiliza los controles declarados en la clase :class:`SHome` del archivo :file:`s_home.py`

    Regresa un objeto de la clase :class:`ft.Column`
    """

    # Logo de la empresa
    logo: ft.Container = SHome.logo()
    # Fila de botones para el redireccionamiento de la ventana
    button_row: ft.Container = SHome.button_row(page)

    # Propiedades de la página de inicio
    view: ft.Column = ft.Column(
        spacing = 25,
        # Se compone de:
        # - Control de imagen con el logo de la empresa
        # - Dos botones que redireccionan a las páginas de caja y órdenes
        controls = [
            ft.Container(
                expand = True,
                border = ft.border.all(1, "#FF0000"),
                content = ft.Column(
                    alignment = ft.MainAxisAlignment.SPACE_EVENLY,
                    controls = [
                        # Logo de la empresa
                        ft.Row(
                            alignment = ft.MainAxisAlignment.CENTER,
                            controls = [
                                logo
                            ]
                        ),
                        # Fila de botones para el redireccionamiento de la ventana
                        ft.Row(
                            alignment = ft.MainAxisAlignment.CENTER,
                            controls = [
                                button_row
                            ]
                        )
                    ]
                )
            )
        ]
    )

    return view