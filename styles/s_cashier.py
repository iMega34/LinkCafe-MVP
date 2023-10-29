
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

# Nombre del cliente
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
    text_align = ft.TextAlign.END,
)

# Lista de productos que se mostrarán en el resumen de la comanda
_product_list: ProductList = ProductList()

# Contenedor de la lista de productos que se mostrarán en el resumen de la comanda
# Se crea de manera global para poder acceder a él desde la clase ProductList
_on_screen_product_list: ft.Container = ft.Container(
    width = styles["product_list"]["width"],
    height = styles["product_list"]["height"],
    content = ft.Column(
        alignment = ft.MainAxisAlignment.CENTER,
        scroll = True
    )
)

# Total de la compra
_total: ft.Container = ft.Container(
    alignment = ft.alignment.center,
    content = ft.Text(
        f"Total: ${_product_list._total}",
        width = styles["card"]["width"],
        height = 60,
        font_family = styles["total"]["font"],
        size = styles["total"]["font_size"],
        color = styles["total"]["font_color"],
        weight = ft.FontWeight.W_300,
        text_align = ft.TextAlign.CENTER
    )
)


class SCashier:
    """
    Propiedades de los controles utilizados por la función :function:`Cashier`
    del archivo :file:`cashier.py` para la creación de la página de caja.
    """

    def _button_on_hover(self, _: ft.HoverEvent, button: ft.Container) -> None:
        """
        Permite al botón elevarse al pasar el cursor sobre él

        Parámetros:
            - _: ft.HoverEvent: Evento de pasar el cursor sobre el botón.
            - button (ft.Container): Botón al que se le aplicará el efecto.

        Regresa:
            - No regresa ningún valor.
        """

        if _.data == "true":
            button.border = ft.border.all(3, "#F4FF2B")
            button.update()

        else:
            button.border = ft.border.all(3, "#00000000")
            button.update()


    def _clear_order_summary(self) -> None:
        """
        Limpia la lista de productos, el total de la compra y el nombre del cliente

        Parámetros:
            - No recibe parámetros.

        Regresa:
            - No regresa ningún valor.
        """

        _product_list.clear()
        _customer_name.value = ""
        _customer_name.update()
        _on_screen_product_list.content.controls.clear()
        _on_screen_product_list.update()
        _total.content.value = f"Total: ${_product_list._total}"
        _total.update()


    def _cancel_button_on_click(self, _: ft.ControlEvent) -> None:
        """
        Permite cancelar la comanda y regresa el botón a su estado original

        Parámetros:
            - _: ft.ControlEvent: Evento de hacer clic en el botón.
        
        Regresa:
            - No regresa ningún valor.
        """

        print(f"Comanda\t{_customer_name.value}\t{_product_list._quantity_ref_dict}")

        # Limpia la lista de productos, el total de la compra y el nombre del cliente
        self._clear_order_summary()

        print(f"Comanda cancelada\t{_customer_name.value}\t{_product_list._quantity_ref_dict}")


    def _send_button_on_click(self, _: ft.ControlEvent) -> None:
        """
        Permite enviar la comanda al SCD y regresa el botón a su estado original

        Parámetros:
            - _: ft.ControlEvent: Evento de hacer clic en el botón.

        Regresa:
            - No regresa ningún valor.
        """

        print(f"Comanda\t{_customer_name.value}\t{_product_list._quantity_ref_dict}")

        # Limpia la lista de productos, el total de la compra y el nombre del cliente
        self._clear_order_summary()

        print(f"Comanda enviada\t{_customer_name.value}\t{_product_list._quantity_ref_dict}")


    def catalog() -> ft.Container:
        """
        Catálogo de productos.

        Parámetros:
            - No recibe parámetros.

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
                            True, _on_screen_product_list, _product_list, _total
                        )
                    else:
                        product_card: ft.Card = ProductCard(products[_counter]).build_card(
                            False, _on_screen_product_list, _product_list, _total
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

        # Se coloca el título y el cuadro de texto para el nombre del cliente dentro
        # de un objeto de la clase ft.Container
        title_content: ft.Container = ft.Container(
            alignment = ft.alignment.center,
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
            alignment = ft.alignment.center,
            content = ft.Column(
                controls = [
                    _divider,
                    _subtitle_text,
                    _divider
                ]
            )
        )

        return subtitle_content


    def _buttons(self) -> ft.Container:
        """
        Botones para cancelar la comanda o enviarla al Sistema Digital de Comandas (SCD).

        Parámetros:
            - No recibe parámetros.

        Regresa:
            - :return:`buttons_content` (ft.Container): Botones para cancelar la comanda o enviarla al SCD.
        """

        # Botón para cancelar la comanda
        _cancel_button: ft.Container = ft.Container(
            width = styles["button"]["width"],
            height = styles["button"]["height"],
            bgcolor = styles["button"]["cancel_color"],
            border_radius = ft.border_radius.all(styles["button"]["border_radius"]),
            animate = ft.animation.Animation(250, ft.AnimationCurve.EASE_IN),
            alignment = ft.alignment.center,
            # Contenido del botón
            content = ft.Text(
                "Cancelar",
                font_family = styles["button"]["font"],
                size = styles["button"]["font_size"],
                color = styles["button"]["font_color"],
                weight = ft.FontWeight.W_300,
                text_align = ft.TextAlign.CENTER
            ),
            on_hover = lambda _: self._button_on_hover(_, _cancel_button),
            on_click = lambda _: self._cancel_button_on_click(_)
        )

        # Botón para enviar la comanda al Sistema Digital de Comandas (SCD)
        _send_button: ft.Container = ft.Container(
            width = styles["button"]["width"],
            height = styles["button"]["height"],
            bgcolor = styles["button"]["send_color"],
            border_radius = ft.border_radius.all(styles["button"]["border_radius"]),
            animate = ft.animation.Animation(250, ft.AnimationCurve.EASE_IN),
            alignment = ft.alignment.center,
            # Contenido del botón
            content = ft.Text(
                "Enviar",
                font_family = styles["button"]["font"],
                size = styles["button"]["font_size"],
                color = styles["button"]["font_color"],
                weight = ft.FontWeight.W_300,
                text_align = ft.TextAlign.CENTER
            ),
            on_hover = lambda _: self._button_on_hover(_, _send_button),
            on_click = lambda _: self._send_button_on_click(_)
        )

        # Se colocan los botones dentro de un objeto de la clase ft.Container
        buttons_content: ft.Container = ft.Container(
            content = ft.Row(
                alignment = ft.MainAxisAlignment.SPACE_BETWEEN,
                controls = [
                    _cancel_button,
                    _send_button
                ]
            )
        )

        return buttons_content


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
        # Botones para cancelar la comanda o enviarla al SCD
        _buttons: ft.Container = SCashier()._buttons()

        order_summary_content: ft.Container = ft.Container(
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
                    _on_screen_product_list,
                    # Total de la compra
                    _total,
                    # Botones para cancelar la comanda o enviarla al SCD
                    _buttons
                ]
            )
        )

        return order_summary_content
