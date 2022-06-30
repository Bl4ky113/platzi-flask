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
- 21/06/2022 14:46 | 21:19
- 22/06/2022 09:55 | 22:05
- 24/06/2022 12:05 | 22:41
- 25/06/2022 19:17 | ...
- 27/06/2022 12:35 | 22:12
- 28/06/2022 16:06 | ...
- 29/06/2022 16:15 | 19:53
- 30/06/2022 11:27 | 

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

# Proyecto de Flask

Nuestro proyecto va a ser una app de to do lists de nuestros usuarios.
En donde vamos a guardar los usuarios y sus to do lists en una base de datos, 
donde van a tener que hacer un login y subir, hacer sus to do lists.

Esta app va a ser un deploy en app factory, para que se pueda acceder desde el internet.
Pero tambien como nuestra app esta un poco desorganizada, la vamos a organizar usando blueprints.
Haciendola un poco más modular y organizada.

## Modularizacion de Apps de Flask

### App

Primero debemos tener un dir de nuestra app de flask, en donde vamos a 
crear la app y agregar sus extensiones. Esto lo vamos a hacer en el 
archivo __init__.py dentro de una function llamada create_app.

Ahora para usar la app de Flask vamos a tener que importar de app, create_app.

### App Config

Para configuraciones de esta app vamos a hacerlo en otros archivos, así para 
tener diferentes para cada env. Estos archivos deben estar en el dir app.

### Forms 

Para los forms de WTforms vamos a crear un archivo aparte, el cual se va a importar 
cuando se necesiten los forms, dentro del dir de app.

### Templates, Static y Tests

Todas las carpetas que antes teniamos, las vamos a mover al dir app.

## Blueprints

Aunque ya tenemos casí todo organizado, podemos usar Blueprints que nos permite 
modularizar las routes de nuestra app. 

El crear un Blueprint es algo complicado, pero no imposible.
1. Creamos un modulo en app (carpeta/__init__.py)
2. En init vamos a crear un Blueprint importandolo desde flask
	- Blueprint nos pide el nombre del blueprint, el nombre del archivo, y el prefijo o subdireccion de nuestro blueprint
		"blueprint", __name__, url_prefix="/blueprint"
3. Vamos a crear un archivo en el modulo de views, el cual va a guardar las rutas del blueprint.
4. Tenemos que hacer un import del blueprint creado en init y desde init vamos a importar el archivo de views
	En init: from . #module import views
	En views: from . #module import var_blueprint
	Obviamente quitar el #module
5. En views vamos crear una nueva route usando el decorador de route, de var_blueprint en una function 
	que va a ser igual a nuestras routes normales de app. Creando un contexto y haciendo render de una template.
6. Despues de tener o para probar nuestro blueprint, vamos a ir a app/__init__.py a registrar el 
	blueprint con ese mismo method, poniendo como arg al var_blueprint, importandolo como 
	from .blueprint import var_blueprint.
7. Ya podemos usar nuestro blueprint o subdireccion en nuestra app de Flask

- Para acceder a una url o route desde un blueprint, generalmente con url_for, vamos a escribir "blueprint.route"

## Bases de Datos en Flask

Como explicado anteriormente, Flask no tiene definida una db para su uso. Si no que tenemos nosotros
que implementar la que vayamos a usar. Lo que vamos a definir es un ORM y el tipo de base de datos que vamos a usar.

### Que es ORM 
ORM o Object Relational Mapping es una tecnica que nos permite convertir datos, generalmente de 
dbs, en objects de programacion. 

Los ORMs que se pueden utilizar en flask son extensiones de estos, para dbs SQL generalmente se 
usa SQLAlchemy, Y en el proyecto del curso vamos a usar la db de google, firestore. En donde
vamos a usar una db NoSQL, No Relacional, basada en documentos.

Vamos a tener que crear una cuenta en Google Cloud Plataform. Y tener que instalar un cli para 
poder usar la terminal de nuestra db desde nuestra terminal. Aunque lo mejor seria utilizar una 
cli en el navegador para no instalar ninguna cosa de Google en mi sistema.
Podemos usar una terminal cloud que nos da Google, que es mejor que instalar gcloud en nustro OS.

## Crear una DB de Firestore en Google Cloud.

Despues de crear nuestra cuenta en Google Cloud, generalmente solo conectar nuestra cuenta de 
gmail. Vamos a crear un proyecto, ir al menu de la izquierda & buscar el recurso de firestore.
Vamos a crear una db de firestore con base de documentos y collections. Vamos a elegir 
un servidor donde vamos a guardar nuestra db, generalmente cercano a nosotros y a nuestros 
potenciales usuarios.
Una vez creado todo, simplemente la usamos, generando collections y sus documentos. Generalmente
creando el schema de nuestra db. Para el proyecto, va a ser:

- /
	- /users/
		- ../user_id
			- user_name:str
			- user_email:str|email
			- user_password:str
			- user_id/todos/
				- todo_id
					- description_todo:str
					- status_todo:bool

Al parecer va a tocar instalar el CLI de google, ya que no creo que se pueda mandar mi app de 
flask al navegador, a la terminal cloud del proyecto, y que sea de una forma efectiva. :c srry foss

### Configurar y demas el CLI de GCloud

Lamentablemente debemos instalar el CLI GCloud para hacer funcinar nuesta app de Flask con Firestore,
La vamos a descargar usando un curl, desempaquetamos el tar, y ejecutamos el install.sh.
En la instalacion nos va a preguntar si queremos agregar gcloud al path, aceptamos
Y nos va a preguntar si quiere recolectar nuestros datos anonimos, denegado.
Despues vamos a hacer login con nuestra cuenta de google, usando:
gcloud auth login

Y iniciar el CLI con 
gcloud init
el cual nos va a reconfirmar nuestra session, seleccionar un proyecto y demás.

Despues vamos a autenticar nuestro uso de GCloud en cuando manejo del servidor y SQL.
gcloud auth application-default login.

## Implementar Firestore en Flask

Vamos a instalar con pip firebase-admin, y vamos a crear en app/firestore_services.py
En este archivo vamos a importar firebase_admin, y aparte de firebase_admin, credentials y 
firestore. 

Vamos a crear unas credenciales de nuestra "app default" que fue la que configuramos en gcloud
y usar el method initialize_app de firebase_admin, pasandole las credencials que creamos.

la db la vamos a acceder usando el metohod client de firestore. Con esta instancia vamos a 
acceder a nuestra db con los metodos y submetodos:
- collection("nombre"): accedemos a collections
	- get(): obtiene todos los docs en una lista.

Una vez tengamos los documentos, vamos a poder acceder a los valores ya sea atra vez de 
propiedades, o convirtiendolo a dicts, con to_dict(). Uno de los valores importantes que 
no van a estar disponibles en los dicts son los id unicos, cuales solo los accedemos desde 
el firestore obj con la propiedad .id.

## Implementar Login con nuestra db en Flask

Usaremos la ext de Flask Logins para implementar logins. Vamos a crear una instancia de 
LoginManager en init de nuestra app. Hacer set de la route de nuestro login en login_view.

Y dentro de create app, vamos a hacer init a la app, recibiendo nuestra app como parameter.

Si necesitamos que una ruta solo se accesible para personas ya logeadas, podemos agregar 
a nuestra def de ruta otro decorador, abajo del de route, @login_required

Pero como para tal tener usuarios logeados en nuestra app, LoginManager requiere de unos 
modelos de usuarios que tengan unas propiedades. 
Para no tener que escribir las propiedades, podemos hacer heritance de UserMixin de 
flask_login. Y de esta clase, vamos a crear otra clase con los datos que vamos a tener de 
nuestro usuario. Y pasar los datos como propiedades de ambas clases.

En UserModel vamos a crear un static method que nos va a permitir hacer un query a los 
usuarios en la db y obtener estos mismos retornandolos en una instancia de UserModel.

En init de nuestra app vamos a crear una function que pida un id, email en mi caso, y 
que retorne el UserModel del usuario con ese id, usando el method query. Y a esta 
function le ponemos el decorador user_loader de la instancia creada del LoginManager.

Con esto podemos obtener y crear un obj cómo tal de un usuario, pero nos falta 
hacer el login cómo tal. 

EL login se implementa en el proceso del POST de los datos del Login_Form en nuestra
ruta auth.login, donde vamos a tomar los datos del formulario y:
1. Mirar que exista el usuario
2. Mirar que el usuario y la contraseña dada sea correcta
3. Crear una instancia de UserModel, pasandole UserData como param
4. Usar la function login_user de flask_login y pasarle nuestro UserModel
5. Usar el usuario logeado con el obj current_user de flask_login. Accediendo a los 
parametros de nuestra User Data y UserMixmin

## Implementar Logout

Para hacer una implementacion del Logout vamos a hacer otra ruta en 
auth, vamos a usar la function logout_user, en la cual no necesitamos 
pasar nada, ya que flask mismo sabe cual usuario quitar.
Agregamos un flash, para que se note el cambio y hacemos redirect a login o 
index para que no de error.

## Implementar Sign In

Para hacer sign in básicamente vamos a usar las mismas estructuras y plantillas 
de log in, cambiandoles cosas cómo los titulos. Y agregando más inputs del usuario.
Además al momento de ingresar la contraseña, vamos a tener que encryptarla 
o hashsearla. Para que esta no este disponible en nuestra db, y que solo el 
usuario pueda usarla. 
Esto se va a hacer con la function de generate_password_hash() del modulo integrado de
Flask, werkzeug.security, con la cual le pasamos la password y nos devuelve la 
password hasheada.

Vamos a crear una instancia de user_data con los datos que nos dieron, usando 
una function de nuestra db, que en el curso primero se crea usando el nombre 
del usuario el doc, y despues se hace set() de los datos del usuario. 
Yo solo tengo que tomar los valores del usuario, convertirlo en dict y 
hacer un add() con estos a la collection, con esto se generara automaticamente
un id unico.

Aunque nosotros ahora vamos a tener hasheada el pwd de nuestro usuario, vamos a 
tener que modificar el login para que pueda leer estas passwords hasheadas, 
usando check_password_hash de werkzeug.security, el cual recibe la password 
del usuario y la password del form

## Implementar To Do Lists

Todo el proceso de agregar las To Do lists en el proyecto del curso 
y el mio son difentes, la mayor diferencia entre el curso y yo son:
- El curso hace las to do lists por cada usuario, yo 
hago que el usuario pueda crear diferentes to do lists y que estas
tengan a su creador como identificador.
- El curso hace la to do list solo una lista y los to dos los 
objs de esta. Yo hago la to do list un obj que se pueda usar y 
que contenga objs, los to dos.

## Resumen Implementacion Delete y Update de To Dos

En el proyecto del curso, despues de poder crear los to dos, se genera un 
macro de jinja para darles un style especial, en esta macro se pasan dos 
forms para Delete y Update, los cuales solo son un botón de butmit que pasan 
los valores de cada to do list al hacer submit, para ser eliminados de la db.

Por cierto, toma los todos del usuario y los imprime con el macro en un loop.

Para enviar los ids, lo que se hace es crear una url dinamica.

### URL dinamicas

Generalmente son URL que solo se acceden con POST, el cual 
se usa la URL para enviar datos, para hacer esto en Flask vamos a 
escribir una nueva function con el decorador route de nuestra app o blueprint. 
En la url entre <>, y aunque no he podido verificar si solo se puede asi, 
separados por / cada valor.

Los valores los vamos a acceder poniendolo como arg en la function que 
tiene el decorador. Para poder ser usadas en esta function.
Las variables en la URL pueden tener al inicio el tipo  de la variable, dos puntos 
y el nombre de esta, estos pueden ser:
- string (default)
- int
- float
- path (string con /)
- uuid
Para manejar bools, vamos a tener que usar su equivalencia en ints o strings
