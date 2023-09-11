
import sys


# Evita la creación de archivos .pyc, debido a problemas de arranque
# en algunas ejecuciones
sys.dont_write_bytecode = True


class Styles:
    """
    Contiene las propiedades de estilo de la página web
    """

    def product_styles() -> dict[str]:
        """
        Estilos de los compoenentes de productos

        Parámetros:
            - No recibe parámetros.

        Regresa:
            - :return:`product_style_dict` (dict[str]): Diccionario con las propiedades de estilo
        """

        product_style_dict: dict[str] = {
            "name" : {
                "height" : 30,
                "font" : "Arbutus Slab",
                "font_size" : 18,
                "font_color" : "#FFFFFF"
            },
            "price" : {
                "height" : 30,
                "font" : "Arbutus Slab",
                "font_size" : 22,
                "font_color" : "#FFFFFF"
            },
            "image" : {
                "width" : 100,
                "height" : 100
            },
            "card" : {
                "width" : 200,
                "height" : 200,
                "width_container" : 180,
                "height_container" : 180,
                "padding" : 10,
                "bgcolor_1" : "#2F374C",
                "bgcolor_2" : "#4F5467",
                "hover_color" : "#1F2129",
                "tint_color" : "#404040",
                "shadow_color" : "#656565",
            }
        }

        return product_style_dict


    def home_styles() -> dict[str]:
        """
        Estilos de la página de inicio

        Parámetros:
            - No recibe parámetros.

        Regresa:
            - :return:`home_style_dict` (dict[str]): Diccionario con las propiedades de estilo
        """

        home_style_dict: dict[str] = {
            "welcome" : {
                "height" : 100,
                "font" : "Tenor Sans",
                "font_size" : 50,
                "font_color" : "#FFFFFF"
            },
            "logo" : {
                "width" : 700,
                "height" : 375
            },
            "button_row" : {
                "width" : 900,
                "height" : 150,
                "spacing" : 75
            },
            "button" : {
                "button_width" : 350,
                "button_height" : 100,
                "border_radius" : 25,
                "font" : "Arbutus Slab",
                "font_size" : 40,
                "font_color" : "#FFFFFF",
                "color" : "#6E1B27",
                "hover_color" : "#1F2129",
                "tint_color" : "#404040",
                "shadow_color" : "#656565",
            }
        }

        return home_style_dict


    def cashier_styles() -> dict[str]:
        """
        Estilos de la página de caja

        Parámetros:
            - No recibe parámetros.

        Regresa:
            - :return:`cashier_style_dict` (dict[str]): Diccionario con las propiedades de estilo
        """

        cashier_style_dict: dict[str] = {
            "catalog" : {
                "width_container" : 840,
                "width_list" : 835,
                "height" : 560,
                "spacing" : 1
            },
            "card" : {
                "width" : 700,
                "height" : 690,
                "border_radius" : 50,
                "bgcolor" : "#25242B",
                "font_color" : "#FFFFFF"
            },
            "title" : {
                "font" : "Tenor Sans",
                "font_customer" : "Forum",
                "font_size_title" : 70,
                "font_size_customer" : 35,
                "font_color" : "#FFFFFF",
                "text_field_border_color" : "#404040",
                "text_field_border_radius" : 25
            },
            "subtitle" : {
                "font" : "Arbutus Slab",
                "font_size" : 35,
                "font_color" : "#FFFFFF",
                "divider_color" : "#2F374C"
            }
        }

        return cashier_style_dict


    def orders_styles() -> dict[str]:
        """
        Estilos de la página de órdenes

        Parámetros:
            - No recibe parámetros.

        Regresa:
            - :return:`orders_style_dict` (dict[str]): Diccionario con las propiedades de estilo
        """

        orders_style_dict: dict[str] = {
            "title" : {
                "height" : 100,
                "font" : "Tenor Sans",
                "font_size" : 50,
                "font_color" : "#FFFFFF"
            },
            "logo" : {
                "width" : 700,
                "height" : 375
            },
            "button_row" : {
                "width" : 900,
                "height" : 150,
                "spacing" : 75
            },
            "button" : {
                "button_width" : 350,
                "button_height" : 100,
                "border_radius" : 25,
                "font" : "Arbutus Slab",
                "font_size" : 40,
                "font_color" : "#FFFFFF",
                "color" : "#6E1B27",
                "hover_color" : "#1F2129",
                "tint_color" : "#404040",
                "shadow_color" : "#656565",
            }
        }

        return orders_style_dict