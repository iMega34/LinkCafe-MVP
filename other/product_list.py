
import flet as ft


class ProductList:
    """
    Contiene los métodos para el manejo de la lista de productos.

    Requiere de objetos de la clase :class:`Product` para agregarlos a la lista de productos.
    """

    def __init__(self) -> None:
        self._product_list: list[ft.Card] = []
        self._quantity_ref_dict: dict[str, int] = {}
        self._total: int = 0


    def _get_product_atributes(self, product: ft.Card) -> tuple[str, str]:
        """
        Extrae el nombre y el precio de un producto y los regresa en una tupla.

        Parámetros:
            - :param:`product` (ft.Card): Producto del cual se extraerán los atributos.

        Regresa:
            - :return:`product_atributes` (tuple[str, str]): Tupla con el nombre y el precio del producto.
        """

        product_name: str = product.content.content.controls[1].content.value
        product_price: str = product.content.content.controls[3].content.key

        return product_name, product_price


    def _calculate_total(self) -> None:
        """
        Calcula el total de la comanda.

        - Parámetros:
            - No recibe parámetros.

        - Regresa:
            - No regresa ningún valor.
        """

        # Se calcula el total de la comanda sumando los subtotales de cada producto
        # en el diccionario de referencia de cantidades
        total = sum(
            int(product.content.content.controls[3].content.value.replace("$", ""))
            for product in self._product_list
        )

        self._total = total


    def _add_it(self, product_list_content: ft.Container, product: ft.Card, name: str, price: str) -> None:
        """
        Función añadir para agregar un producto a la lista de productos.

        - Parámetros:
            - :param:`product_list_content` (ft.Container): Contenedor de la lista de productos.
            - :param:`product` (ft.Card): Producto a añadir a la lista de productos.
            - :param:`name` (str): Nombre del producto a actualizar.
            - :param:`price` (str): Precio del producto a actualizar.

        - Regresa:
            - No regresa ningún valor.
        """

        # Se obtiene la cantidad del producto a actualizar, si no existe se crea
        # y se le asigna el valor de 1
        self._quantity_ref_dict[name] = self._quantity_ref_dict.get(name, 0) + 1
        # Se obtiene el índice del producto a actualizar, si no existe se asigna None
        product_index: int | None = next(
            (index for (index, product) in enumerate(self._product_list) if product.content.content.controls[1].content.value == name),
            None
        )

        # Si el producto ya está en la lista, es decir, ya está en la referencia de cantidades
        # se actualiza la cantidad del producto en la lista y en la referencia de cantidades
        if product_index is not None:
            self._product_list[product_index] = product
            product_list_content.content.controls[product_index] = product
            product_list_content.content.controls[product_index].content.content.controls[2].content.controls[1].value = self._quantity_ref_dict[name]
            # Se actualiza el subtotal del producto
            subtotal: int = int(price) * self._quantity_ref_dict[name]
            product_list_content.content.controls[product_index].content.content.controls[3].content.value = f"${subtotal}"
        # Si el producto no está en la lista, es decir, no está en la referencia de cantidades
        # se agrega a la lista y se agrega a la referencia de cantidades
        else:
            self._product_list.append(product)
            product_list_content.content.controls.append(product)

        # Se actualiza el total de la comanda
        self._calculate_total()


    def _add_it_from_text_field(self, product_list_content: ft.Container, product: ft.Card, name: str, price: str) -> None:
        """
        Función auxiliar para añadir una cantidad de un producto a la lista de productos.

        - Parámetros:
            - :param:`product_list_content` (ft.Container): Contenedor de la lista de productos.
            - :param:`product` (ft.Card): Producto a actualizar en la lista de productos.
            - :param:`name` (str): Nombre del producto a actualizar.
            - :param:`price` (str): Precio del producto a actualizar.

        - Regresa:
            - No regresa ningún valor.
        """

        # Se obtiene el índice del producto a actualizar, si no existe se asigna None
        product_index: int | None = next(
            (index for (index, product) in enumerate(self._product_list) if product.content.content.controls[1].content.value == name),
            None
        )

        # Se actualiza la cantidad del producto en la lista del producto y la
        # tarjeta del producto en la lista de productos
        if product_index is not None:
            try:
                new_quantity: int = int(product.content.content.controls[2].content.controls[1].value)
                # Si la cantidad del producto a actualizar es menor a 1, se elimina el producto
                if new_quantity < 1:
                    self._delete_it(product_list_content, name)
                # Si la cantidad del producto a actualizar es mayor a 1, se actualiza la cantidad
                else:
                    self._quantity_ref_dict[name] = new_quantity
                    product_list_content.content.controls[product_index].content.content.controls[2].content.controls[1].value = self._quantity_ref_dict[name]
                    # Se actualiza el subtotal del producto
                    subtotal: int = int(price) * self._quantity_ref_dict[name]
                    product_list_content.content.controls[product_index].content.content.controls[3].content.value = f"${subtotal}"
            except ValueError:
                pass

        # Se actualiza el total de la comanda
        self._calculate_total()


    def _reduce_quantity(self, product_list_content: ft.Container, name: str, price: str) -> None:
        """
        Función auxiliar para reducir en uno un producto de la lista de productos.

        - Parámetros:
            - :param:`product_list_content` (ft.Container): Contenedor de la lista de productos.
            - :param:`name` (str): Nombre del producto a actualizar.
            - :param:`price` (str): Precio del producto a actualizar.

        - Regresa:
            - No regresa ningún valor.
        """

        # Se obtiene el índice del producto a actualizar, si no existe se asigna None
        product_index: int | None = next(
            (index for (index, product) in enumerate(self._product_list) if product.content.content.controls[1].content.value == name),
            None
        )

        if product_index is not None:
            # Si la cantidad del producto a actualizar es mayor a 1, se reduce en uno
            # la cantidad del producto en la lista y en la referencia de cantidades
            if self._quantity_ref_dict[name] > 1:
                self._quantity_ref_dict[name] -= 1
                product_list_content.content.controls[product_index].content.content.controls[2].content.controls[1].value = self._quantity_ref_dict[name]
                # Se actualiza el subtotal del producto
                subtotal: int = int(price) * self._quantity_ref_dict[name]
                product_list_content.content.controls[product_index].content.content.controls[3].content.value = f"${subtotal}"
            # Si la cantidad del producto a actualizar es igual a 1, se elimina el producto
            # de la lista y de la referencia de cantidades
            elif self._quantity_ref_dict[name] == 1:
                self._delete_it(product_list_content, name)

        # Se actualiza el total de la comanda
        self._calculate_total()


    def _delete_it(self, product_list_content: ft.Container, name: str) -> None:
        """
        Función auxiliar para eliminar un producto de la lista de productos.

        - Parámetros:
            - :param:`product_list_content` (ft.Container): Contenedor de la lista de productos.
            - :param:`name` (str): Nombre del producto a eliminar.

        - Regresa:
            - No regresa ningún valor.
        """

        # Se obtiene el índice del producto a eliminar, si no existe se asigna None
        product_idx: int | None = next(
            (idx for (idx, product) in enumerate(self._product_list) if product.content.content.controls[1].content.value == name),
            None
        )

        if product_idx is not None:
            # Se elimina el producto de la lista de productos, de la referencia de cantidades
            # y del resumen de la comanda
            self._product_list.pop(product_idx)
            product_list_content.content.controls.pop(product_idx)
            del self._quantity_ref_dict[name]

        # Se actualiza el total de la comanda
        self._calculate_total()


    def add_to_list(self, product_list_content: ft.Container, product: ft.Card, total: ft.Container) -> None:
        """
        Añade un producto a la lista de productos y lo muestra en el resumen de la comanda.

        Utiliza los parámetros de acarreo traídos desde el archivo :file:`s_cashier.py`.

        Parámetros:
            - :param:`product_list_content` (ft.Container): Contenedor de la lista de productos.
            - :param:`product_to_add` (ft.Card): Producto a agregar a la lista de productos.
            - :param:`total` (ft.Container): Contenedor del total de la comanda.

        Regresa:
            - No regresa ningún valor.
        """

        # Se obtiene el nombre del producto a agregar
        name, price = self._get_product_atributes(product)

        # Se llama al método auxiliar para agregar el producto a la lista de productos
        self._add_it(product_list_content, product, name, price)

        # Se actualiza el total de la comanda
        total.content.value = f"Total: ${self._total}"

        product_list_content.update()
        total.update()


    def add_from_text_field(self, product_list_content: ft.Container, product: ft.Card, total: ft.Container) -> None:
        """
        Agrega la cantidad de un producto escrito en el cuadro de texto del contador en la tarjeta del producto.

        - Parámetros:
            - :param:`page` (ft.Page): Página actual.
            - :param:`product_list_content` (ft.Container): Contenedor de la lista de productos.
            - :param:`product_to_add` (ft.Card): Producto a agregar a la lista de productos.
            - :param:`total` (ft.Container): Contenedor del total de la comanda.

        - Regresa:
            - No regresa ningún valor.
        """

        # Se obtiene el nombre del producto a actualizar su cantidad
        name, price = self._get_product_atributes(product)

        # Se llama al método auxiliar para agregar la cantidad del producto
        self._add_it_from_text_field(product_list_content, product, name, price)

        # Se actualiza el total de la comanda
        total.content.value = f"Total: ${self._total}"

        product_list_content.update()
        total.update()


    def reduce_one(self, product_list_content: ft.Container, product: ft.Card, total: ft.Container) -> None:
        """
        Reduce en uno la cantidad de un producto en la lista de productos y lo muestra en el resumen de la comanda.

        - Parámetros:
            - :param:`product_list_content` (ft.Container): Contenedor de la lista de productos.
            - :param:`product_to_substarct` (ft.Card): Producto a reducir en la lista de productos.
            - :param:`total` (ft.Container): Contenedor del total de la comanda.

        - Regresa:
            - No regresa ningún valor.
        """

        # Se obtiene el nombre del producto a reducir
        name, price = self._get_product_atributes(product)

        # Se llama al método auxiliar para reducir en uno la cantidad del producto
        self._reduce_quantity(product_list_content, name, price)

        # Se actualiza el total de la comanda
        total.content.value = f"Total: ${self._total}"

        product_list_content.update()
        total.update()


    def delete(self, product_list_content: ft.Container, product: ft.Card, total: ft.Container) -> None:
        """
        Elimina un producto de la lista de productos y lo elimina del resumen de la comanda.

        - Parámetros:
            - :param:`product_list_content` (ft.Container): Contenedor de la lista de productos.
            - :param:`product_to_remove` (ft.Card): Producto a eliminar de la lista de productos.
            - :param:`total` (ft.Container): Contenedor del total de la comanda.

        - Regresa:
            - No regresa ningún valor.
        """

        # Se obtiene el nombre del producto a eliminar
        name, _= self._get_product_atributes(product)

        # Se llama al método auxiliar para eliminar el producto de la lista de productos
        self._delete_it(product_list_content, name)

        # Se actualiza el total de la comanda
        total.content.value = f"Total: ${self._total}"

        product_list_content.update()
        total.update()


    def clear(self) -> None:
        """
        Limpia la lista de productos y la referencia de cantidades.

        - Parámetros:
            - No recibe parámetros.

        - Regresa:
            - No regresa ningún valor.
        """

        self._product_list.clear()
        self._quantity_ref_dict.clear()
        self._total = 0
