
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

    # Catálogo de productos

    # Resumen de la comanda
    order_summary: ft.Container = SCashier.order_summary()
    # Catálogo de productos
    catalog: ft.Container = SCashier.catalog(page)

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
                            controls = [
                                catalog
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