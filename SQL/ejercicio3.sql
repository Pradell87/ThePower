--Ejercicio 3
--Nivel de dificultad: Difícil
/*1. Crea una tabla llamada "Productos" con las columnas: "id" (entero, clave
primaria), "nombre" (texto) y "precio" (numérico).*/
CREATE TABLE Productos (
    id INT PRIMARY KEY,
    nombre VARCHAR(100),
    precio NUMERIC
)

/*2. Inserta al menos cinco registros en la tabla "Productos".*/
INSERT INTO Productos (id, nombre, precio) VALUES
(1, 'Ordenador', 799.99),
(2, 'Teclado', 25.50),
(3, 'Ratón', 15.75),
(4, 'Monitor', 199.90),
(5, 'Impresora', 120.00)

/*3. Actualiza el precio de un producto en la tabla "Productos".*/
UPDATE Productos
SET precio = 849.99
WHERE id = 1

/*4. Elimina un producto de la tabla "Productos".*/
DELETE FROM Productos
WHERE id = 5

/*5. Realiza una consulta que muestre los nombres de los usuarios junto con los
nombres de los productos que han comprado (utiliza un INNER JOIN con la
tabla "Productos").*/
CREATE TABLE Compras (
    id SERIAL PRIMARY KEY,
    usuario_id INT REFERENCES Usuarios(id),
    producto_id INT REFERENCES Productos(id)
);

INSERT INTO Compras (usuario_id, producto_id) VALUES
(1, 1),
(1, 2),
(2, 3);

SELECT u.nombre AS usuario, p.nombre AS producto
FROM Compras c
INNER JOIN Usuarios u ON c.usuario_id = u.id
INNER JOIN Productos p ON c.producto_id = p.id;


