
from mysql.connector import MySQLConnection, connect
from mysql.connector.cursor import MySQLCursor
from time import strftime


class DBConnection:
    """
    Contiene los métodos para la conexión con la base de datos

    Requiere una conexión a internet para poder conectarse con la base de
    datos en AWS.
    """

    def __init__(self) -> None:
        # Host y contraseña de la base de datos
        self.__host, self.__password = self._get_db_info()
        # Atributos privados
        self.__database: MySQLConnection = connect(
            host = self.__host,
            user = "admin",
            password = self.__password,
            database = "test_database"
        )
        # Atributos protegidos
        self._cursor: MySQLCursor = self.__database.cursor()
        self._employees: list[str] = []
        self._order_to_send: list = []


    def _get_db_info(self) -> tuple[str]:
        """
        Obtiene la información de la base de datos

        Parámetros:
            - No recibe parámetros.

        Regresa:
            - :return:`db_info` (tuple[str]): Tupla con la información de la base de datos
        """

        with open("other/db_info.txt", "r") as file:
            db_info: tuple[str] = tuple(file.read().splitlines())

        return db_info


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

        # Obtiene la fecha y hora actual
        date: str = strftime("%d/%b/%Y")
        time: str = strftime("%H:%M:%S")

        sql: str = "INSERT INTO orders (customer_name, products_n_quantities, total, employee, active, date, hour) VALUES (%s, %s, %s, %s, 1, %s, %s)"
        values: tuple[str] = (order["customer_name"], products_and_quantities_str, order["total"], order["employee"], date, time)

        # Envía la orden a la base de datos
        self._cursor.execute(sql, values)
        self.__database.commit()


    def get_orders(self) -> dict[str, list]:
        """
        Obtiene las órdenes de la base de datos

        Parámetros:
            - No recibe parámetros.

        Regresa:
            - :return:`orders` (dict[str, list]): Diccionario con las órdenes, con
            el formato ``{id : {name, products_n_quantities, total, origin}}``
        """

        # Obtiene las órdenes de la base de datos
        self._cursor.execute("SELECT * FROM orders")
        db_rows: list[tuple[str]] = self._cursor.fetchall()

        orders: dict[str, list] = {}

        # Se crea un diccionario con las órdenes
        for order in db_rows:
            id, name, products_n_quantities, total, origin = order[0], order[1], order[2], order[3], order[5]
            products_n_quantities_list: list[str] = products_n_quantities.split(", ")
            products_n_quantities_dict: dict[str, str] = {}

            # Se crea un diccionario con los productos y cantidades de la orden
            for product in products_n_quantities_list:
                product_name, product_quantity = product.split(" x ")
                products_n_quantities_dict[product_name] = product_quantity

            # Se agrega la orden al diccionario de órdenes
            orders[id] = {
                "name" : name,
                "products_n_quantities" : products_n_quantities_dict,
                "total" : total,
                "origin" : origin
            }

        return orders