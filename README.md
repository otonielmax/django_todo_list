# To Do List - Prueba 1

_To Do List en Django 2.1 con registro e inicio de sesión para usuarios empleando los modulos de autenticación del framework._

## Comenzando 🚀

_Clona el repositorio usando git, abre la consola de comandos de tu preferencia, ubicate en el directorio donde desees clonar el repo y ejecuta el siguiente comando:_

git clone https://github.com/otonielmax/django_todo_list.git

NOTA: Si no tienes instalado GIT, abajamos te indicamos como hacerlo


### Pre-requisitos 📋

_A continuación te indicamos que necesitas instalar antes de poder correr el proyecto_

GIT (Para poder descargar el repositorio)

```
Windows: Accede al siguiente enlace https://git-scm.com/download/win espera que se descargue el paquete e instala
Linux: Ejecuta el siguiente comando sudo apt-get install git. 
```

_Python 3.7_

```
Windows: Descargar e instalar https://www.python.org/ftp/python/3.7.2/python-3.7.2.exe
Linux: Ejecuta el siguiente comando apt-get install python3
```

_PIP_

```
Descarga el siguiente archivo https://bootstrap.pypa.io/3.2/get-pip.py y colocalo en un directorio de tu preferencia y ejecuta el siguiente comando segun tu SO 

Windows: python get-pip.py
Linux: sudo python get-pip.py
```

_Django 2.1_

```
Windows: pip install Django
Linux: pip install Django
```

### Instalación 🔧

_Para poder correr el proyecto correctamente debes seguir los pasos a continuacion:_

_Entorno Virtual_

```
Nos posicionamos en el directorio raiz de nuestro proyecto desde la consola de comandos y ejecutamos lo siguiente para crear nuestro entorno
 
Windows: (Recomendado) Instalar PyCharm de IntelliJ, ejecutar dicha aplicación y selecccionar abrir proyecto (Open Project), 
ubicamos el directorio de nuestro proyecto y lo seleccionamos. Una vez el proyecto este abierto nos dirijimos a File->Settings->Project Interpreter 
hacemos click en el icono con el engranaje y le damos 'Add' y configuramos el entorno a nuestro gusto. 

Linux: Ejecutamos desde la consola sudo apt-get install python-virtualenv virtualenv. Luego ejecutamos virtualenv env --python=python3 para crearlo
y por ultimo usamos source bin/activate para activarlo.
```

_Migraciones_

```
Es importante correr las migraciones antes de levantar el proyecto:

python manage.py migrate --settings=<DIRECTORIO RAIZ>.settings.develop
```

_Iniciar_

```
Para levantar nuestro proyecto hacemos uso de:

python manage.py runserver --settings=<DIRECTORIO RAIZ>.settings.develop
```

NOTA: Se debe agregar el siguiente parametro --settings=todo_list.settings.develop cuando se desee correr cualquier comando asociado al manage.py   

## Herramientas empleadas 🛠️

* [Django](https://docs.djangoproject.com/es/2.1/) - El framework web usado
* [Python 3.7](http://docs.python.org/3/) - Lenguaje de programación

## Autores ✒️

* **Otoniel Marquez** - [otonielmax](https://github.com/otonielmax)

