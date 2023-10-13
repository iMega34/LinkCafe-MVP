
import flet as ft

_quantity_ref_dict: dict = {}


class ProductList:
    """
    Contiene los métodos para el manejo de la lista de productos.

    Requiere de objetos de la clase :class:`Product` para agregarlos a la lista de productos.
    """

    def __init__(self) -> None:
        self._product_list: list[ft.Card] = []


    def add_to_list(self, page: ft.Page, product_list_content: ft.Container, product_to_add: ft.Card) -> None:
        """
        Agrega un producto al carrito de compras y lo muestra en el resumen de la comanda.

        Utiliza los parámetros de acarreo traídos desde el archivo :file:`s_cashier.py`.

        Parámetros:
            - :param:`page` (ft.Page): Página actual.
            - :param:`product_list_content` (ft.Container): Contenedor de la lista de productos.
            - :param:`product_to_add` (ft.Card): Producto a agregar a la lista de productos.

        Regresa:
            - No regresa ningún valor.
        """

        # Se obtiene el nombre del producto a agregar
        product_to_add_name: str = product_to_add.content.content.controls[1].content.value

        # Si el producto no está en la lista, es decir, no está en la referencia de cantidades
        # se agrega a la lista y se agrega a la referencia de cantidades
        if product_to_add_name not in _quantity_ref_dict:
            _quantity_ref_dict[product_to_add_name] = 1
            self._product_list.append(product_to_add)
            product_list_content.content.controls.append(product_to_add)
        # Si el producto ya está en la lista, es decir, ya está en la referencia de cantidades
        # se actualiza la cantidad del producto en la lista y en la referencia de cantidades
        else:
            _quantity_ref_dict[product_to_add_name] += 1
            # Se recorre la lista de productos para encontrar el producto a actualizar
            for idx, product in enumerate(self._product_list):
                # Si el nombre del producto a actualizar es igual al nombre del producto a agregar
                if product.content.content.controls[1].content.value == product_to_add_name:
                    # Se actualiza la cantidad del producto en la lista del producto y la
                    # tarjeta del producto en la lista de productos
                    self._product_list.pop(idx)
                    self._product_list.insert(idx, product_to_add)
                    product_list_content.content.controls.pop(idx)
                    product_list_content.content.controls.insert(idx, product_to_add)
                    product_list_content.content.controls[idx].content.content.controls[2].content.controls[1].value = _quantity_ref_dict[product_to_add_name]
                    # Se actualiza el subtotal del producto
                    price: str = product_to_add.content.content.controls[3].content.key
                    subtotal: int = int(price) * _quantity_ref_dict[product_to_add_name]
                    product_list_content.content.controls[idx].content.content.controls[3].content.value = f"${subtotal}"
                    break

        page.update()


    def add_one(self, page: ft.Page, product_list_content: ft.Container, product_to_add_one: ft.Card) -> None:
        """
        Aumenta en uno la cantidad de un producto en la lista de productos y lo muestra en el resumen de la comanda.

        - Parámetros:
            - :param:`page` (ft.Page): Página actual.
            - :param:`product_list_content` (ft.Container): Contenedor de la lista de productos.
            - :param:`product_to_add` (ft.Card): Producto a aumentar en la lista de productos.

        - Regresa:
            - No regresa ningún valor.
        """

        # Se obtiene el nombre del producto a aumentar
        product_to_add_one_name: str = product_to_add_one.content.content.controls[1].content.value

        # Se recorre la lista de productos para encontrar el producto a aumentar
        for idx, product in enumerate(self._product_list):
            # Si el nombre del producto a aumentar es igual al nombre del producto a aumentar
            if product.content.content.controls[1].content.value == product_to_add_one_name:
                # Se aumenta en uno la cantidad del producto en la lista del producto y la
                # tarjeta del producto en la lista de productos
                _quantity_ref_dict[product_to_add_one_name] += 1
                product_list_content.content.controls[idx].content.content.controls[2].content.controls[1].value = _quantity_ref_dict[product_to_add_one_name]
                # Se actualiza el subtotal del producto
                price: str = product_to_add_one.content.content.controls[3].content.key
                subtotal: int = int(price) * _quantity_ref_dict[product_to_add_one_name]
                product_list_content.content.controls[idx].content.content.controls[3].content.value = f"${subtotal}"
                break

        page.update()


    def remove_one(self, page: ft.Page, product_list_content: ft.Container, product_to_substarct) -> None:
        """
        Reduce en uno la cantidad de un producto en la lista de productos y lo muestra en el resumen de la comanda.

        - Parámetros:
            - :param:`page` (ft.Page): Página actual.
            - :param:`product_list_content` (ft.Container): Contenedor de la lista de productos.
            - :param:`product_to_substarct` (ft.Card): Producto a reducir en la lista de productos.

        - Regresa:
            - No regresa ningún valor.
        """

        # Se obtiene el nombre del producto a reducir
        product_to_remove_one_name: str = product_to_substarct.content.content.controls[1].content.value

        # Se recorre la lista de productos para encontrar el producto a reducir
        for idx, product in enumerate(self._product_list):
            # Si el nombre del producto a reducir es igual al nombre del producto a reducir y su cantidad
            # en la lista de productos es mayor a 1
            if (product.content.content.controls[1].content.value == product_to_remove_one_name 
                and _quantity_ref_dict[product_to_remove_one_name] > 1):
                # Se reduce en uno la cantidad del producto en la lista del producto y la
                # tarjeta del producto en la lista de productos
                _quantity_ref_dict[product_to_remove_one_name] -= 1
                product_list_content.content.controls[idx].content.content.controls[2].content.controls[1].value = _quantity_ref_dict[product_to_remove_one_name]
                # Se actualiza el subtotal del producto
                price: str = product_to_substarct.content.content.controls[3].content.key
                subtotal: int = int(price) * _quantity_ref_dict[product_to_remove_one_name]
                product_list_content.content.controls[idx].content.content.controls[3].content.value = f"${subtotal}"
                break
            # Si el nombre del producto a reducir es igual al nombre del producto a reducir y su cantidad
            # en la lista de productos es menor a 1
            elif (product.content.content.controls[1].content.value == product_to_remove_one_name
                and _quantity_ref_dict[product_to_remove_one_name] == 1):
                self._product_list.pop(idx)
                product_list_content.content.controls.pop(idx)
                del _quantity_ref_dict[product_to_remove_one_name]
                break

        page.update()


    def add_from_text_field(self, page: ft.Page, product_list_content: ft.Container, product_to_add: ft.Card) -> None:
        """
        Agrega la cantidad de un producto escrito en el cuadro de texto del contador en la tarjeta del producto.

        - Parámetros:
            - :param:`page` (ft.Page): Página actual.
            - :param:`product_list_content` (ft.Container): Contenedor de la lista de productos.
            - :param:`product_to_add` (ft.Card): Producto a agregar a la lista de productos.

        - Regresa:
            - No regresa ningún valor.
        """

        # Se obtiene el nombre del producto a actualizar su cantidad
        product_to_add_name: str = product_to_add.content.content.controls[1].content.value

        # Se recorre la lista de productos para encontrar el producto a actualizar su cantidad
        for idx, product in enumerate(self._product_list):
            # Si el nombre del producto a a actualizar es igual al nombre del producto a agregar
            if product.content.content.controls[1].content.value == product_to_add_name:
                # Se actualiza la cantidad del producto en la lista del producto y la
                # tarjeta del producto en la lista de productos
                new_quantity: int = int(product_to_add.content.content.controls[2].content.controls[1].value)
                _quantity_ref_dict[product_to_add_name] = new_quantity
                product_list_content.content.controls[idx].content.content.controls[2].content.controls[1].value = _quantity_ref_dict[product_to_add_name]
                # Se actualiza el subtotal del producto
                price: str = product_to_add.content.content.controls[3].content.key
                subtotal: int = int(price) * _quantity_ref_dict[product_to_add_name]
                product_list_content.content.controls[idx].content.content.controls[3].content.value = f"${subtotal}"
                break

        page.update()


    def delete(self, page: ft.Page, product_list_content: ft.Container, product_to_remove: ft.Card) -> None:
        """
        Elimina un producto de la lista de productos y lo elimina del resumen de la comanda.

        - Parámetros:
            - :param:`page` (ft.Page): Página actual.
            - :param:`product_list_content` (ft.Container): Contenedor de la lista de productos.
            - :param:`product_to_remove` (ft.Card): Producto a eliminar de la lista de productos.

        - Regresa:
            - No regresa ningún valor.
        """

        # Se obtiene el nombre del producto a eliminar
        product_to_remove_name: str = product_to_remove.content.content.controls[1].content.value

        # Se recorre la lista de productos para encontrar el producto a eliminar
        for idx, product in enumerate(self._product_list):
            # Si el nombre del producto a eliminar es igual al nombre del producto a eliminar
            if product.content.content.controls[1].content.value == product_to_remove_name:
                # Se elimina el producto de la lista de productos, de la referencia de cantidades
                # y del resumen de la comanda
                self._product_list.pop(idx)
                product_list_content.content.controls.pop(idx)
                del _quantity_ref_dict[product_to_remove_name]
                break

        page.update()
