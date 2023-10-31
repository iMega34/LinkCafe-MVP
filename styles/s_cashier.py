
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
    product: Product = Product(
        index,
        row["Nombre"],
        row["Precio"],
        row["Precio empleado"],
        row["Precio socio"],
        row["Cantidad"],
        row["Imagen"],
        row["Información adicional"]
    )
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
    text_align = ft.TextAlign.START,
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

# Objeto de la clase ft.ListView para contener los productos del catálogo
list_view: ft.ListView = ft.ListView(
    spacing = styles["catalog"]["spacing"],
    width = styles["catalog"]["width_list"],
    height = styles["catalog"]["height"],
    key = "Cliente"
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
            - :param:`_` (ft.HoverEvent): Evento de pasar el cursor sobre el botón.
            - :param:`button` (ft.Container): Botón al que se le aplica el evento.

        Regresa:
            - No regresa ningún valor.
        """

        if _.data == "true":
            button.border = ft.border.all(3, "#F4FF2B")
            button.update()

        else:
            button.border = ft.border.all(3, "#00000000")
            button.update()


    def _build_catalog(self) -> None:
        """
        Construye el catálogo de productos

        Parámetros:
            - No recibe parámetros.

        Regresa:
            - No regresa ningún valor.
        """

        _counter: int = 0
        _row_counter: int = 0

        # Se recorre la lista de productos y se agregan a la lista de productos
        for row in range(len(products)):
            list_row = ft.Row(spacing = 1)
            # Se agregan 4 productos por fila
            for product in range(4):
                try:
                    # Se alterna el color de fondo de las filas
                    is_odd_row: bool = _row_counter % 2 != 0
                    # Se crea la tarjeta del producto
                    product_card: ft.Card = ProductCard(products[_counter]).build_card(
                        is_odd_row, _on_screen_product_list, _product_list, _total, list_view.key
                    )
                    # Se agregan los productos a la lista de productos y aumenta el contador
                    list_row.controls.append(product_card)
                    _counter += 1

                # Si se llega al final de la lista de productos, se termina el ciclo
                except IndexError:
                    break

            # Se agregan las filas a la lista de productos
            list_view.controls.append(list_row)
            _row_counter += 1


    def _show_products(self, _: ft.ControlEvent, query: str) -> None:
        """
        Muestra los productos en el catálogo de productos

        Si se ingresa texto en la barra de búsqueda, se muestran los productos que
        coincidan con el texto ingresado, si no se ingresa texto en la barra de búsqueda
        se muestran todos los productos.

        Parámetros:
            - :param:`_` (ft.ControlEvent): Evento de cambio en el texto de la barra de búsqueda.
            - :param:`query` (str): Texto ingresado en la barra de búsqueda.

        Regresa:
            - No regresa ningún valor.
        """

        # Se limpia la lista de productos
        list_view.controls.clear()

        _counter: int = 0
        _row_counter: int = 0

        # Se recorre la lista de productos y se agregan a la lista de productos
        for row in range(len(products)):
            list_row = ft.Row(spacing = 1)
            # Se agregan 4 productos por fila
            for product in range(4):
                try:
                    # Se alterna el color de fondo de las filas
                    is_odd_row: bool = _row_counter % 2 != 0
                    # Se crea la tarjeta del producto
                    product_card: ft.Card = ProductCard(products[_counter]).build_card(
                        is_odd_row, _on_screen_product_list, _product_list, _total, list_view.key
                    )
                    # Se agregan los productos a la lista de productos solo si coinciden
                    # con el texto ingresado
                    if query.capitalize() in products[_counter].name:
                        list_row.controls.append(product_card)
                    _counter += 1

                # Si se llega al final de la lista de productos, se termina el ciclo
                except IndexError:
                    break

            # Se agregan las filas a la lista de productos
            list_view.controls.append(list_row)
            _row_counter += 1

        # Se actualiza la lista de productos
        list_view.update()


    def _apply_customer_type_discount(self, _: ft.ControlEvent, customer_type: str) -> None:
        """
        Aplica el descuento correspondiente al tipo de cliente y actualiza el catálogo de productos

        Parámetros:
            - :param:`_` (ft.ControlEvent): Evento de cambio en el tipo de cliente.
            - :param:`customer_type` (str): Tipo de cliente.

        Regresa:
            - No regresa ningún valor.
        """

        # Se limpia la lista de productos y se actualiza el tipo de cliente
        list_view.controls.clear()
        list_view.key = customer_type

        # Se aplica el descuento correspondiente al tipo de cliente y 
        # se muestran los nuevos precios
        self._build_catalog()

        # Se actualiza la lista de productos
        list_view.update()


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
            - :param:`_` (ft.ControlEvent): Evento de hacer clic en el botón.

        Regresa:
            - No regresa ningún valor.
        """

        # Limpia la lista de productos, el total de la compra y el nombre del cliente
        self._clear_order_summary()


    def _open_alert(self, page: ft.Page, alert: ft.AlertDialog) -> None:
        """
        Abre el cuadro de alerta

        Parámetros:
            - :param:`page` (ft.Page): Página actual.
            - :param:`alert` (ft.AlertDialog): Cuadro de alerta.

        Regresa:
            - No regresa ningún valor.
        """

        page.dialog = alert
        alert.open = True
        page.update()


    def _close_alert(self, _: ft.ControlEvent, page: ft.Page, alert: ft.AlertDialog) -> None:
        """
        Cierra el cuadro de alerta

        Parámetros:
            - :param:`page` (ft.Page): Página actual.
            - :param:`alert` (ft.AlertDialog): Cuadro de alerta.

        Regresa:
            - No regresa ningún valor.
        """

        alert.open = False
        page.update()


    def _send_button_on_click(self, _: ft.ControlEvent, page) -> None:
        """
        Permite enviar la comanda al SCD y regresa el botón a su estado original

        Parámetros:
            - :param:`_` (ft.ControlEvent): Evento de hacer clic en el botón.
            - :param:`page` (ft.Page): Página actual.

        Regresa:
            - No regresa ningún valor.
        """

        # Se crea el cuadro de alerta
        alert: ft.AlertDialog = ft.AlertDialog(
            # Título del cuadro de alerta
            title = ft.Text(
                "No se puede enviar la comanda",
                font_family = styles["alert"]["font"],
                size = styles["alert"]["title_font_size"],
                color = styles["alert"]["font_color"],
                weight = ft.FontWeight.W_500,
                text_align = ft.TextAlign.CENTER
            ),
            # Mensaje del cuadro de alerta
            content = ft.Text(
                "Por favor, verifica que hayan productos en el resumen de la comanda, y\nque el nombre del cliente y quién esté atendiendo no estén vacíos.",
                font_family = styles["alert"]["font"],
                size = styles["alert"]["content_font_size"],
                color = styles["alert"]["font_color"],
                weight = ft.FontWeight.W_300,
                text_align = ft.TextAlign.CENTER
            ),
            # Botón para cerrar el cuadro de alerta
            actions = [
                # Botón como un objeto de la clase ft.Container
                ft.Container(
                    width = styles["alert"]["button_width"],
                    bgcolor = styles["alert"]["bgcolor"],
                    border = ft.border.all(0, styles["alert"]["border_color"]),
                    border_radius = ft.border_radius.all(styles["alert"]["border_radius"]),
                    alignment = ft.alignment.center,
                    # Contenido del botón
                    content = ft.Text(
                        "Cerrar",
                        font_family = styles["alert"]["font"],
                        size = styles["alert"]["content_font_size"],
                        color = styles["alert"]["font_color"],
                        weight = ft.FontWeight.W_300,
                        text_align = ft.TextAlign.CENTER
                    ),
                    # Cierre del cuadro de alerta
                    on_click = lambda _: self._close_alert(_, page, alert)
                )
            ],
            # Align de los botones del cuadro de alerta -> Centro del cuadro de alerta
            actions_alignment = ft.MainAxisAlignment.CENTER
        )

        # Se verifica que haya productos en el resumen de la comanda, y que el nombre
        # del cliente y quién esté atendiendo no estén vacíos
        params_to_verify: tuple[bool, bool] = (
            not _on_screen_product_list.content.controls, _customer_name.value == ""
        )

        # Se abre el cuadro de alerta si no se cumplen las condiciones
        if any(params_to_verify):
            self._open_alert(page, alert)
        # Si se cumplen las condiciones, se envia la comanda al Sistema Digital de Comandas (SCD)
        # y se limpia la lista de productos, el total de la compra y el nombre del cliente
        else:
            self._clear_order_summary()



    def catalog_title() -> ft.Container:
        """
        Título del catálogo de productos.

        Parámetros:
            - No recibe parámetros.

        Regresa:
            - :return:`catalog_title_content` (ft.Container): Título del catálogo de productos.
        """

        catalog_title_content: ft.Container = ft.Container(
            alignment = ft.alignment.center,
            content = ft.Text(
                "Catálogo",
                width = styles["catalog"]["width_container"],
                font_family = styles["title"]["font"],
                size = styles["title"]["font_size_title"],
                color = styles["title"]["font_color"],
                weight = ft.FontWeight.W_300,
                text_align = ft.TextAlign.CENTER
            )
        )

        return catalog_title_content


    def search_bar(self) -> ft.Container:
        """
        Barra de búsqueda de productos.

        Parámetros:
            - No recibe parámetros.

        Regresa:
            - :return:`search_bar_content` (ft.Container): Barra de búsqueda de productos.
        """

        search_bar_content: ft.Container = ft.Container(
            width = styles["search_bar"]["width"],
            alignment = ft.alignment.center,
            content = ft.TextField(
                label = "Barra de busqueda",
                label_style = ft.TextStyle(
                    font_family = styles["search_bar"]["font"],
                    size = styles["search_bar"]["hint_size"],
                    color = styles["search_bar"]["font_color"],
                ),
                text_style = ft.TextStyle(
                    font_family = styles["search_bar"]["font"],
                    size = styles["search_bar"]["font_size"],
                    color = styles["search_bar"]["font_color"],
                ),
                bgcolor = styles["search_bar"]["bgcolor"],
                border_color = styles["search_bar"]["border_color"],
                border_radius = styles["search_bar"]["border_radius"],
                text_align = ft.TextAlign.START,
                # Busca los productos que coincidan con el texto ingresado
                on_change = lambda _: self._show_products(_, search_bar_content.content.value)
            )
        )

        return search_bar_content


    def catalog(self) -> ft.Container:
        """
        Catálogo de productos.

        Parámetros:
            - No recibe parámetros.

        Regresa:
            - :return:`catalog_content` (ft.Container): Catálogo de productos.
        """

        self._build_catalog()

        # Se coloca la lista de productos dentro de un objeto de la clase ft.Container
        catalog_content = ft.Container(
            width = styles["catalog"]["width_container"],
            alignment = ft.alignment.center,
            content = list_view,
        )

        return catalog_content


    def customer_type_selector(self) -> ft.Container:
        """
        Selector de tipo de cliente.

        Modifica el precio de los productos dependiendo del tipo de cliente.

        Parámetros:
            - No recibe parámetros.

        Regresa:
            - :return:`selector_content` (ft.Container): Selector de empleado o socio.
        """

        _dropdown: ft.Dropdown = ft.Dropdown(
            value = "Cliente",
            label = "Tipo de cliente",
            label_style = ft.TextStyle(
                font_family = styles["customer_type"]["font"],
                size = styles["customer_type"]["label_size"],
                color = styles["customer_type"]["font_color"],
            ),
            text_style = ft.TextStyle(
                font_family = styles["customer_type"]["font"],
                size = styles["customer_type"]["font_size"],
                color = styles["customer_type"]["font_color"],
            ),
            options = [
                ft.dropdown.Option("Cliente"),
                ft.dropdown.Option(r"Empleado - 15% descuento"),
                ft.dropdown.Option(r"Socio - 30% descuento")
            ],
            border_radius = styles["customer_type"]["border_radius"],
            bgcolor = styles["customer_type"]["bgcolor"],
            border_color = styles["customer_type"]["border_color"],
            focused_bgcolor = styles["customer_type"]["bgcolor"],
            focused_border_color = styles["customer_type"]["border_color"],
            on_change = lambda _: self._apply_customer_type_discount(_, _dropdown.value)
        )

        selector_content: ft.Container = ft.Container(
            width = styles["customer_type"]["width"],
            height = styles["customer_type"]["height"],
            alignment = ft.alignment.center,
            content = _dropdown
        )

        return selector_content


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


    def _buttons(self, page) -> ft.Container:
        """
        Botones para cancelar la comanda o enviarla al Sistema Digital de Comandas (SCD).

        Parámetros:
            - :param:`page` (ft.Page): Página actual.

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
            on_click = lambda _: self._send_button_on_click(_, page)
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


    def order_summary(page) -> ft.Container:
        """
        Resumen de la comanda.

        Se muestra el total de la compra, el número de productos que se han agregado,
        la opción de enviar la comanda al Sistema Digital de Comandas (SCD) y la opción
        de cancelar la comanda.

        Parámetros:
            - :param:`page` (ft.Page): Página actual.

        Regresa:
            - :return:`order_summary_content` (ft.Container): Resumen de la comanda.
        """

        # Título del cuadro de resumen y cuadro de texto para el nombre del cliente
        _title: ft.Container = SCashier._title()
        # Subtítulo del cuadro de resumen
        _subtitle: ft.Container = SCashier._subtitle()
        # Botones para cancelar la comanda o enviarla al SCD
        _buttons: ft.Container = SCashier()._buttons(page)

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
