
import flet as ft

from styles.styles import Styles
from other.product import Product
from other.product_list import ProductList
from other.product_card import ProductCard
from other.product_table import ProductTable


# Tabla de productos
product_table: ProductTable = ProductTable("catalogo.xlsm").get_table()
products: list[Product] = []

for index, row in product_table.iterrows():
    product: Product = Product(index, row["Nombre"], row["Precio"], row["Cantidad"], row["Imagen"], row["Información adicional"])
    products.append(product)


# Propiedades de estilo de la página de caja, se obtienen de la clase
# Styles del archivo styles.py
styles: dict[str] = Styles.cashier_styles()

# Lista de productos que se mostrarán en el resumen de la comanda
_ticket_product_list: ProductList = ProductList()

# Contenedor de la lista de productos que se mostrarán en el resumen de la comanda
# Se crea de manera global para poder acceder a él desde la clase ProductList
product_list_content: ft.Container = ft.Container(
    border = ft.border.all(1, "#FF0000"),
    width = styles["product_list"]["width"],
    height = styles["product_list"]["height"],
    content = ft.Column(
        alignment = ft.MainAxisAlignment.CENTER,
        scroll = True
    )
)


class SCashier:
    """
    Propiedades de los controles utilizados por la función :function:`Cashier`
    del archivo :file:`cashier.py` para la creación de la página de caja.
    """


    def catalog(page: ft.Page) -> ft.Container:
        """
        Catálogo de productos.

        Parámetros:
            - :param:`page` (ft.Page): Página actual.

        Regresa:
            - :return:`catalog_content` (ft.Container): Catálogo de productos.
        """

        _counter: int = 0
        _row_counter: int = 0

        # Se crea un objeto de la clase ft.ListView para contener los productos del catálogo
        list_view: ft.ListView = ft.ListView(
            spacing = styles["catalog"]["spacing"],
            width = styles["catalog"]["width_list"],
            height = styles["catalog"]["height"],
        )

        # Se crean objetos de la clase ft.Row para contener los productos del catálogo en grupos de 4
        for row in range(len(products)):
            list_row: ft.Row = ft.Row(spacing = 1)
            for product in range(4):
                try:
                    if _row_counter % 2 != 0:
                        product_card: ft.Card = ProductCard(products[_counter]).build_card(
                            True, page, product_list_content, _ticket_product_list
                        )
                    else:
                        product_card: ft.Card = ProductCard(products[_counter]).build_card(
                            False, page, product_list_content, _ticket_product_list
                        )
                    list_row.controls.append(product_card)
                    _counter += 1

                except IndexError:
                    break

            list_view.controls.append(list_row)
            _row_counter += 1

        # Se coloca el objeto list_view dentro de un objeto de la clase ft.Container
        catalog_content: ft.Container = ft.Container(
            width = styles["catalog"]["width_container"],
            alignment = ft.alignment.center,
            content = list_view,
            border = ft.border.all(1, "#FF0000"),
        )

        return catalog_content


    def _title() -> ft.Container:
        """
        Título del cuadro de resumen.

        Parámetros:
            - No recibe parámetros.

        Regresa:
            - :return:`title_content` (ft.Container): Título del cuadro de resumen.
        """

        # Título del cuadro de resumen
        _title_text: ft.Text = ft.Text(
            "Caja",
            font_family = styles["title"]["font"],
            size = styles["title"]["font_size_title"],
            color = styles["title"]["font_color"],
            weight = ft.FontWeight.W_300,
            text_align = ft.TextAlign.CENTER
        )

        # Cuadro de texto para el nombre del cliente
        _customer_name: ft.TextField = ft.TextField(
            label = "Nombre del cliente",
            label_style = ft.TextStyle(
                font_family = styles["title"]["font"],
                color = styles["title"]["font_color"],
            ),
            text_style = ft.TextStyle(
                font_family = styles["title"]["font_customer"],
                size = styles["title"]["font_size_customer"],
                color = styles["title"]["font_color"],
            ),
            border_color = styles["title"]["text_field_border_color"],
            border_radius = styles["title"]["text_field_border_radius"],
        )

        # Se coloca el título y el cuadro de texto para el nombre del cliente dentro
        # de un objeto de la clase ft.Container
        title_content: ft.Container = ft.Container(
            content = ft.Row(
                alignment = ft.MainAxisAlignment.SPACE_BETWEEN,
                controls = [
                    _title_text,
                    ft.Container(
                        content = _customer_name
                    )
                ]
            )
        )

        return title_content


    def _subtitle() -> ft.Container:
        """
        Subtítulo del cuadro de resumen.

        Parametros:
            - No recibe parámetros.

        Regresa:
            - :return:`subtitle_content` (ft.Container): Subtítulo del cuadro de resumen.
        """

        # Subtítulo del cuadro de resumen
        _subtitle_text: ft.Text = ft.Text(
            "Resumen",
            width = styles["card"]["width"],
            font_family = styles["subtitle"]["font"],
            size = styles["subtitle"]["font_size"],
            color = styles["subtitle"]["font_color"],
            weight = ft.FontWeight.W_300,
            text_align = ft.TextAlign.CENTER
        )

        # Divisor del subtítulo del cuadro de resumen
        _divider: ft.Divider = ft.Divider(
            color = styles["subtitle"]["divider_color"],
            height = 2,
        )

        # Se colocan el subtítulo y el divisor dentro de un objeto de la
        # clase ft.Container
        subtitle_content: ft.Container = ft.Container(
            content = ft.Column(
                controls = [
                    _divider,
                    _subtitle_text,
                    _divider
                ]
            )
        )

        return subtitle_content


    def order_summary() -> ft.Container:
        """
        Resumen de la comanda.

        Se muestra el total de la compra, el número de productos que se han agregado,
        la opción de enviar la comanda al Sistema Digital de Comandas (SCD) y la opción
        de cancelar la comanda.

        Parámetros:
            - No recibe parámetros.

        Regresa:
            - :return:`order_summary_content` (ft.Container): Resumen de la comanda.
        """

        # Título del cuadro de resumen y cuadro de texto para el nombre del cliente
        _title: ft.Container = SCashier._title()
        # Subtítulo del cuadro de resumen
        _subtitle: ft.Container = SCashier._subtitle()
        # Lista con el resumen de la comanda

        order_summary_content: ft.Container = ft.Container(
            border = ft.border.all(1, "#FF0000"),
            width = styles["card"]["width"],
            height = styles["card"]["height"],
            padding = styles["card"]["padding"],
            bgcolor = styles["card"]["bgcolor"],
            border_radius = ft.border_radius.all(styles["card"]["border_radius"]),
            alignment = ft.alignment.center,
            content = ft.Column(
                controls = [
                    # Título del cuadro de resumen y cuadro de texto para el nombre del cliente
                    _title,
                    # Subtítulo del cuadro de resumen
                    _subtitle,
                    # Lista con el resumen de la comanda (variable global)
                    product_list_content,
                ]
            )
        )

        return order_summary_content
