# SQL - Structured Query Language

USE DataScienceEnero2022;
SELECT nombre,genero,edad FROM users WHERE edad>23;

SELECT * FROM users; # Trae todas las columnas de la tabla users

INSERT INTO users VALUES(2,"Juan Diego","Arenas",23,"M");

INSERT INTO users(nombre,apellidos,edad) VALUES("Maxi","Colque",24);

UPDATE users SET genero="M"; # Actualiza todos los registros
UPDATE users SET genero="" WHERE genero IS null; # Casi siempre añadir el WHERE

INSERT INTO users(nombre,edad,genero) VALUES("Salvador",24,"M");

DELETE FROM users WHERE nombre="Maxi";