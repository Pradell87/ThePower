-- Ejercicio 1
/*1. Crear una tabla llamada "Clientes" con las columnas: id (entero, clave primaria),
nombre (texto) y email (texto).*/
CREATE TABLE Clientes (
	id INT PRIMARY KEY,
	nombre VARCHAR(255),
	email VARCHAR(255)
)

/*2. Insertar un nuevo cliente en la tabla "Clientes" con id=1, nombre="Juan" y
email="juan@example.com"*/
INSERT INTO clientes (id, nombre, email)
	VALUES (1, 'Juan', 'juan@example.com')

/*3. Actualizar el email del cliente con id=1 a "juan@gmail.com".*/
UPDATE clientes
	SET email = 'juan@gmail.com'
	WHERE id = 1

/*4. Eliminar el cliente con id=1 de la tabla "Clientes".*/
DELETE FROM clientes
	WHERE id = 1

/*5. Crear una tabla llamada "Pedidos" con las columnas: id (entero, clave primaria),
cliente_id (entero, clave externa referenciando a la tabla "Clientes"), producto
(texto) y cantidad (entero).*/
CREATE TABLE Pedidos (
	id INT PRIMARY KEY,
	cliente_id INT,
	FOREIGN KEY (cliente_id) REFERENCES clientes(id),
	producto VARCHAR(255),
	cantidad INT
)

/*6. Insertar un nuevo pedido en la tabla "Pedidos" con id=1, cliente_id=1,
producto="Camiseta" y cantidad=2.*/
INSERT INTO pedidos (id, cliente_id, producto, cantidad)
	 VALUES (1, 1, 'Camiseta', 2)

/*7. Actualizar la cantidad del pedido con id=1 a 3.*/
UPDATE pedidos
	SET cantidad = 3
	WHERE id = 1

/*8. Eliminar el pedido con id=1 de la tabla "Pedidos".*/
DELETE FROM pedidos
	WHERE id = 1

/*9. Crear una tabla llamada "Productos" con las columnas: id (entero, clave
primaria), nombre (texto) y precio (decimal).*/
CREATE TABLE Productos (
	id INT PRIMARY KEY,
	nombre VARCHAR(255),
	precio DECIMAL
)

/*10. Insertar varios productos en la tabla "Productos" con diferentes valores.*/
INSERT INTO Productos (id, nombre, precio)
	VALUES
	(1, 'Manzana', 0.50),
	(2, 'Banana', 0.30),
	(3, 'Naranja', 0.60),
	(4, 'Leche', 1.20),
	(5, 'Pan', 0.90)

/*11. Consultar todos los clientes de la tabla "Clientes".*/
SELECT * FROM clientes

/*12. Consultar todos los pedidos de la tabla "Pedidos" junto con los nombres de los
clientes correspondientes.*/
SELECT * FROM pedidos p
LEFT JOIN clientes c ON p.cliente_id = c.id

/*13. Consultar los productos de la tabla "Productos" cuyo precio sea mayor a $50.*/
SELECT * FROM Productos
WHERE precio > 50

/*14. Consultar los pedidos de la tabla "Pedidos" que tengan una cantidad mayor o
igual a 5.*/
SELECT * FROM Pedidos
WHERE cantidad >= 5

/*15. Consultar los clientes de la tabla "Clientes" cuyo nombre empiece con la letra
"A".*/
SELECT * FROM clientes
WHERE nombre ILIKE 'A%'
