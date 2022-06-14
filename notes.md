# Curso de Flask 

start: 14/06/2020
end: 

sessions:
- 14/06/2020 14:51 | 

## Que es Flask?

Flask es un micro framework de python que nos
permite realizar apps webs. Es micro ya que 
es extremadamente ligero y no tiene tantas cosas
cómo los demas frameworks, ademas de ser extremadamente
flexible y se puede agregar / aumentar funciones con 
flask extensions.

" Flask Sabe Hacer una Sola Cosa, Pero la Sabe Hacer Bien "

## Hello World en Flask

Flask es bastante sencillo, solo debemos importar la clase de Flask,
y hacer una instancia de nuestra app. la cual va a necesitar el nombre
de nuestro archivo, generalmente main.py o __init__.py

Este sera nuestra app de flask, y para darle una ruta de accesso desde nuestro
localhost, vamos a crear una function, que solo devolvera "Hello World!!!", y 
le agregamos un decorador de nuestra app.

@app.route("/")

Esto nos permitira acceder a nuestra app desde la ruta / o home. Y al entrar 
nos enviara el contenido de la function, que es "Hello World".

Para crear el servidor vamos a usar el cli de flask, usando:
flask run
Pero primero debemos definir nuestra app de flask como variable global en 
nuestro computador, haciendo:
export FLASK_APP=main.py o nuestro archivo

Despues de tener volver a correr nuestro servidor, nos dira que esta en el 
127.0.0.1 - localhost, en el puerto :5000. Si accedemos con un navegador a 
esta ruta, vamos a encontrar nuestro Hello World

## Debuggin en Flask

Despues de montar el servidor, deberiamos tener que desmontar y montar para cada 
modificacion y arreglo. Ademas de que los errores no nos explicarian donde ocurrienron
Simeplemente vamos a crear otra variable global:
export FLASK_DEBUG=1

Ahora nuestro servidor detectara cada cambio en sus archivos y se reiniciara automaticamente,
y nos dara un reporte y explicaciones de los errores que ocurran.

Para confirmar, nuestro servidor al iniciarlo debe decir Debug mode: on y Debugger is Active! junto a 
su pin.

## Request y Response 

Los Requests y Responses es la forma en la que nuestro servidor y el usuario se 
comunican, generalmente se hace un request al servidor para ver su contenido, la página web.
Y el servidor respondera con el responce se esta.
Pero tambien se puede hacer diferentes requests desde el servidor hacia el usuario, como su IP.
Y este dara la informacion. Para hacer request vamos a importar request y mirar que 
vamos a pedirle al usuario.

## Request y Response de Cookies 

Las cookies son valores que podemos agregarle a los usuarios cuando 
esten usando nuestro sitio web, como login, entre otros. Con Flask 
podemos crear cookies que tendran un valor y un nombre, la cual 
podremos usar.
