
from mysql.connector import MySQLConnection, connect
from mysql.connector.cursor import MySQLCursor


class DBConnection:
    """
    Contiene los métodos para la conexión con la base de datos

    Requiere una conexión a internet para poder conectarse con la base de
    datos en AWS.
    """

    def __init__(self) -> None:
        # Atributos privados
        self.__database: MySQLConnection = connect(
            host = "localhost",
            user = "root",
            password = self._get_db_password(),
            database = "trigali_test_database"
        )
        # Atributos protegidos
        self._cursor: MySQLCursor = self.__database.cursor()
        self._employees: list[str] = []
        self._order_to_send: list = []


    def _get_db_password(self) -> str:
        """
        Obtiene la contraseña de la base de datos

        Parámetros:
            - No recibe parámetros.

        Regresa:
            - :return:`password` (str): Contraseña de la base de datos
        """

        with open("other/db_password.txt", "r") as file:
            password: str = file.read()

        return password


    def get_employees(self) -> list[str]:
        """
        Obtiene los empleados activos de la base de datos

        Parámetros:
            - No recibe parámetros.

        Regresa:
            - :return:`self._employees` (list[str]): Lista con los nombres de los empleados activos
        """

        self._cursor.execute("SELECT name, active FROM employees")

        employees_list: list[str, int] = self._cursor.fetchall()

        for employee in employees_list:
            name, active = employee
            if active:
                self._employees.append(name)

        return self._employees
    

    def send_order_to_db(self, order: dict[str]) -> None:
        """
        Envía la comanda a la base de datos

        Parámetros:
            - :param:`order` (dict[str]): Diccionario con los datos de la comanda

        Regresa:
            - No regresa ningún valor.
        """

        products_and_quantities_str: str = ""

        # Convierte el diccionario de referencia de cantidades en un string
        for product, quantity in order["products_and_quantities"].items():
            products_and_quantities_str += f"{product} x {quantity}, "
        else:
            products_and_quantities_str = products_and_quantities_str[0:products_and_quantities_str.rfind(", ")]

        sql: str = "INSERT INTO orders (customer_name, products_n_quantities, total, employee, active) VALUES (%s, %s, %s, %s, 1)"
        values: tuple[str] = (order["customer_name"], products_and_quantities_str, order["total"], order["employee"])

        # Envía la orden a la base de datos
        self._cursor.execute(sql, values)
        self.__database.commit()
