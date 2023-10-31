
import flet as ft

from styles.styles import Styles
from other.product import Product
from other.product_list import ProductList


# Propiedades de estilo de los componentes de productos, se obtienen de la clase
# Styles del archivo styles.py
styles: dict[str] = Styles.product_styles()


class ProductCard:
    """
    Contiene los métodos para la creación de la tarjeta de producto.

    Require de la creación de un objeto de la clase :class:`Product` para poder construir la tarjeta. 
    """

    def __init__(self, producto: Product) -> None:
        self._product: Product = producto
        self._card: ft.Card = ft.Card()
        self._ticket_card: ft.Card = ft.Card()


    def _card_on_hover(self, _: ft.HoverEvent) -> None:
        """
        Permite a la tarjeta elevarse al pasar el cursor sobre ella
        """

        if _.data == "true":
            for __ in range(10):
                self._card.elevation += 1
                self._card.update()

            self._card.content.border = ft.border.all(1, "#8B9DDE")
            self._card.content.update()

        else:
            for __ in range(10):
                self._card.elevation -= 1
                self._card.update()

            self._card.content.border = ft.border.all(0, "#00000000")
            self._card.content.update()


    def _ticket_card_on_hover(self, _: ft.HoverEvent) -> None:
        """
        Permite a la tarjeta elevarse al pasar el cursor sobre ella
        """

        if _.data == "true":
            for __ in range(10):
                self._ticket_card.elevation += 1
                self._ticket_card.update()

            self._ticket_card.content.border = ft.border.all(1, "#8B9DDE")
            self._ticket_card.content.update()

        else:
            for __ in range(10):
                self._ticket_card.elevation -= 1
                self._ticket_card.update()

            self._ticket_card.content.border = ft.border.all(0, "#00000000")
            self._ticket_card.content.update()


    def _add_to_cart(self, _: ft.ControlEvent, product_list_content: ft.Container, product_list: ProductList, total: ft.Container, customer_type: str) -> None:
        """
        Agrega un producto al carrito de compras

        Parámetros de acarreo:
            - :param:`product_list_content` (ft.Container): Contenedor de la lista de productos añadidos.
            - :param:`product_list` (ProductList): Lista de productos.
            - :param:`total` (ft.Container): Contenedor del total de la compra.
            - :param:`customer_type` (str): Tipo de cliente.

        Regresa:
            - No regresa ningún valor.
        """

        product_to_add: ft.Card = self.build_ticket_card(product_list_content, product_list, total, customer_type)
        product_list.add_to_list(product_list_content, product_to_add, total)


    def build_card(self, odd_row: bool, product_list_content: ft.Container , product_list: ProductList, total: ft.Container, customer_type: str) -> ft.Card:
        """
        Construye una tarjeta de producto a partir de un objeto de la clase :class:`Product`.

        Contiene el nombre del producto, su precio y su imagen.

        Parámetros:
            - odd_row (bool): Indica si la tarjeta se encuentra en una fila par o impar.

        Parámetros de acarreo:
            - :param:`product_list_content` (ft.Container): Contenedor de la lista de productos añadidos.
            - :param:`product_list` (ProductList): Lista de productos.
            - :param:`total` (ft.Container): Contenedor del total de la compra.
            - :param:`customer_type` (str): Tipo de cliente.

        Regresa:
            - :return:`card` (ft.Card): Tarjeta de producto construida.
        """

        # Se cambia el color de fondo de la tarjeta dependiendo de si se encuentra en una fila par o impar
        if odd_row:
            styles["card"]["bgcolor_1"] = "#4F5467"
            styles["card"]["bgcolor_2"] = "#2F374C"
        else:
            styles["card"]["bgcolor_1"] = "#2F374C"
            styles["card"]["bgcolor_2"] = "#4F5467"

        price_str: str = ""

        if customer_type == r"Empleado - 15% descuento":
            price_str = self._product.employee_price
        elif customer_type == r"Socio - 30% descuento":
            price_str = self._product.partner_price
        else:
            price_str = self._product.price

        # Nombre del producto
        name: ft.Container = ft.Container(
            height = styles["name"]["height"],
            alignment = ft.alignment.center,
            content = ft.Text(
                self._product.name,
                font_family = styles["name"]["font"],
                size = styles["name"]["font_size"],
                color = styles["name"]["font_color"],
                weight = ft.FontWeight.W_500,
                text_align = ft.TextAlign.START,
                no_wrap = True
            )
        )

        # Precio del producto
        price: ft.Container = ft.Container(
            height = styles["price"]["height"],
            alignment = ft.alignment.center,
            content = ft.Text(
                f"${price_str}",
                key = price_str,
                font_family = styles["price"]["font"],
                size = styles["price"]["font_size"],
                color = styles["price"]["font_color"],
                weight = ft.FontWeight.W_300
            )
        )

        # Imagen del producto
        image: ft.Container = ft.Container(
            height = styles["image"]["height"],
            alignment = ft.alignment.center,
            content = ft.Image(
                width = styles["image"]["width"],
                height = styles["image"]["height"],
                src = self._product.image
            )
        )

        # Se coloca el nombre, la imagen y el precio del producto dentro de un objeto
        # de la clase ft.Container
        card_content: ft.Container = ft.Container(
            width = styles["card"]["width"],
            height = styles["card"]["height"],
            padding = styles["card"]["padding"],
            bgcolor = styles["card"]["bgcolor_2"] if self._product.id % 2 == 0 else styles["card"]["bgcolor_1"],
            animate = ft.animation.Animation(250, ft.AnimationCurve.EASE_OUT),
            # Contenido de la tarjeta del producto
            content = ft.Column(
                alignment = ft.MainAxisAlignment.CENTER,
                controls = [
                    # Nombre del producto con su precio y su imagen
                    ft.Row(
                        controls = [
                            ft.Container(
                                width = styles["card"]["width_container"],
                                height = styles["card"]["height_container"],
                                alignment = ft.alignment.center,
                                content = ft.Column(
                                    controls = [
                                        # Nombre del producto
                                        name,
                                        # Imagen del producto
                                        image,
                                        # Precio del producto
                                        price
                                    ]
                                )
                            )
                        ]
                    )
                ]
            ),
            on_hover = lambda _: self._card_on_hover(_),
            on_click = lambda _: self._add_to_cart(_, product_list_content, product_list, total, customer_type),
        )

        # Se coloca el contenido de la tarjeta dentro de un objeto de la clase ft.Card
        # para poder elevarla al pasar el cursor sobre ella
        self._card = ft.Card(
            elevation = 0,
            color = styles["card"]["hover_color"],
            shadow_color = styles["card"]["shadow_color"],
            surface_tint_color = styles["card"]["tint_color"],
            content = card_content
        )

        return self._card


    def build_ticket_card(self, product_list_content: ft.Container, product_list: ProductList, total: ft.Container, customer_type: str) -> ft.Card:
        """
        Construye una tarjeta de producto a partir de un objeto de la clase :class:`Product`.

        Versión simplificada de la tarjeta de producto, contiene únicamente el nombre del producto, precio
        y la cantidad del producto en la lista, así como un botón para eliminar el producto de la lista.

        Parámetros:
            - :param:`product_list_content` (ft.Container): Contenedor de la lista de productos añadidos.
            - :param:`product_list` (ProductList): Lista de productos.
            - :param:`total` (ft.Container): Contenedor del total de la compra.
            - :param:`customer_type` (str): Tipo de cliente.

        Regresa:
            - :return:`simple_card` (ft.Card): Tarjeta de producto simplificada construida.
        """

        if customer_type == r"Empleado - 15% descuento":
            price_str = self._product.employee_price
        elif customer_type == r"Socio - 30% descuento":
            price_str = self._product.partner_price
        else:
            price_str = self._product.price

        # Nombre del producto
        name: ft.Container = ft.Container(
            width = styles["ticket_card"]["name_width"],
            alignment = ft.alignment.center_left,
            content = ft.Text(
                self._product.name,
                font_family = styles["ticket_card"]["font"],
                size = styles["ticket_card"]["font_size"],
                color = styles["ticket_card"]["font_color"],
                weight = ft.FontWeight.W_500,
                text_align = ft.TextAlign.CENTER,
                no_wrap = True
            )
        )

        # Precio del producto
        price: ft.Container = ft.Container(
            width = styles["ticket_card"]["price_width"],
            alignment = ft.alignment.center,
            content = ft.Text(
                f"${price_str}",
                key = price_str,
                font_family = styles["ticket_card"]["font"],
                size = styles["ticket_card"]["font_size"],
                color = styles["ticket_card"]["font_color"],
                weight = ft.FontWeight.W_300
            )
        )

        # Botón para restar en uno la cantidad del producto en la lista
        _remove_one_button: ft.IconButton = ft.IconButton(
            icon = ft.icons.REMOVE,
            icon_color = styles["ticket_card"]["button_color"],
            on_click = lambda _: product_list.reduce_one(product_list_content, self._ticket_card, total)
        )

        # Botón para sumar en uno la cantidad del producto en la lista
        _add_one_button: ft.IconButton = ft.IconButton(
            icon = ft.icons.ADD,
            icon_color = styles["ticket_card"]["button_color"],
            on_click = lambda _: product_list.add_to_list(product_list_content, self._ticket_card, total)
        )

        # Cuadro de texto para mostrar la cantidad del producto en la lista
        _quantity_viewer: ft.TextField = ft.TextField(
            value = "1",
            width = styles["ticket_card"]["text_field_width"],
            text_align = ft.TextAlign.CENTER,
            text_style = ft.TextStyle(
                font_family = styles["ticket_card"]["font"],
                color = styles["ticket_card"]["font_color"],
            ),
            text_size = styles["ticket_card"]["text_field_font_size"],
            bgcolor = styles["ticket_card"]["text_field_bgcolor"],
            border_color = styles["ticket_card"]["text_field_border_color"],
            border_radius = styles["ticket_card"]["text_field_border_radius"],
            on_change = lambda _: product_list.add_from_text_field(product_list_content, self._ticket_card, total)
        )

        # Se coloca el contador de productos dentro de un objeto de la clase ft.Container
        counter: ft.Container = ft.Container(
            alignment = ft.alignment.center,
            content = ft.Row(
                alignment = ft.MainAxisAlignment.SPACE_EVENLY,
                controls = [
                    _remove_one_button,
                    _quantity_viewer,
                    _add_one_button
                ]
            )
        )

        # Botón para eliminar el producto de la lista
        delete_button: ft.IconButton = ft.IconButton(
            icon = ft.icons.CLOSE_ROUNDED,
            icon_color = styles["ticket_card"]["remove_button_color"],
            icon_size = styles["ticket_card"]["remove_button_size"],
            on_click = lambda _: product_list.delete(product_list_content, self._ticket_card, total)
        )

        # Se coloca el nombre, el precio, el contador de productos y el botón para eliminar
        # dentro de un objeto de la clase ft.Container
        ticket_card_content: ft.Container = ft.Container(
            expand = True,
            height = styles["ticket_card"]["height"],
            padding = styles["ticket_card"]["padding"],
            bgcolor = styles["ticket_card"]["color"],
            border_radius = ft.border_radius.all(styles["ticket_card"]["border_radius"]),
            animate = ft.animation.Animation(250, ft.AnimationCurve.EASE_OUT),
            # Contentido de la tarjeta de producto en el ticket
            content = ft.Row(
                alignment = ft.MainAxisAlignment.SPACE_AROUND,
                controls = [
                    # Botón para eliminar el producto del carrito
                    delete_button,
                    # Nombre del producto
                    name,
                    # Contador de productos
                    counter,
                    # Precio del producto
                    price
                ]
            ),
            on_hover = lambda _: self._ticket_card_on_hover(_)
        )

        # Se coloca el contenido de la tarjeta dentro de un objeto de la clase ft.Card
        # para poder elevarla al pasar el cursor sobre ella
        self._ticket_card = ft.Card(
            elevation = 0,
            color = styles["ticket_card"]["hover_color"],
            shadow_color = styles["ticket_card"]["shadow_color"],
            surface_tint_color = styles["ticket_card"]["tint_color"],
            content = ticket_card_content
        )

        return self._ticket_card
