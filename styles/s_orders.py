
import sys
import flet as ft

from styles.styles import Styles


# Evita la creación de archivos .pyc, debido a problemas de arranque
# en algunas ejecuciones
sys.dont_write_bytecode = True


# Propiedades de estilo de la página de órdenes, se obtienen de la clase
# Styles del archivo styles.py
styles: dict[str] = Styles.orders_styles()

class SOrders:
    """
    Propiedades de los controles utilizados por la función :function:`Orders`
    del archivo :file:`orders.py` para la creación de la página de órdenes.
    """

    