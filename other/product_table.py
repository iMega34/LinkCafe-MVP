
import sys
import pandas as pd


# Evita la creación de archivos .pyc, debido a problemas de arranque
# en algunas ejecuciones
sys.dont_write_bytecode = True


class ProductTable:
    """
    Contiene el método :method:`build_table` para la construcción de la tabla de productos
    a partir de un archivo de Excel, que contiene el catálogo de productos.

    El archivo de Excel debe tener la siguiente estructura:
        - Columna A: ID del producto
        - Columna B: Nombre del producto
        - Columna C: Precio del producto
        - Columna D: Cantidad de productos disponibles
        - Columna E: Dirección de la imagen del producto en assets/images
        - Columna F: Información adicional del producto como alérgenos, etc.

    El archivo de Excel debe tener el nombre :file:`catalogo.xlsx` y debe estar en la raíz del proyecto.

    Esta clase es de suma importancia pues es la base para el funcionamiento de la aplicación.
    """

    def __init__(self, spreadsheet_file: str) -> None:
        """
        Construye la tabla de productos a partir del archivo de Excel :file:`catalogo.xlsx`.

        Parámetros:
            - :param:`spreadsheet_file` (str): Nombre del archivo de Excel que contiene el catálogo de productos.
        
        Regresa:
            - :return:`None`
        """

        self._table: pd.DataFrame = pd.DataFrame()

        self._table = pd.read_excel(spreadsheet_file)
        self._table.set_index("ID", inplace = True)
        # Previene que se muestren valores NaN en la tabla
        self._table = self._table.fillna("")


    def get_table(self) -> pd.DataFrame:
        """
        Regresa la tabla de productos construida a partir del archivo de Excel :file:`catalogo.xlsx`.

        Parámetros:
            - No recibe parámetros.

        Regresa:
            - :return:`self._table` (pd.DataFrame): Tabla de productos construida a partir del archivo de Excel :file:`catalogo.xlsx`.
        """

        return self._table
