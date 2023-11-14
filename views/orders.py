
import flet as ft

from styles.s_orders import SOrders


def Orders(page: ft.Page) -> ft.Column:
    """
    Página de las comandas.

    Se muestran las comandas que se han enviado al Sistema Digital de Comandas (SCD),
    cada una se puede eliminar, editar o cerrar.

    Utiliza los controles declarados en la clase :class:`SOrders` del archivo :file:`s_orders.py`

    Regresa un objeto de la clase :class:`ft.Column`
    """

    # Título de la lista de órdenes
    title: ft.Container = SOrders.title()
    # Contador de órdenes
    orders_counter: ft.Container = SOrders().active_counter()
    # Lista de órdenes
    order_list: ft.Container = SOrders().order_list()

    # Propiedades de la página de órdenes
    view: ft.Column = ft.Column(
        spacing = 25,
        # Se compone de:
        # - Título de la lista de órdenes
        # - Lista de órdenes
        controls = [
            ft.Container(
                padding = 25,
                expand = True,
                content = ft.Column(
                    alignment = ft.MainAxisAlignment.CENTER,
                    controls = [
                        # Título de la lista de órdenes y contador de órdenes
                        ft.Row(
                            alignment = ft.MainAxisAlignment.SPACE_AROUND,
                            controls = [
                                title,
                                orders_counter
                            ]
                        ),
                        # Lista de órdenes
                        order_list
                    ]
                )
            )
        ]
    )

    return view
