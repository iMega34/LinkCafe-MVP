
import flet as ft

from styles.styles import Styles


# Propiedades de estilo de la página de inicio, se obtienen de la clase
# Styles del archivo styles.py
styles: dict[str] = Styles.home_styles()

class SHome:
    """
    Propiedades de los controles utilizados por la función :function:`Home`
    del archivo :file:`welcome.py` para la creación de la página de inicio.
    """

    def _cashier_button_on_hover(self, _: ft.Container) -> None:
        """
        Permite al botón elevarse al pasar el cursor sobre él
        """

        if _.data == "true":
            for __ in range(30):
                self._cashier_button.elevation += 1
                self._cashier_button.update()
        else:
            for __ in range(30):
                self._cashier_button.elevation -= 1
                self._cashier_button.update()


    def _cashier_button_on_click(self, page: ft.Page, _: ft.ControlEvent) -> None:
        """
        Permite dirigirse a la vista de caja al dar clic sobre el botón y regresa el botón a su estado
        original
        """

        self._cashier_button.elevation = 0

        page.go("/cashier")


    def _orders_button_on_hover(self, _: ft.Container) -> None:
        """
        Permite al botón elevarse al pasar el cursor sobre él
        """

        if _.data == "true":
            for __ in range(30):
                self._orders_button.elevation += 1
                self._orders_button.update()
        else:
            for __ in range(30):
                self._orders_button.elevation -= 1
                self._orders_button.update()


    def _orders_button_on_click(self, page: ft.Page, _: ft.ControlEvent) -> None:
        """
        Permite dirigirse a la vista de órdenes al dar clic sobre el botón y regresa el botón a su estado
        original
        """

        self._orders_button.elevation = 0

        page.go("/orders")


    def welcome() -> ft.Container:
        """
        Bienvenida a la página

        Regresa un objeto de la clase :class:`ft.Container`
        """

        welcome_content: ft.Container = ft.Container(
            height = styles["welcome"]["height"],
            alignment = ft.alignment.center,
            content = ft.Text(
                "¡Hola, que tengas un excelente día!",
                font_family = styles["welcome"]["font"],
                size = styles["welcome"]["font_size"],
                color = styles["welcome"]["font_color"],
                weight = ft.FontWeight.W_300,
                text_align = ft.TextAlign.CENTER
            )
        )

        return welcome_content


    def logo() -> ft.Container:
        """
        Logo de la empresa

        Regresa un objeto de la clase :class:`ft.Container`
        """

        logo_content: ft.Container = ft.Container(
            width = styles["logo"]["width"],
            height = styles["logo"]["height"],
            alignment = ft.alignment.center,
            content = ft.Image(
                src = "logo.png",
            )
        )

        return logo_content


    def cashier_button(self, page: ft.Page) -> ft.Card:
        """
        Botón hacia a la vista de caja

        Recibe un objeto de la clase :class:`ft.Page` para poder
        realizar el redireccionamiento de vistas

        Regresa un objeto de la clase :class:`ft.Card`
        """

        self._cashier_button_content: ft.Container = ft.Container(
            width = styles["button"]["button_width"],
            height = styles["button"]["button_height"],
            bgcolor = styles["button"]["color"],
            border_radius = ft.border_radius.all(styles["button"]["border_radius"]),
            alignment = ft.alignment.center,
            content = ft.Text(
                "Caja",
                font_family = styles["button"]["font"],
                size = styles["button"]["font_size"],
                color = styles["button"]["font_color"],
                weight = ft.FontWeight.W_300,
                text_align = ft.TextAlign.CENTER
            ),
            on_hover = lambda _: self._cashier_button_on_hover(_),
            on_click = lambda _: self._cashier_button_on_click(page, _)
        )

        self._cashier_button: ft.Card = ft.Card(
            elevation = 0,
            color = styles["button"]["hover_color"],
            shadow_color = styles["button"]["shadow_color"],
            surface_tint_color = styles["button"]["tint_color"],
            content = self._cashier_button_content,
        )

        return self._cashier_button
    

    def orders_button(self, page: ft.Page) -> ft.Card:
        """
        Botón hacia a la vista de órdenes

        Recibe un objeto de la clase :class:`ft.Page` para poder
        realizar el redireccionamiento de vistas

        Regresa un objeto de la clase :class:`ft.Card`
        """

        self._orders_button_content: ft.Container = ft.Container(
            width = styles["button"]["button_width"],
            height = styles["button"]["button_height"],
            bgcolor = styles["button"]["color"],
            border_radius = ft.border_radius.all(styles["button"]["border_radius"]),
            alignment = ft.alignment.center,
            content = ft.Text(
                "Comandas",
                font_family = styles["button"]["font"],
                size = styles["button"]["font_size"],
                color = styles["button"]["font_color"],
                weight = ft.FontWeight.W_300,
                text_align = ft.TextAlign.CENTER
            ),
            on_hover = lambda _: self._orders_button_on_hover(_),
            on_click = lambda _: self._orders_button_on_click(page, _)
        )

        self._orders_button: ft.Card = ft.Card(
            elevation = 0,
            color = styles["button"]["hover_color"],
            shadow_color = styles["button"]["shadow_color"],
            surface_tint_color = styles["button"]["tint_color"],
            content = self._orders_button_content,
        )

        return self._orders_button
