
class Product:
    """
    Crea objetos Producto que contienen la información de un producto en el
    catálogo de productos. El catálogo de productos se obtiene de el archivo
    :file:`catalogo.xlsx`.

    El objeto Producto contiene la siguiente información:
        - id: Identificador del producto
        - name: Nombre del producto
        - price: Precio del producto
        - quantity: Cantidad de productos disponibles
        - image: Dirección de la imagen del producto en assets/images
        - additional_info: Información adicional del producto como alérgenos, etc.
    """

    def __init__(self, id: int, name: str, price: int, quantity: int, image: str, additional_info: str) -> None:
        """
        Construye un objeto Producto con la información proporcionada.

        Parámetros:
            - :param:`id` (int): Identificador del producto
            - :param:`name` (str): Nombre del producto
            - :param:`price` (int): Precio del producto
            - :param:`quantity` (int): Cantidad de productos disponibles
            - :param:`image` (str): Dirección de la imagen del producto en assets/images
            - :param:`additional_info` (str): Información adicional del producto como alérgenos, etc.
        """

        self.id: int = id
        self.name: str = name
        self.price: int = price
        self.quantity: int = quantity
        self.image: str = image
        self.additional_info: str = additional_info
