
import flet as ft

from styles.s_home import SHome
from styles.styles import Styles


def Home(page: ft.Page) -> ft.Column:
    """
    Página de inicio.

    Se muestra el logo de la empresa y dos botones que redireccionan a las
    páginas de caja y órdenes.

    Utiliza los controles declarados en la clase :class:`SHome` del archivo :file:`s_home.py`

    Regresa un objeto de la clase :class:`ft.Column`
    """

    # Propiedades de estilo de la página de inicio, se obtienen de la clase
    # Styles del archivo styles.py
    styles: dict[str] = Styles.home_styles()

    # Bienvenida a la página
    welcome: ft.Container = SHome.welcome()
    # Logo de la empresa
    logo: ft.Container = SHome.logo()
    # Botón hacia la vista de caja
    cashier_button: ft.Card = SHome().cashier_button(page)
    # Botón hacia la vista de órdenes
    orders_button: ft.Card = SHome().orders_button(page)

    # Propiedades de la página de inicio
    view: ft.Column = ft.Column(
        spacing = 25,
        # Se compone de:
        # - Control de imagen con el logo de la empresa
        # - Dos botones que redireccionan a las páginas de caja y órdenes
        controls = [
            ft.Container(
                expand = True,
                content = ft.Column(
                    alignment = ft.MainAxisAlignment.SPACE_EVENLY,
                    controls = [
                        # Bienvenida a la página
                        ft.Row(
                            alignment = ft.MainAxisAlignment.CENTER,
                            controls = [
                                welcome
                            ]
                        ),
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
                                ft.Container(
                                    width = styles["button_row"]["width"],
                                    height = styles["button_row"]["height"],
                                    content = ft.Row(
                                        alignment = ft.MainAxisAlignment.SPACE_EVENLY,
                                        controls = [
                                            # Botón hacia la vista de caja
                                            cashier_button,
                                            # Botón hacia la vista de órdenes
                                            orders_button
                                        ]
                                    )
                                )
                            ]
                        )
                    ]
                )
            )
        ]
    )

    return view