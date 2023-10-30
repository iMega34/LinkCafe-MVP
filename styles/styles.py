
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
            },
            "ticket_card" : {
                "height" : 75,
                "padding" : 10,
                "text_field_width" : 50,
                "text_field_border_radius" : 15,
                "text_field_font_size" : 18,
                "text_field_bgcolor" : "#302C30",
                "text_field_border_color" : "#00000000",
                "remove_button_size" : 40,
                "name_width" : 300,
                "price_width" : 100,
                "border_radius" : 25,
                "font_size" : 28,
                "font" : "Arbutus Slab",
                "font_color" : "#FFFFFF",
                "button_color" : "#FFFFFF",
                "remove_button_color" : "#FF0000",
                "color" : "#202026",
                "hover_color" : "#25242B",
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
                "height" : 420,
                "spacing" : 1
            },
            "card" : {
                "width" : 700,
                "height" : 750,
                "padding" : 25,
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
            "search_bar" : {
                "width" : 840,
                "border_radius" : 25,
                "bgcolor" : "#1C1E24",
                "font" : "Arbutus Slab",
                "font_size" : 35,
                "hint_size" : 25,
                "font_color" : "#FFFFFF",
                "border_color" : "#404040",
            },
            "customer_type" : {
                "width" : 840,
                "height" : 100,
                "bgcolor" : "#1C1E24",
                "font" : "Arbutus Slab",
                "font_color" : "#FFFFFF",
                "font_size" : 25,
                "label_size" : 20,
                "border_radius" : 15,
                "border_color" : "#404040",
            },
            "subtitle" : {
                "font" : "Arbutus Slab",
                "font_size" : 35,
                "font_color" : "#FFFFFF",
                "divider_color" : "#2F374C"
            },
            "total" : {
                "font" : "Arbutus Slab",
                "font_size" : 35,
                "font_color" : "#FFFFFF"
            },
            "button" : {
                "width" : 300,
                "height" : 65,
                "border_radius" : 50,
                "font_size" : 35,
                "font" : "Arbutus Slab",
                "font_color" : "#FFFFFF",
                "cancel_color" : "#FF3131",
                "send_color" : "#00BF63",
                "hover_color" : "#1F2129",
                "tint_color" : "#404040",
                "shadow_color" : "#656565"
            },
            "product_list" : {
                "width" : 650,
                "height" : 365,
                "border_radius" : 25,
                "color" : "#292830",
                "border_color" : "#404040",
            },
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