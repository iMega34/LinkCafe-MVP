
import pandas as pd


class ProductTable:
    """
    Contiene el método :method:`build_table` para la construcción de la tabla de productos
    a partir de un archivo de Excel, que contiene el catálogo de productos.

    El archivo de Excel debe tener la siguiente estructura:
        - Columna A: ID del producto
        - Columna B: Nombre del producto
        - Columna C: Precio del producto
        - Columna D: Precio de empleado del producto
        - Columna E: Precio de socio del producto
        - Columna F: Cantidad de productos en existencia
        - Columna G: Dirección de la imagen del producto
        - Columna H: Información adicional del producto

    El archivo de Excel debe tener el nombre :file:`catalogo.xlsm` y debe estar en la raíz del proyecto.

    Esta clase es de suma importancia pues es la base para el funcionamiento de la aplicación.
    """

    def __init__(self, spreadsheet_file: str) -> None:
        """
        Construye la tabla de productos a partir del archivo de Excel :file:`catalogo.xlsm`.

        Parámetros:
            - :param:`spreadsheet_file` (str): Nombre del archivo de Excel que contiene el catálogo de productos.
        
        Regresa:
            - No regresa ningún valor.
        """

        self._table: pd.DataFrame = pd.DataFrame()

        self._table = pd.read_excel(spreadsheet_file)
        self._table.set_index("ID", inplace = True)
        # Previene que se muestren valores NaN en la tabla
        self._table = self._table.fillna("")


    def get_table(self) -> pd.DataFrame:
        """
        Regresa la tabla de productos construida a partir del archivo de Excel :file:`catalogo.xlsm`.

        Parámetros:
            - No recibe parámetros.

        Regresa:
            - :return:`self._table` (pd.DataFrame): Tabla de productos construida a partir del archivo de Excel :file:`catalogo.xlsm`.
        """

        return self._table
