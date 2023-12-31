
import flet as ft

from styles.s_cashier import SCashier


def Cashier(page: ft.Page) -> ft.Column:
    """
    Página de la caja.

    Se muestra el catálogo de productos, el resumen con el total de la compra
    y dos botones para enviar la comanda al Sistema Digital de Comandas (SCD) o
    cancelar la comanda.

    Utiliza los controles declarados en la clase :class:`SCashier` del archivo :file:`s_cashier.py`

    Regresa un objeto de la clase :class:`ft.Column`
    """

    # Resumen de la comanda
    order_summary: ft.Container = SCashier.order_summary(page)
    # Título de catálogo de productos
    catalog_title: ft.Container = SCashier.catalog_title()
    # Barra de búsqueda
    search_bar: ft.Container = SCashier().search_bar()
    # Catálogo de productos
    catalog: ft.Container = SCashier().catalog()
    # Selector de tipo de cliente
    customer_type: ft.Container = SCashier().customer_type_selector()

    # Propiedades de la página de caja
    view: ft.Column = ft.Column(
        spacing = 25,
        # Se compone de:
        # - Catálogo de productos
        # - Resumen de la comanda
        controls = [
            ft.Container(
                padding = 25,
                expand = True,
                content = ft.Row(
                    alignment = ft.MainAxisAlignment.SPACE_EVENLY,
                    controls = [
                        # Catálogo de productos
                        ft.Column(
                            alignment = ft.MainAxisAlignment.CENTER,
                            spacing = 15,
                            controls = [
                                catalog_title,
                                search_bar,
                                catalog,
                                customer_type
                            ]
                        ),
                        # Resumen de la comanda
                        ft.Column(
                            alignment = ft.MainAxisAlignment.CENTER,
                            controls = [
                                order_summary
                            ]
                        )
                    ]
                )
            )
        ]
    )

    return view