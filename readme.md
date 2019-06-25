# Prueba tecnica python

Esta es la prueba técnica de python para Innohub México

### Requerimientos
  - Python 3.7

#### Sección A
Sin hacer uso de librerías o funciones nativas. Hacer un programa que tomando una palabra o párrafo:
  - Contar cuántas vocales hay.
  - Reemplazar las vocales por la vocal consecutiva (a->e).

```
python vocals.py
```

Sin hacer uso de librerías o funciones nativas. Escribe un programa el cual tomando un conjunto de datos con sus atributos (Figura a):
  - Ordenar los datos de acuerdo al nivel de prioridad (padre e hijo).
  - Utilizar un método llamado show() que permita visualizar los datos ordenados.
  - Al ingresar un nuevo dato (o conjunto de datos) realizar el ajuste necesario para colocar el dato en la posición adecuada.

```
python order.py
```

#### Sección B

Realiza el esquema DB (Relacional o NoSql) para lo siguiente:
  - Aplicación para gestionar una flota de vehículos, en donde una persona puede tener n vehículos asignados pero solo puede manejar uno. Cada asignación de vehículo tiene una fecha de expiración.

**Vease archivo database_1.png**

Dado las siguientes entidades y atributos, normaliza como creas conveniente. 

Inventario
  - Número
  - Fecha
  - Usuario
  
Producto
- Descripción
- Cantidad
- Precio

Almacén

**Vease archivo database_2.png**

#### Sección C

Basados en las reglas del torneo de badminton.
-  Escribe un programa para llevar el marcador.
   - El programa debe permitir mostrar el resultado actual.
   - Debe permitir añadir los puntos de cada jugador.
   - Debe notificar cuando exista un set, Match o cambio de campo. o Debe notificar cuando un jugador gane.
```
python badminton.py
```
   - Escribe las pruebas unitarias necesarias.
```
python test_badminton.py
```

Basado en la siguiente HU, define las pruebas a realizar
  - Como Cliente, quiero suscribirme a un canal Premium por períodos flexibles de tiempo por medio del sitio web.

***

Para la historia de usuario dada, se proponen las siguientes pruebas:
-	Verficar que el cliente se encuentra activo
-	Verificar que el canal al que el cliente intenta subscribirse se encuentra activo
-	Verificar que la fecha de fin del perido de subcscripción no es anterior a la fecha de inicio
-	Verificar que el total a pagar corresponda con el precio del perido más impuestos
-	Verificar que despues de pagar el usuario tiene acceso al canal


