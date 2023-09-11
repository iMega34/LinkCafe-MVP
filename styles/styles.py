
class Styles:
    """
    Contiene las propiedades de estilo de la página web
    """

    def home_styles() -> dict[str]:
        """
        Estilos de la página de inicio

        Regresa un diccionario con las propiedades de estilo
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

        Regresa un diccionario con las propiedades de estilo
        """

        cashier_style_dict: dict[str] = {
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

        Regresa un diccionario con las propiedades de estilo
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