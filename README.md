# Sofka-Challenge

Applicación web fullstack similar al juego "¿Quién quiere ser millonario?" creada con React JS, TailwindCSS, Python Flask y MySQL

## ¿Cómo ejecutar localmente?

El repositorio cuenta con todo el código que construye la aplicación, incluyendo la carpeta `src` que alberga el código sin compilar de React JS. **Sin embargo, para ejecutar la aplicacíon a nivel local** sólo es necesario descargar la carpeta `backend`, el archivo `requirements.txt` y los tres scripts SQL: `answers.sql`, `levels.sql` y `questions.sql`, dado que estos contienen las 25 preguntas de prueba para la aplicación. 

La aplicación de Flask está configurada para servir de forma estática los archivos producidos por Webpack una vez se ejecuta el comando `npm run build`

### Cree el entorno virtual
Una vez descargado el directorio `backend` y los otros archivos mencionados, es necesario crear un entorno virtual para python (`.venv`) para descargar allí los paquetes que requiere la aplicación. En Linux:

```
# En Linux
>>>> python3 -m venv .venv
```

### Instale los paquetes y extensiones especificadas en `requirements.txt`
Una vez creado el virtual environment, actívelo:
```
# En Linux
>>>> source .venv/bin/activate
```
Tras ello, instale las extensiones de Flask especificadas en `requirements.txt`:
```
>>> pip install -r ./requirements.txt
```
*Nota:* `requirements.txt` incluye tanto `mariadb` como `pymysql` para que así usted pueda emplear el conector de base de datos que prefiera. En el desarrollo de esta aplicación, se empleó `mariadb`. 

### Cree la base de datos MySQL, construya el `string` de conexión y agrégelo a `.flaskenv`
Es momento de crear una base de datos para el proyecto, junto con un usuario con todos los permisos para acceder a esta base de datos. Tras crearla, construya un `string` de conexión en el siguiente formato:
```
mariadb+mariadbconnector://<usuario_para_la_base_de_datos>:<contraseña_para_dicho_usuario>@127.0.0.1:3306/<nombre_de_la_base_de_datos>
```
Compruebe que la conexión funciona (por ejemplo, usando un gestor como DBeaver).

### Cree el archivo `.flaskenv` para guardar las variables del entorno
Una vez comprobado el funcionamiento del `string` de conexión, cree un archivo `.flaskenv` para guardar las variables del entorno. Este archivo es leído por Flask para configurar el origen de la base de datos, el entorno de desarrollo y otras configuraciones. Dicho archivo debe tener la siguiente estructura:

```
SECRET_KEY=dev
SQLALCHEMY_DATABASE_URI=<el_string_de_conexión_que_creo_en_el_paso_anterior>
SQLALCHEMY_TRACK_MODIFICATIONS = False
FLASK_APP=backend.py
FLASK_ENV=development
FLASK_CONFIG=development
```

### Cree las tablas en la base de datos que acaba de crear
Este proyecto consta con tres tablas `Questions`, `Answers` y `Levels`, definidas en `./backend/app/models.py`. Para crearlas, ejecute (siempre dentro del virtual environment):

```
>>> flask shell
>>> db.create_all()
```
Salga de `flask shell` (oprima Ctrl+D). Las tablas han sido creadas, pero ahora deben ser llenadas con las preguntas de muestra.

Usted cuenta con acceso a todas las tablas de la base de datos en `flask shell`.  Si revisa el archivo `./backend/backend.py` encontrará definido el contexto para el shell processor.

### Popule las tablas con información de muestra
El repositorio incluye 3 scripts `SQL` en donde se encuentran las 25 preguntas & 100 respuestas solicitadas en los requerimientos para la aplicación, así como los 5 niveles de dificultad. Bien sea en la CLI de MySQL o empleando un gestor como DBeaver, puede ejecutar los scripts para popular las tablas que acaba de crear con la información provista. Tan sólo requerde reemplazar con el nombre de su base de datos en los scripts. Por ejemplo, para la tabla `Answers`:

```
INSERT INTO <Reemplaze_aqui_con_el_nombre_de_su_base_de_datos>.answers (id,question_id,answer_text,correct) VALUES
	 (1,1,'Steve Jobs',1),
	 (2,1,'Román Riquelme',0),
	 (3,1,'Bill Gates',0),
	 (4,1,'Linus Torvalds',0),
	 (7,3,'Linus Torvalds',1),
	 (8,3,'Bill Gates',0),
	 (9,3,'Richard Stallman',0),
	 (10,3,'Aaron Swartz',0),
	 (11,4,'Gentoo',0),
	 (12,4,'Ubuntu',0);
```
Para evitar problemas con los foreign keys, primero ejecute el script `levels.sql`, luego `questions.sql` y, finalmente, `answers.sql`. 

### ¡La aplicación está lista para ser ejecutada!

Una vez:
* El virtual environment haya sido creado.
* Las extensiones de Flask hayan sido instaladas en dicho virtual environment
* Haya sido creada la base de datos y se haya configurado la regla `SQLALCHEMY_DATABASE_URI` con el `string` de conexión.
* Exista el archivo `.flaskenv`
* Hayan sido creadas las tablas con `db.create_all()` desde `flask_shell`
* Hayan sido populadas dichas tablas empleando los scripts de SQL

No hace falta sino ejecutar (nuevamente, desde el virtual environment) el comando `flask run`. Una vez el servidor de desarrollo sea activado, dirígase al link que provee (http://127.0.0.1:5000). Allí, Flask se encargará de servir los archivos estáticos generados por Webpack. Desde allí se puede interactuar con el frontend de la aplicación.

### ¿Cómo crear preguntas en la aplicación?
Para este ejercicio, decidí asumir que el frontend sería utilziado únicamente por jugadores y no por administradores. Por ello, las preguntas se pueden agregar desde `flask shell` empleando el método de clase `create_question` de la Clase `Questions`, definido en el archivo `.backend/app/models.py` de la siguiente forma:

```
>>> flask shell
>>> Questions.create_question(question, answer)
```

La siguiente es la documentación para dicho método:

```
"""
Inserts a question inside Questions table and its associated answers inside Answers table
        Args:
            question: dictionary where the key is a string question_text
            and the value is an int representing the level_id.

            answers: dictionary with 4 key, value pairs where each key is a string
            representing Answers.answer_text and each value is an
            int representing Answers.correct.

        Returns:
            ValueError or KeyError if the provided arguments aren't
            formated as required.

            dict if the question is succesfully added, created by questions.assemble()
"""
```

### Tests incluidos en la aplicación

Dentro de `./backend/tests` encontrará un paquete para ejecutar tests que comprueban la funcionalidad de los modelos definidos en `models.py`, que es prácticamente el corazón de la aplicacíon. Para ejecutarlos, debe correr el comando `flask test` **desde el directorio** `./backend`.

### Los archivos `.py` tienen clases de configuración y condicionales que no se utilizan ¿Por qué?

La aplicación eśtá diseñada para poder ser subida a la plataforma Heroku, así que por ello cuenta con, por ejemplo, el paquete `Flask_sslify` y otras configuraciones. Sin embargo, dichos fragmentos de código no son necesarios para poder emplear la aplicación en `localhost`, pero si son requeridos por Heroku (junto con paquetes como `gunicorn` o un archivo `Procfile`) para correr la aplicación. Próximamente una versión en la nube será agregada a este repositorio

