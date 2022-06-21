# Curso de Flask 

start: 14/06/2020
end: 

sessions:
- 14/06/2022 14:51 | 20:01
- 15/06/2022 21:08 | 22:37
- 16/06/2022 14:04 | 22:48
- 17/06/2022 15:01 | ...
- 18/06/2022 ...   | ...
- 19/06/2022 17:11 | 20:11
- 20/06/2022 14:38 | 16:30

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

## Extensiones de Flask: Bootstrap

Como visto anteriomente las extensiones de flask son modulos que podemos agregar 
para tener más funcionalidades. 

Bootstrap es un framework de css, que nos permite hacer UI webs de una forma sencilla.
Pero con flask podemos usarlo para crear las templates de una forma más sencilla tambien, usando
las templates de jinja, que teniamos, solo requieren unos cambios pequeños de syntaxis.

Para instalar bootstrap, vamos a usar pip. pip3 install flask-bootstrap. Y para inicializarlo 
vamos a:
1. Importar la clase Bootstrap de flask_bootstrap
2. Crear una instancia de Bootstrap
	- Pasar la app de Flask como arg al crear la instancia
3. Usarla.

Este proceso generalmente se puede hacer en la gran mayoria de extensiones, pero algunos no 
son compatibles con este metodo.

El principal uso es en las templates de jinja2. Y usa de varios 
blocks para hacer su estrucutra. Aunque tambien si estamos cortos de tiempo y 
desarrollo, podemos elegir usar un component de bootstrap, copiandolo, pegandolo y
cambiando lo que necesitamos.

## Configuracion de Flask

### Enviroment de servidor
El servidor puede ser tanto de produccion, o listo para ser usado por el usuario, como de development o testing.
Para cambiar esto, vamos a exportar una variable que tenga un enviroment valido.

export FLASK_ENV=development | production

### Debug

Ya lo hemos visto, pero se declara con:
export FLASK_DEBUG=1 | 0

### Testing

Para declarar que estamos haciendo testing en nuestra app de Flask, vamos a crear una env variable, y debemos 
asegurarnos no estar en production.

export TESTING=TRUE | FALSE

### Otras opciones de testing

Hay varias opciones de testing y desarrollo que generalmente son solo de mostrar, guardar o hacer X cosa 
especifica cuando ocurre una situacion, generalmente errores.

### Secret Key

Es una key que nos permite encriptar unos valores de cookies. generalmente de sessions.

### Session

Las sessions son formas en las que los usuarios y servidores pueden comunicarse de una forma segura 
y encriptada, para no tener que caer en el uso de cookies sin restriccion, ya que estas pueden ser 
interceptadas o robadas. 

Generalmente se usan para realizar sesiones de cuentas, entre otros.

### Configuracion desde archivos

Se puede configurar nuestra app usando arvhicos de python, declarando variables. 
U usando json o toml.

El archivo de python generalmente se hace poniendo su path en una env variable. Y despues accediendo a 
esta con python. 

Lo recomendado es tener diferentes configuraciones para development y production, lo cual se 
puede hacer usando estas caracteristicas. 

## App / Request Context

En Python no se pueden manejar valores globales en multi threading, para evitar 
esto, Flask genera contextos que acaparan un gran valor de variables y valores. 
De diferentes categorias, como la app cómo tal y los request del usuario.

Esto lo hace formando proxies o intermedarios entre los datos necesarios.
- App: current_app y g
	- Configuracion de la app
	- Logger
	- Conection a una db
- Req: request y session
	- URL
	- HTTP method
	- Headers
	- request data
	- sessions

## Uso de Formularios con Flask What the Form

What the form es una extension de Flask que nos permite interactuar con los forms que pongamos en
nuestra página web. Es necesario usar una secret key para hacer los forms

Para hacerlo lo vamos a instalar flask-wtf con pip, y importar FlaskForm de flask-wtf.

Vamos a crear una clase, con herencia de FlaskForm, y vamos a definir los inputs esperados como 
propiedades de esta. Definiendo si es un input de str o de password usando la clase de cada 
input, importadas desde wtforms.fields, en cada input vamos a pasar el label que tengan en nuestra 
template.
Para evitar que los usuarios nos envien inputs vacios podemos usar un verificador de contenido
con wtforms.validators. Mandando una instancia de esta al karg de validators. 
Quedandonos nuestra clase de form así:

class NameForm (FlaskForm):
	string = StringField("string label", validators=(Datarequired()))
	pwd = PasswordFiel("password label", validators=(Datarequired()))
	submit = SubmitField("label")

Pasamos una instancia del Form al context de nuestra template y vamos a poder acceder a 
nuestros inputs fields accediendo a estos como propiedades de nuestro form. Y a sus 
labels como propiedades de estos.
{{ name_form.string }}
{{ name_form.string.label }}

Tambien podemos usar un metodo de wtf y bootstrap, que nos permite hacer un quick_form, 
debemos importarlo primero:
{% import "bootstrap/wtf.html" as wtf %}
{{ wtf.quick_form(name_form) }}
Imprimiendo nuestro form con su label, un line break, y el input. Hasta el submit btn del form.

Una vez ya tengamos nuestro form bien hecho, podemos hacer que el action de este se rediriga a una url 
de nuestro servidor, pero para hacer esto debemos primero tener un sistema que pueda recibir ese POST de 
informacion.

## Recibiendo POST de un Form con Flask WTForm

Vamos a crear o modificar una url para nuestro sitio web, en el cual vamos a habilitar los 
methods de POST y GET si vamos a modificar. Esto se hace junto al decorador de @app.route(), 
declarando como una karg y pasando los metodos como un iterable.

Desde la function de la url que sea de POST, vamos a crear o usar una instancia del form 
que vayamos a tomar los datos. Vamos a crear una condicional sencilla en la que se 
verifica que se este verificando el submit de datos, que es un metodo de la instancia del form.

Ahi vamos a poder tomar los valores del form accediendo a los inputs como propiedades de la instancia, 
y sus valores como la propiedad data de los inputs.

## Flash de Confirmacion

Los Flash son popups o alertas que podemos hacer para enviar informacion de confirmacion 
al usuario. Se puede mandar el mensaje del flash a nuestras templates, usando 
la function get_flashed_messages(), donde podremos darles un style unico. Generalmente 
usando bootstrap.

Para hacer un flash solo se va a tener que importarlo de Flask y al usarlo solo 
pasarle el mensaje.

## Flask Testing

Para hcer testing con Flask, podemos usar unit testing o podemos usar la extension de 
Flask Testing, la cual vamos a instalar con pip.
Los tests en Flask generalmente se hacen en diferentes archivos en el folder tests. 

Aunque no lo vamos a usar directamente, vamos a usar de unittesting el TextTestRunner,
el cual correra todos los tests que vayamos haciendo. Y vamos a llamar esto usando 
un decorador de nuestra app que nos permite crear command line interfaces. 

En la terminal que lleguemos a intentar correr el comando, debemos primero exportar 
el FLASK_APP para que funcione.

Para configurar nuestro test, vamos a crear una clase con herencia de TestCase la 
cual vamos a importar de flask_testing. 
En la clase vamos a crear un metodo de create_app, para que nuestra app se inicialice.
Donde vamos a configurar nuestra app para que indique que esta en testing y que se 
pueda enviar posts de nuestros forms. Y importante retornar la app ya configurada.

Despues podemos crear metodos, que empiecen por test_ ya que si no; no los lee, donde podremos hacer nuestros
tests como tal. Generalmente son tests relacionados a una cosa, configuracion o 
parte de nuestro programa, no vayamos a hacer un TestCase para todos los tests 
posibles.

En los tests podemos usar self y los metodos assert... para poder hacer verificaciones 
y los tests como tal. La gran mayoria de asserts son de operadores relacionales, pero 
tambien incluye asserts de respuestas http, redirects, entre otros.
