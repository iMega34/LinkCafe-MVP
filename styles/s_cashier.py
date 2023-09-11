
import flet as ft

from styles.styles import Styles


# Propiedades de estilo de la página de caja, se obtienen de la clase
# Styles del archivo styles.py
styles: dict[str] = Styles.cashier_styles()


class SCashier:
    """
    Propiedades de los controles utilizados por la función :function:`Cashier`
    del archivo :file:`cashier.py` para la creación de la página de caja.
    """

    def _title() -> ft.Container:
        """
        Título del cuadro de resumen.

        Regresa un objeto de la clase :class:`ft.Container`
        """

        title_content: ft.Container = ft.Container(
            content = ft.Row(
                alignment = ft.MainAxisAlignment.SPACE_BETWEEN,
                controls = [
                    ft.Text(
                        "Caja",
                        font_family = styles["title"]["font"],
                        size = styles["title"]["font_size_title"],
                        color = styles["title"]["font_color"],
                        weight = ft.FontWeight.W_300,
                        text_align = ft.TextAlign.CENTER
                    ),
                    ft.Container(
                        content = ft.TextField(
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
                    )
                ]
            )
        )

        return title_content


    def _subtitle() -> ft.Container:
        """
        Subtítulo del cuadro de resumen.

        Regresa un objeto de la clase :class:`ft.Container`
        """

        subtitle_content: ft.Container = ft.Container(
            content = ft.Column(
                controls = [
                    ft.Divider(
                        color = styles["subtitle"]["divider_color"],
                        height = 1,
                    ),
                    ft.Text(
                        "Resumen",
                        width = styles["card"]["width"],
                        font_family = styles["subtitle"]["font"],
                        size = styles["subtitle"]["font_size"],
                        color = styles["subtitle"]["font_color"],
                        weight = ft.FontWeight.W_300,
                        text_align = ft.TextAlign.CENTER
                    ),
                    ft.Divider(
                        color = styles["subtitle"]["divider_color"],
                        height = 1,
                    ),
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

        Regresa un objeto de la clase :class:`ft.Container`
        """

        # Título del cuadro de resumen y cuadro de texto para el nombre del cliente
        _title: ft.Container = SCashier._title()
        # Subtítulo del cuadro de resumen
        _subtitle: ft.Container = SCashier._subtitle()

        order_summary_content: ft.Container = ft.Container(
            border = ft.border.all(1, "#FF0000"),
            padding = 25,
            width = styles["card"]["width"],
            height = styles["card"]["height"],
            bgcolor = styles["card"]["bgcolor"],
            border_radius = ft.border_radius.all(styles["card"]["border_radius"]),
            alignment = ft.alignment.center,
            content = ft.Column(
                controls = [
                    # Título del cuadro de resumen y cuadro de texto para el nombre del cliente
                    _title,
                    # Subtítulo del cuadro de resumen
                    _subtitle,
                ]
            )
        )

        return order_summary_content