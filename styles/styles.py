
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
            "logo" : {
                "width" : 500,
                "height" : 500
            },
            "button_row" : {
                "width" : 900,
                "height" : 200,
                "spacing" : 75,
                "button_width" : 350,
                "button_height" : 100,
                "font" : "Arbutus",
                "font_size" : 40,
                "font_color" : "#FFFFFF",
            }
        }

        return home_style_dict