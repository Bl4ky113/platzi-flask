# Curso de Flask 

start: 14/06/2020
end: 

sessions:
- 14/06/2022 14:51 | 20:01
- 15/06/2022 21:08 | 22:37
- 16/06/2022 14:04 | 

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

## Templates en Flask

Las Templates son fracciones o archivos enteros de HTML5 que nos 
va a permitir darle informacion y el sitio web como tal al usuario.
Flask tiene integrado un render de estas templates y estas van a 
estar guardadas en el dir templates/

Con los templates se pueden enviar valores y variables para que no solo 
muestren dados estaticos, si no dinamicos.
Estos se acceden usando {{ valor }}
Y como generalmente vamos a tener varios valores a enviar, lo recomendado 
es hacer un dict de context, el cual vamos a pasar a la templeate usando 
el unpack de dict:

context = { ... valores de la template }
render_template("template", \*\*context)

Así no tendremos que acceder a context para tener cada valor en nuestra template.

## Syntaxis de Jinja2

En jinja 2 tiene una syntaxis parecida a html, con unas añadiduras para ser 
procesadas. Se puede usar comentario, print y sentence. Las cuales 
nos permitiran hacer diferentes acciones, principalmente la sentece.

{# comentario #}: Se usa para comemtarios que no se muestren en el html final
{{ variable }}: Se usa para imprimir una variable o valor en el html final, se puede usar tambien para macros
{% sentece %}: Se usa para realizar una sentencia de lógica o de programación. Se usa en:
- estructuras de control: if, else, for, while
- estructuras de template: extends, block, macro
Se deben cerrar especificando con {% endsentence %}, cambiando sentence por el nombre de 
la sentece usada.
Como algunas veces vamos a tener que hacer de varios niveles nuestras sentence, el whitespace 
tambien va a ser usado en el htmlfinal, para evitar esto, vamos a usar un - en el primer % de 
la sentece y otro - en el ultimo % del endsentence
{%- sentece  %}
	...
{% endsentece -%}

## Estructuras de Control

Las estructuras de control, en las plantillas, son formas en las que podemos 
hacer llamado a bloques de código como ifs, elses, loops, etc.

Estas van a tener que ser abiertas y usadas con {% estructura %}, las cuales son 
exactamente iguales a las de python normal, pero sin ":".
Y van a tener que ser cerradas usando {% end"estructura" %} dado a que no contamos
con iteraciona

## Herancia de Templates

Con las templates, para evitar tener que repetir código, podemos hacer diferentes
llamados o herencias en las templates de otras templates de html.

### Extends
Podemos directamente hacer un export, el cual va a tomar todo el código html de la 
template dada, hasta que cierre la tiqueta </hmtl>. Esto puede generar problemas ya 
que podemos tener problemas al exportar todo un archivo html completo.
Para hacer un export usamos la sintaxis de las estructuras de control y usamos 
export "template.html"

{% extends 'template.html' %}

Debemos tener en cuenta que al llamar el export, se va a poner la template en la 
posicion en la que fue llamada. Util para tener en cuenta el orden de declaracion de los 
blocks y en el export de templates pequeñas cómo modulos de otra más grande.

### Blocks
Pero se puede hacer diferentes bloques de templates para evitar problemas con el export. 
Las cuales nos permitiran hacer diferentes estructuras en las templates.
Se define con block nombre y al final con endblock.
Se puede hacer varios blocks con los mismos nombres, y estos seran reescritos, pero 
usables con super() dentro del block.

{% block nombre %} ... {% endblock %}
{% block nombre %} 
{{ super() }}
...
{% endblock %}

Es importante al momento de crear la base de nustra estructura, llamar a render de 
template al archivo que tenga el export, ya que puede generar errores de carga y demás.

### Macros
Los Macros son partes de html que se repiten y que pueden tener alguna que otra 
variacion, cómo si fueran una funcion. Estos generalmente se van a 
escribir en un archivo y se importaran para su uso. 
Se usa la misma sintaxis de sentence.

{% macro nombre_macro(args) %}
... {{ args }}
{% endmacro %}

// En el archivo donde se van a usar los macros

{% import "macros.hmtl" as variable_macros %}
{{ variable_macros.nombre_macro(args) }}

## Include 

Include nos permite tomar templates pequeñas y agregarlas a otras, sin nada más.
{% include "archivo.html" %}

## Archivos staticos en Flask

Los archivos estaticos en Flask se organizan en una carpeta llamada 
static, pueden ser:
- css
- js
- imagenes
- videos
- etc
Por lo general cada tipo de archivo deberia tener su propia carpeta.
Para acceder a los elementos vamos a tener que usar {{ url_for("static". filename="carpeta/archivo") }}
Y desde ahí nos dara el url del archivo, para despues usarlo en las tags o campos que se necesite.

## Manejo de Errores HTTP

Los errores en HTTP generalmente son de rangos 400 y 500. Para manejarlos, los vamos a 
tener que hacer justo como las urls. Pero con otro decorador.

@app.errorhandle(num_error)

Los rangos de códigos http son:
- 100: mensajes informativos entre navegador y server
- 200: mensaje y envio de informacion correcta
- 300: mensaje de reenvio & redirecciones
- 400: error de cliente, archivo privado o no existente
- 500: error de servidor

Para poder simular un error de servidor, podemos retornar en una 
route una execption 500.

@app.route("/error-test")
def error_500():
	raise Exception("500 error")
