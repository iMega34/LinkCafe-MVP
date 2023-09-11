
import sys
import flet as ft

from styles.s_cashier import SCashier
from styles.styles import Styles


# Evita la creación de archivos .pyc, debido a problemas de arranque
# en algunas ejecuciones
sys.dont_write_bytecode = True


def Orders(page: ft.Page) -> ft.Column:
    """
    Página de las comandas.

    Se muestran las comandas que se han enviado al Sistema Digital de Comandas (SCD),
    cada una se puede eliminar, editar o cerrar.

    Utiliza los controles declarados en la clase :class:`SOrders` del archivo :file:`s_orders.py`

    Regresa un objeto de la clase :class:`ft.Column`
    """
