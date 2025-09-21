--Ejercicio 4
--Nivel de dificultad: Experto
/*1. Crea una tabla llamada "Pedidos" con las columnas: "id" (entero, clave
primaria), "id_usuario" (entero, clave foránea de la tabla "Usuarios") y
"id_producto" (entero, clave foránea de la tabla "Productos").*/
CREATE TABLE Pedidos (
    id INT PRIMARY KEY,
    id_usuario INT REFERENCES Usuarios(id),
    id_producto INT REFERENCES Productos(id)
)

/*2. Inserta al menos tres registros en la tabla "Pedidos" que relacionen usuarios con
productos.*/
INSERT INTO Pedidos (id, id_usuario, id_producto) VALUES
(1, 1, 1),
(2, 1, 2),
(3, 1, 3)

/*3. Realiza una consulta que muestre los nombres de los usuarios y los nombres de
los productos que han comprado, incluidos aquellos que no han realizado
ningún pedido (utiliza LEFT JOIN y COALESCE).*/
SELECT u.nombre AS usuario,
       COALESCE(p.nombre, 'Sin pedido') AS producto
FROM Usuarios u
LEFT JOIN Pedidos pd ON u.id = pd.id_usuario
LEFT JOIN Productos p ON pd.id_producto = p.id

/*4. Realiza una consulta que muestre los nombres de los usuarios que han
realizado un pedido, pero también los que no han realizado ningún pedido
(utiliza LEFT JOIN).*/
SELECT u.nombre AS usuario, pd.id AS id_pedido
FROM Usuarios u
LEFT JOIN Pedidos pd ON u.id = pd.id_usuario

/*5. Agrega una nueva columna llamada "cantidad" a la tabla "Pedidos" y actualiza
los registros existentes con un valor (utiliza ALTER TABLE y UPDATE)*/
ALTER TABLE Pedidos
ADD COLUMN cantidad INT;

UPDATE Pedidos
SET cantidad = 1;
