
# Proyecto de digitalización de Trigali

eTrigali. Sistema de caja, comandas y menú digital

## Descripción

El sistema consta de tres elementos principales:
  - **Caja digital**: Permite al encargado de la caja realizar las tareas de tomar órdenes de los clientes y realizar el corte de caja. La idea es automatizar la mayor cantidad de tareas posibles para que el encargado de la caja pueda realizar su trabajo de manera más eficiente. Se espera que el trabajo manual se reduzca a la toma de órdenes y el conteo de dinero en caja al cierre del local.

  - **Sistema Digital de Comandas (SDC)**: Sistema de gestión y visualización de comandas para el personal de panadería y baristas. El sistema permite visualizar las comandas traídas desde la caja en tiempo real y marcarlas como completadas, editarlas o eliminarlas.

  - **Menú digital**: Menú digital para los clientes. Al menú se podrá acceder mediante una tableta electrónica instalada a la vista de los clientes. El menú mostrará los productos disponibles con sus respectivos precios y una imagen de referencia. Además permitirá a los clientes realizar pedidos y enviarlos directamente al sistema, ya que estará vinculado al _Sistema Digital de Comandas (SDC)_. Este menú digital funcionará como un complemento al menú físico y como sistema auxiliar en momentos de alta demanda, lo que permitirá a los clientes realizar sus pedidos desde la fila y antes de llegar a la caja.

  - **Sistema de Digital de Fábrica (SDF)**: Sistema de gestión de inventario en la fábrica de Trigali. El sistema permitirá al personal de fábrica, a través del _Sistema Complementario de Recetas (SCR)_, llevar un registro de los ingredientes utilizados en la elaboración de los productos, lo que permitirá llevar un control de inventario más preciso y automatizado. Además de monitorear el inventario en tiempo real, el sistema enviará notificaciones al personal de compras cuando un ingrediente esté por agotarse, permitiendo realizar los pedidos de insumos con mayor anticipación.

  - **Sistema Complementario de Recetas (SCR)**: Aplicación complemetaria al Sistema Digital de Fábrica. El SCR permitirá al personal de fábrica llevar un registro de los insumos utilizados para la preparación de los productos de la cafetería gracias a una interfaz gráfica donde se seleccionarán las recetas de los productos a elaborar y el sistema calculará los insumos necesarios para la preparación de dichos productos. El SCR estará vinculado al _Sistema Digital de Fábrica (SDF)_, por lo que los insumos utilizados en la elaboración de los productos se descontarán automáticamente del inventario.

## Preview del sistema

#### Página de inicio - En desarrollo...

![Preview del sistema](/assets/previews/preview_inicio.png "Preview del sistema")

La página de inicio del sistema muestra un mensaje de bienvenida, un botón para acceder al sistema de caja y otro para acceder al Sistema Digital de Comandas (SDC).

#### Ventana de caja - ¡Completada!

![Preview del sistema](/assets/previews/preview_caja_v_0_3_0-alpha_final.gif "Preview del sistema")

La ventana de caja muestra el resumen de la compra del cliente y el catálogo de productos. El resumen de la compra muestra el total de la compra, los productos y sus cantidades en la comanda, el botón para enviar al SDC, el botón para cancelar la comanda y el nombre del cliente asociado a la orden. El catálogo de productos muestra los productos disponibles con su respectiva imagen, nombre y precio.

Además gestionará el inventario de productos disponibles en el local, pues se busca automatizar el proceso para el corte de caja y la disponibilidad de productos en Rappi.

#### Ventana de visualización del Sistema Digital de Comandas (SDC) - Pendiente

La ventana de visualización del SDC muestra las comandas cargadas al sistema en tiempo real. Cada comanda muestra el nombre del cliente asociado a la orden, el resumen de la orden, el botón para marcar la orden como completada, el botón para editar la orden y el botón para cancelar la orden; traerán un distintivo que indicará la proveniencia de la orden (caja, menú digital o Rappi).

#### Ventana del menú digital - Pendiente

La ventana de menú digital muestra el catálogo de productos disponibles con su respectiva imagen, nombre y precio. Cada producto cuenta con un botón para agregarlo al carrito. El carrito muestra el resumen de la compra, el botón para enviar al SDC, el botón para cancelar la comanda y el nombre del cliente asociado a la orden.

#### Ventana de corte de caja - Pendiente

La ventana de corte de caja muestra el resumen de las ventas del día: el total de efectivo en caja, el total de ventas en efectivo, el total de ventas con tarjeta, el total de ventas con Rappi, el total de ventas con menú digital y el total de ventas en general. Al finalizar el corte de caja se enviará un reporte por correo electrónico con el resumen de las ventas del día.

#### Ventana del Sistema Complementario de Recetas (SCR) - Pendiente

La ventana del SCR muestra las recetas de los productos que se elaboran en la fábrica de Trigali. Cada receta muestra el nombre del producto, la imagen de referencia, los ingredientes y sus cantidades, el botón para agregar o eliminar la receta de la lista de recetas a elaborar y el botón para enviar la lista de recetas al Sistema Digital de Fábrica (SDF).

## Presentación del proyecto

[Presentación del proyecto](https://www.canva.com/design/DAFtLa90Y5g/hfpBiFyKO_-vv-mgCCOl8Q/edit?utm_content=DAFtLa90Y5g&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton "Proyecto de digitalización de Trigali - eTrigali") en Canva.

## Registro de avances

#### v0.1.0-alpha

  - Establecida la estructura general del proyecto.
  - Creación de la página de inicio del sistema.
  - Ventana de **Caja** en proceso.

#### v0.2.0-alpha

  - Ventana de **Caja** funcional, con interacción mínima con el usuario.
  - Widgets de barra de busqueda, total de la compra, botón de envío de comanda y botón de cancelación de comanda **en proceso**.
  - Ajustes menores en la arquitetura del proyecto, así como __refactorización__ de ciertos bloques de código.

### v0.3.0-alpha

  - Ventana de **Caja** **completada**
  - Widgets de barra de busqueda, total de la compra, botón de envío de comanda y botón de cancelación de comanda **completados**.
  - Añadidos los widgets de selección de tipo de pago, selección del empleado que atiende la caja, alerta de comanda no válida y alerta de comanda enviada.

### v0.3.1-alpha

  - Conexion con la base de datos **local** mediante el uso de _MySQL_.
  - Conexion con la base de datos **en la nube** mediante el uso de _AWS_ con motor _MySQL_ **en proceso**.

### v0.3.2-alpha

  - Conexion con la base de datos **en la nube** mediante el uso de _AWS_ con motor _MySQL_ **completada**.

## Planes a futuro

  - Implementación de sistema de trazabilidad de productos accesible a los clientes mediante un código QR y basado en la tecnología _blockchain_.

## Información de contacto

- **Nombre**: Erick Daniel Ortiz Cervantes
- **Correo**: A01750495@tec.mx
