
import flet as ft

from styles.styles import Styles
from other.order_card import OrderCard
from other.db_connection import DBConnection


# Propiedades de estilo de la página de órdenes, se obtienen de la clase
# Styles del archivo styles.py
styles: dict[str] = Styles.orders_styles()


# Conexión con la base de datos
db_connection: DBConnection = DBConnection()
# Lista de órdenes
orders: dict[str] = db_connection.get_orders()
# Número de órdenes en el local
pos_orders: int = 0
# Número de órdenes de Rappi
rappi_orders: int = 0
# Número de órdenes de menú digital
digital_menu_orders: int = 0

# Objeto de la clase ft.ListView para contener los productos del catálogo
_list_view: ft.ListView = ft.ListView(
    horizontal = True,
    spacing = styles["list"]["spacing"],
)


class SOrders:
    """
    Propiedades de los controles utilizados por la función :function:`Orders`
    del archivo :file:`orders.py` para la creación de la página de órdenes.
    """

    def _build_order_list(self) -> None:
        """
        Construye la lista de órdenes.

        Parámetros:
            - :param:`page` (ft.Page): Página actual.

        Regresa:
            - No regresa ningún valor.
        """

        for id, details in orders.items():

            # Se extraen los datos de la orden
            customer_name: str = details["customer_name"]
            products_n_quantities: str = details["products_n_quantities"]
            total: str = details["total"]
            hour: str = details["hour"]
            origin: str = details["origin"]

            # Tarjeta de orden
            order_card: ft.Card = OrderCard(id, customer_name, products_n_quantities, total, hour, origin).build_card()

            _list_view.controls.append(order_card)


    def _calculate_order_quantity_by_origin(self) -> None:
        """
        Calcula la cantidad de órdenes por origen.

        Parámetros:
            - No recibe parámetros.

        Regresa:
            - No regresa ningún valor.
        """

        global pos_orders, rappi_orders, digital_menu_orders

        pos_orders = rappi_orders = digital_menu_orders = 0

        for order in orders.values():
            if order["origin"] == "Local":
                pos_orders += 1
            elif order["origin"] == "Rappi":
                rappi_orders += 1
            elif order["origin"] == "Menú digital":
                digital_menu_orders += 1


    def _subcounter(self, origin: str, quantity: int, tag_color: str) -> ft.Container:
        """
        Crea los contadores de órdenes por origen.

        Parámetros:
            - :param:`origin` (str): Origen de la orden.
            - :param:`quantity` (int): Cantidad de órdenes por origen.
            - :param:`tag_color` (str): Color de la etiqueta.

        Regresa:
            - :return:`counter` (ft.Container): Contador de órdenes por origen.
        """

        return ft.Container(
            alignment = ft.alignment.center,
            content = ft.Row(
                spacing = styles["counter"]["spacing"],
                alignment = ft.MainAxisAlignment.CENTER,
                controls = [
                    ft.Container(
                        width = styles["counter"]["tag_width"],
                        height = styles["counter"]["tag_height"],
                        bgcolor = tag_color,
                        border_radius = ft.border_radius.only(
                            bottom_left = styles["counter"]["tag_border_radius"],
                            bottom_right = styles["counter"]["tag_border_radius"]
                        ),
                    ),
                    ft.Text(
                        f"{origin}: {quantity}",
                        font_family = styles["counter"]["font"],
                        size = styles["counter"]["font_size"],
                        color = styles["counter"]["font_color"],
                        weight = ft.FontWeight.W_300,
                        text_align = ft.TextAlign.CENTER
                    )
                ]
            )
        )


    def title() -> ft.Container:
        """
        Título de la lista de órdenes.

        Parámetros:
            - No recibe parámetros.

        Regresa:
            - :return:`title_content` (ft.Container): Título de la lista de órdenes
        """

        title_content: ft.Container = ft.Container(
            width = styles["title"]["width"],
            alignment = ft.alignment.center_left,
            content = ft.Text(
                "Órdenes",
                font_family = styles["title"]["font"],
                size = styles["title"]["font_size"],
                color = styles["title"]["font_color"],
                weight = ft.FontWeight.W_300,
                text_align = ft.TextAlign.START
            )
        )

        return title_content


    def active_counter(self) -> ft.Container:
        """
        Contador de órdenes activas totales y por origen.

        Parámetros:
            - :param:`page` (ft.Page): Página actual.

        Regresa:
            - :return:`counter_content` (ft.Container): Contador de órdenes activas
        """

        # Calcula la cantidad de órdenes por origen
        self._calculate_order_quantity_by_origin()

        # Contador de órdenes activas totales
        total_counter: ft.Container = ft.Container(
            alignment = ft.alignment.center,
            content = ft.Text(
                f"Total activos: {len(orders)}",
                font_family = styles["counter"]["font"],
                size = styles["counter"]["font_size"],
                color = styles["counter"]["font_color"],
                weight = ft.FontWeight.W_300,
                text_align = ft.TextAlign.CENTER
            )
        )

        # Contador de órdenes activas por caja
        point_of_sale_counter: ft.Container = self._subcounter("Local", pos_orders, styles["counter"]["pos_color"])

        # Contador de órdenes activas por Rappi
        rappi_counter: ft.Container = self._subcounter("Rappi", rappi_orders, styles["counter"]["rappi_color"])

        # Contador de órdenes activas por menú digital
        digital_menu_counter: ft.Container = self._subcounter("Menú digital", digital_menu_orders, styles["counter"]["digital_menu_color"])

        # Contenedor de los contadores
        counter_content: ft.Container = ft.Container(
            width = styles["counter"]["width"],
            alignment = ft.alignment.center,
            content = ft.Column(
                alignment = ft.MainAxisAlignment.CENTER,
                controls = [
                    # Contador de órdenes activas totales
                    total_counter,
                    # Contador de órdenes activas por caja, Rappi y menú digital
                    ft.Row(
                        alignment = ft.MainAxisAlignment.SPACE_AROUND,
                        controls = [
                            point_of_sale_counter,
                            rappi_counter,
                            digital_menu_counter
                        ]
                    )
                ]
            )
        )

        return counter_content


    def order_list(self) -> ft.Container:
        """
        Lista de órdenes que se han enviado al SCD y se mostrarán en la página de órdenes
        como tarjetas.

        Parámetros:
            - :param:`page` (ft.Page): Página actual.

        Regresa:
            - :return:`order_list_content` (ft.Container): Lista de tarjetas con las órdenes
        """

        self._build_order_list()

        order_list_content: ft.Container = ft.Container(
            expand = True,
            content = _list_view
        )

        return order_list_content

