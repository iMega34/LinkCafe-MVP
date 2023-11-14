
import flet as ft

from styles.styles import Styles


# Propiedades de estilo de los componentes de la tarjeta de orden, 
# se obtienen de la clase :class:`Styles` del archivo :file:`styles.py`
styles: dict[str] = Styles.orders_styles()


class OrderCard:
    """
    Contiene los métodos para crear la tarjeta de orden
    """

    def __init__(self, order_id: str, customer_name: str, products: dict[str], total: str, hour: str, origin: str) -> ft.Card:
        # Atributos privados
        self.__order_id: str = order_id
        self.__customer_name: str = customer_name
        self.__products: dict[str] = products
        self.__hour: str = hour
        self.__total: str = total
        self.__origin: str = origin


    def _order_card_on_hover(self, _: ft.HoverEvent, card: ft.Container) -> None:
        """
        Permite a la tarjeta de orden elevarse al pasar el cursor sobre ella

        Parámetros:
            - :param:`_` (ft.HoverEvent): Evento de pasar el cursor sobre la tarjeta de orden

        Regresa:
            - No regresa nada.
        """

        if _.data == "true":
            card.border = ft.border.all(1, "#8B9DDE")
            card.update()

        else:
            card.border = ft.border.all(1, "#00000000")
            card.update()


    def _button_on_hover(self, _: ft.HoverEvent, button: ft.Container) -> None:
        """
        Permite a los botones de la tarjeta colorear su borde al pasar el cursor sobre ellos

        Parámetros:
            - :param:`_` (ft.HoverEvent): Evento de pasar el cursor sobre los botones
            - :param:`button` (ft.Container): Botón que se coloreará

        Regresa:
            - No regresa nada.
        """

        if _.data == "true":
            button.border = ft.border.all(3, "#F4FF2B")
            button.update()

        else:
            button.border = ft.border.all(3, "#00000000")
            button.update()


    def _origin_tag(self) -> ft.Container:
        """
        Etiqueta que indica el origen de la orden por medio de un color

        Parámetros:
            - No recibe parámetros.

        Regresa:
            - :return:`origin_tag` (ft.Container): Etiqueta que indica el origen de la orden.
        """

        # Etiqueta que indica el origen de la orden
        origin_tag: ft.Container = ft.Container(
            width = styles["counter"]["tag_width"],
            height = styles["counter"]["tag_height"] - 5,
            border_radius = ft.border_radius.only(
                bottom_left = styles["counter"]["tag_border_radius"],
                bottom_right = styles["counter"]["tag_border_radius"]
            ),
            offset = ft.Offset(
                x = 0.25,
                y = -0.85
            )
        )

        # Color de la etiqueta
        if self.__origin == "Local":
            origin_tag.bgcolor = styles["counter"]["pos_color"]
        elif self.__origin == "Rappi":
            origin_tag.bgcolor = styles["counter"]["rappi_color"]
        elif self.__origin == "Menú digital":
            origin_tag.bgcolor = styles["counter"]["digital_menu_color"]

        return origin_tag


    def _order_id(self) -> ft.Container:
        """
        ID de la orden

        Parámetros:
            - No recibe parámetros.

        Regresa:
            - :return:`order_id_content` (ft.Container): ID de la orden.
        """

        order_id_content: ft.Container = ft.Container(
            alignment = ft.alignment.center,
            content = ft.Text(
                f"Orden {self.__order_id}",
                font_family = styles["card"]["font_order"],
                size = styles["card"]["font_size"],
                color = styles["card"]["font_color"],
                weight = ft.FontWeight.W_300,
                text_align = ft.TextAlign.START
            )
        )

        return order_id_content


    def _customer_name(self) -> ft.Container:
        """
        Nombre del cliente

        Parámetros:
            - No recibe parámetros.

        Regresa:
            - :return:`customer_name_content` (ft.Container): Nombre del cliente.
        """

        customer_name_content: ft.Container = ft.Container(
            alignment = ft.alignment.center,
            content = ft.Text(
                self.__customer_name,
                font_family = styles["card"]["font_customer"],
                size = styles["card"]["font_size"],
                color = styles["card"]["font_color"],
                weight = ft.FontWeight.W_300,
                text_align = ft.TextAlign.START
            )
        )

        return customer_name_content


    def _product_text(self, product: str, quantity: str) -> ft.Container:
        """
        Crear el texto de un producto con su cantidad y las propiedades de estilo

        Parámetros:
            - :param:`product` (str): Nombre del producto.
            - :param:`quantity` (str): Cantidad del producto.

        Regresa:
            - :return:`product_line` (tuple[ft.Container, ft.Container]): Contenedores con el nombre
            y la cantidad del producto.
        """

        # Texto del producto
        _product: ft.Container = ft.Container(
            width = styles["card"]["product_width"],
            alignment = ft.alignment.center_left,
            content = ft.Text(
                product,
                font_family = styles["card"]["font_details"],
                size = styles["card"]["font_size_details"],
                color = styles["card"]["font_color"],
                weight = ft.FontWeight.W_300,
                text_align = ft.TextAlign.START
            )
        )

        # Texto de la cantidad con un color de fondo
        _quantity: ft.Container = ft.Container(
            width = styles["card"]["quantity_width"],
            height = styles["card"]["quantity_height"],
            bgcolor = styles["card"]["quantity_bgcolor"],
            border_radius = ft.border_radius.all(styles["card"]["border_radius"] - 30),
            alignment = ft.alignment.center,
            content = ft.Text(
                quantity,
                font_family = styles["card"]["font_details"],
                size = styles["card"]["font_size_quantity"],
                color = styles["card"]["font_color"],
                weight = ft.FontWeight.W_300,
                text_align = ft.TextAlign.START
            )
        )

        return _product, _quantity


    def _product_list(self) -> ft.Container:
        """
        Lista de productos con sus respectivas cantidades

        Parámetros:
            - No recibe parámetros.

        Regresa:
            - :return:`product_list_content` (ft.Container): Lista de productos con sus respectivas cantidades.
        """

        _list: ft.ListView = ft.ListView(
            spacing = styles["card"]["spacing"],
        )

        # Agrega los productos y sus cantidades a la lista como filas a la variable _list
        for product, quantity in self.__products.items():

            # Transforma el producto y la cantidad en un contenedor
            product_name_element, product_quantity_element = self._product_text(product, quantity)

            # Crea una fila con el producto y la cantidad
            row: ft.Row = ft.Row(
                alignment = ft.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment = ft.CrossAxisAlignment.CENTER,
                controls = [
                    product_name_element,
                    product_quantity_element
                ]
            )

            # Agrega la fila a la lista
            _list.controls.append(row)

        product_list_content: ft.Container = ft.Container(
            expand = True,
            border_radius = ft.border_radius.all(styles["card"]["border_radius"]),
            bgcolor = styles["card"]["details_bgcolor"],
            padding = styles["card"]["padding"],
            alignment = ft.alignment.center,
            content = _list
        )

        return product_list_content


    def _hour_and_total(self) -> ft.Container:
        """
        Hora a la que se realizó la orden y el total de la orden

        Parámetros:
            - No recibe parámetros.

        Regresa:
            - :return:`hour_and_total_content` (ft.Container): Hora y total de la orden.
        """

        _hour: ft.Container = ft.Container(
            alignment = ft.alignment.center,
            content = ft.Text(
                f"Hora - {self.__hour}",
                font_family = styles["card"]["font_details"],
                size = styles["card"]["font_size_hour_n_total"],
                color = styles["card"]["font_color"],
                weight = ft.FontWeight.W_300,
                text_align = ft.TextAlign.START
            )
        )

        _total: ft.Container = ft.Container(
            alignment = ft.alignment.center,
            content = ft.Text(
                f"Total: ${self.__total}",
                font_family = styles["card"]["font_details"],
                size = styles["card"]["font_size_hour_n_total"],
                color = styles["card"]["font_color"],
                weight = ft.FontWeight.W_300,
                text_align = ft.TextAlign.START
            )
        )

        hour_and_total_content: ft.Container = ft.Container(
            height = styles["card"]["hour_n_total_height"],
            border_radius = ft.border_radius.all(styles["card"]["hour_n_total_border_radius"]),
            padding = ft.Padding(25, 0, 25, 0),
            alignment = ft.alignment.center,
            bgcolor = styles["card"]["details_bgcolor"],
            content = ft.Row(
                alignment = ft.MainAxisAlignment.SPACE_BETWEEN,
                controls = [
                    _hour,
                    _total
                ]
            )
        )

        return hour_and_total_content
    

    def _button(self, text: str, color: str) -> ft.Container:
        """
        Crea un botón para la tarjeta de orden

        Parámetros:
            - :param:`text` (str): Texto del botón.
            - :param:`color` (str): Color del botón.

        Regresa:
            - :return:`button_content` (ft.Container): Botón para la tarjeta de orden.
        """

        button_content: ft.Container = ft.Container(
            bgcolor = color,
            width = styles["card"]["button_width"],
            height = styles["card"]["button_height"],
            border_radius = ft.border_radius.all(styles["card"]["border_radius"]),
            animate = ft.animation.Animation(250, ft.AnimationCurve.EASE_IN),
            alignment = ft.alignment.center,
            # Contenido del botón
            content = ft.Text(
                text,
                font_family = styles["card"]["font_details"],
                size = styles["card"]["font_size_button"],
                color = styles["card"]["font_color"],
                weight = ft.FontWeight.W_300,
                text_align = ft.TextAlign.CENTER
            ),
            on_hover = lambda _: self._button_on_hover(_, button_content)
        )

        return button_content


    def _button_row(self) -> ft.Container:
        """
        Botones para cancelar, editar y marcar como entregada la orden

        Parámetros:
            - No recibe parámetros.

        Regresa:
            - :return:`button_row` (ft.Container): Botones para cancelar, editar y marcar como entregada la orden.
        """

        # Botón para cancelar la orden
        _cancel_button: ft.Container = self._button("Cancelar", styles["card"]["cancel_color"])

        # Botón para editar la orden
        _edit_button: ft.Container = self._button("Editar", styles["card"]["edit_color"])

        # Botón para marcar como entregada la orden
        _delivered_button: ft.Container = self._button("Entregado", styles["card"]["delivered_color"])

        # Se colocan los botones dentro de un objeto de la clase ft.Container
        buttons_content: ft.Container = ft.Container(
            content = ft.Row(
                alignment = ft.MainAxisAlignment.SPACE_BETWEEN,
                controls = [
                    _cancel_button,
                    _edit_button,
                    _delivered_button
                ]
            ) 
        )

        return buttons_content


    def build_card(self) -> ft.Card:
        """
        Construye la tarjeta de orden

        Contiene el ID de la orden, el nombre del cliente, los productos, la hora y el total

        Parámetros:
            - No recibe parámetros.

        Regresa:
            - :return:`card` (ft.Card): Tarjeta de orden.
        """

        # Contenido de la tarjeta de orden
        card: ft.Container = ft.Container(
            border_radius = styles["card"]["border_radius"],
            width = styles["card"]["width"],
            bgcolor = styles["card"]["bgcolor"],
            padding = styles["card"]["padding"],
            animate = ft.animation.Animation(250, ft.AnimationCurve.EASE_IN),
            alignment = ft.alignment.center,
            # Contenido de la tarjeta de orden
            content = ft.Stack(
                controls = [
                    # Etiqueta que indica el origen de la orden
                    self._origin_tag(),
                    # Contenido de la tarjeta de orden
                    ft.Column(
                        alignment = ft.MainAxisAlignment.CENTER,
                        controls = [
                            # ID de la orden y nombre del cliente
                            ft.Row(
                                alignment = ft.MainAxisAlignment.SPACE_BETWEEN,
                                controls = [
                                    self._order_id(),
                                    self._customer_name()
                                ]
                            ),
                            # Lista de productos con sus respectivas cantidades
                            self._product_list(),
                            # Hora y total de la orden
                            self._hour_and_total(),
                            # Botones para cancelar, editar y marcar como entregada la orden
                            self._button_row()
                        ]
                    )
                ]
            ),
            on_hover = lambda _: self._order_card_on_hover(_, card)
        )

        return card
