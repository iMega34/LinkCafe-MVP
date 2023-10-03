
# Proyecto de digitalización de Trigali

eTrigali. Sistema de caja, comandas y menú digital

## Descripción

El sistema consta de tres elementos principales:
  - **Caja digital**: Permite al encargado de la caja realizar las tareas de tomar órdenes de los clientes y realizar el corte de caja. La idea es automatizar la mayor cantidad de tareas posibles para que el encargado de la caja pueda realizar su trabajo de manera más eficiente. Se espera que el trabajo manual se reduzca a la toma de órdenes y el conteo de dinero en caja al cierre del local.
  - **Sistema Digital de Comandas (SDC)**: Sistema de gestión y visualización de comandas para el personal de panadería y baristas. El sistema permite visualizar las comandas traídas desde la caja en tiempo real y marcarlas como completadas, editarlas o eliminarlas.
  - **Menú digital**: Menú digital para los clientes. Al menú se podrá acceder mediante un código QR desde cualquier dispositivo con acceso a Internet. El menú mostrará los productos disponibles con sus respectivos precios y una imagen de referencia. Además permitirá a los clientes realizar pedidos y enviarlos directamente al sistema, ya que estará vinculado al Sistema Digital de Comandas (SDC). Este menú digital funcionará como un complemento al menú físico y como sistema auxiliar en momentos de alta demanda, lo que permitirá a los clientes realizar sus pedidos desde sus propios dispositivos sin necesidad de esperar en la fila de la caja.

## Preview del sistema

#### Página de inicio

![Preview del sistema](/assets/images/preview_inicio.png "Preview del sistema")

La página de inicio del sistema muestra un mensaje de bienvenida, un botón para acceder al sistema de caja y otro para acceder al Sistema Digital de Comandas (SDC).

#### Página de caja - En desarrollo

![Preview del sistema](/assets/images/preview_caja.png "Preview del sistema")

La página de caja muestra el resumen de la compra del cliente y el catálogo de productos. El resumen de la compra muestra el total de la compra, el número de productos en el carrito, el botón para enviar al SDC, el botón para cancelar la comanda y el nombre del cliente asociado a la orden. El catálogo de productos muestra los productos disponibles con su respectiva imagen, nombre y precio.

Además gestionará el inventario de productos disponibles en el local, pues se busca automatizar el proceso para el corte de caja y la disponibilidad de productos en Rappi.

#### Página de visualización del Sistema Digital de Comandas (SDC) - En desarrollo

La página de visualización del SDC muestra las comandas cargadas al sistema en tiempo real. Cada comanda muestra el nombre del cliente asociado a la orden, el resumen de la orden, el botón para marcar la orden como completada, el botón para editar la orden y el botón para cancelar la orden; traerán un distintivo que indicará la proveniencia de la orden (caja, menú digital o Rappi).

#### Página de menú digital - Pendiente

La página de menú digital muestra el catálogo de productos disponibles con su respectiva imagen, nombre y precio. Cada producto cuenta con un botón para agregarlo al carrito. El carrito muestra el resumen de la compra, el botón para enviar al SDC, el botón para cancelar la comanda y el nombre del cliente asociado a la orden.

#### Página de corte de caja - Pendiente

La página de corte de caja muestra el resumen de las ventas del día: el total de efectivo en caja, el total de ventas en efectivo, el total de ventas con tarjeta, el total de ventas con Rappi, el total de ventas con menú digital y el total de ventas en general. Al finalizar el corte de caja se enviará un reporte por correo electrónico con el resumen de las ventas del día.

## Presentación del proyecto

[Presentación del proyecto](https://www.canva.com/design/DAFtLa90Y5g/hfpBiFyKO_-vv-mgCCOl8Q/edit?utm_content=DAFtLa90Y5g&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton "Proyecto de digitalización de Trigali - eTrigali") en Canva.

## Registro de avances

#### v0.1.0-alpha

- [x] Establecida la estructura general del proyecto.
- [x] Creación de la página de inicio del sistema.
- [ ] Página de **Comandas** en proceso.

## Planes a futuro

  - Automatización del proceso de carga de productos traídos de fábrica al sistema.
  - Implementación de sistema de trazabilidad de productos accesible a los clientes mediante un código QR y basado en la tecnología _blockchain_.

## Información de contacto

- **Nombre**: Erick Daniel Ortiz Cervantes
- **Correo**: A01750495@tec.mx
