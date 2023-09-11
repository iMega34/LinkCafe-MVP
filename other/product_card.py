
import sys
import flet as ft

from other.product import Product
from styles.styles import Styles


# Evita la creación de archivos .pyc, debido a problemas de arranque
# en algunas ejecuciones
sys.dont_write_bytecode = True

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
        self._simple_card: ft.Card = ft.Card()


    def _card_on_hover(self, _: ft.HoverEvent) -> None:
        """
        Permite a la tarjeta elevarse al pasar el cursor sobre ella
        """

        if _.data == "true":
            for __ in range(50):
                self._card.elevation += 1
                self._card.update()

            self._card.content.border = ft.border.all(1, "#8B9DDE")
            self._card.content.update()

        else:
            for __ in range(50):
                self._card.elevation -= 1
                self._card.update()

            self._card.content.border = ft.border.all(0, "#00000000")
            self._card.content.update()


    def build_card(self, odd_row: bool) -> ft.Card:
        """
        Construye una tarjeta de producto a partir de un objeto de la clase :class:`Product`.

        Contiene el nombre del producto, su precio y su imagen.

        Parámetros:
            - No recibe parámetros.

        Regresa:
            - :return:`card` (ft.Card): Tarjeta de producto construida.
        """

        if odd_row:
            styles["card"]["bgcolor_1"] = "#4F5467"
            styles["card"]["bgcolor_2"] = "#2F374C"
        else:
            styles["card"]["bgcolor_1"] = "#2F374C"
            styles["card"]["bgcolor_2"] = "#4F5467"

        name: ft.Container = ft.Container(
            height = styles["name"]["height"],
            alignment = ft.alignment.center,
            content = ft.Text(
                self._product.name,
                font_family = styles["name"]["font"],
                size = styles["name"]["font_size"],
                color = styles["name"]["font_color"],
                weight = ft.FontWeight.W_500,
                text_align = ft.TextAlign.CENTER,
                no_wrap = True
            )
        )

        price: ft.Container = ft.Container(
            height = styles["price"]["height"],
            alignment = ft.alignment.center,
            content = ft.Text(
                f"${self._product.price}",
                font_family = styles["price"]["font"],
                size = styles["price"]["font_size"],
                color = styles["price"]["font_color"],
                weight = ft.FontWeight.W_300
            )
        )

        image: ft.Container = ft.Container(
            height = styles["image"]["height"],
            alignment = ft.alignment.center,
            content = ft.Image(
                width = styles["image"]["width"],
                height = styles["image"]["height"],
                src = self._product.image
            )
        )

        card_content: ft.Container = ft.Container(
            width = styles["card"]["width"],
            height = styles["card"]["height"],
            padding = styles["card"]["padding"],
            bgcolor = styles["card"]["bgcolor_2"] if self._product.id % 2 == 0 else styles["card"]["bgcolor_1"],
            animate = ft.animation.Animation(500, ft.AnimationCurve.EASE_OUT),
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
            on_hover = lambda _: self._card_on_hover(_)
        )

        self._card = ft.Card(
            elevation = 0,
            color = styles["card"]["hover_color"],
            shadow_color = styles["card"]["shadow_color"],
            surface_tint_color = styles["card"]["tint_color"],
            content = card_content
        )

        return self._card


    def build_simple_card(self) -> ft.Card:
        """
        Construye una tarjeta de producto a partir de un objeto de la clase :class:`Product`.

        Versión simplificada de la tarjeta de producto, contiene únicamente el nombre del producto, precio
        y la cantidad del producto en el carrito, así como un botón para eliminar el producto del carrito.

        Parámetros:
            - No recibe parámetros.

        Regresa:
            - :return:`simple_card` (ft.Card): Tarjeta de producto simplificada construida.
        """

