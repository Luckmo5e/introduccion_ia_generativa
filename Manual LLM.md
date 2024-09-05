<h1>LLM Pruebas</h1>

Repositiorio


<h1>1. Intalacion </h1>

Como primer paso descargamos [ollama]
(https://ollama.com/download/linux) de su pagina web, y ejecutamos el 
siguiente comando:

````bash
$ curl -fsSL https://ollama.com/install.sh | sh
````

<h1>2. Ejecutar el servidor </h1>

Una vez que se descargo e instalo ollama se puede iniciar y detener su ejecución para que no se ejecute en segundo plano.

Para iniciar el servidor se ejecuta el siguiente comando:
````
$ollama serve
````

<h1>3. Descargar un modelo</h1> 

en la pagina web de ollama utilizar la siguiente URL [Modelo] (https://ollama.com/library)

````
$ollama pull tinyollama
````


<h1>4. Algunos comandos importantes </h1>

````
$ollama list # Permite visualizar las maquinas que se encuentran cargadas 

````


<h1>5. Repositorios Importantes </h1>
````
[API] (https://github.com/ollama/ollama/blob/main/docs/api.md)
````


<h1>5. Realizar un Request sin Stream</h1>

El stream= False permite generar el response en una unica linea 
````
##Request

curl http://localhost:11434/api/generate -d '{
  "model": "tinyllama",
  "prompt": "What color is the sky at different times of the day? ",
  "stream": false
}' #-o salida.md

##Response 

{
  "model": "tinyllama",
  "created_at": "2023-08-04T08:52:19.385406455-07:00",
  "response": "The",
  "done": false
} 
````

<h1>6. Guardar los cambios en Github</h1>
````
($git add .)
($git commit -m "UPDATE Manual LLM v2.md")
($git push -u origin main)
````

<h1>Como ingrear a GroqCloud y generar una API Key</h1>

Este manual proporciona una guía paso a paso para acceder a **GroqCloud** y generar una clave de API que se utilizará para la autenticación y el acceso a los servicios de GroqCloud.

## Requisitos Previos

Antes de comenzar, asegúrate de tener lo siguiente:

- Una cuenta activa en GroqCloud.
- Acceso a Internet y un navegador web compatible.

## Paso 1: Ingresar a GroqCloud

1. Abre tu navegador web preferido y dirígete a la página principal de GroqCloud: [https://groq.com/cloud](https://groq.com/cloud).
2. Haz clic en el botón **Sign In** (Iniciar sesión) ubicado en la parte superior derecha de la página.
3. Ingresa tus credenciales de acceso (correo electrónico y contraseña) y haz clic en **Login** (Iniciar sesión).

   - Si aún no tienes una cuenta, selecciona la opción **Sign Up** (Registrarse) y sigue los pasos para crear una cuenta nueva.

## Paso 2: Acceder a la sección de API Keys

1. Una vez que hayas iniciado sesión, serás dirigido al panel de control de GroqCloud.
2. En el menú lateral izquierdo, busca y haz clic en **API Keys** (Claves de API).

## Paso 3: Generar una nueva clave de API

1. Dentro de la sección **API Keys**, haz clic en el botón **Generate New Key** (Generar nueva clave).
2. Se te pedirá que proporciones un nombre para tu clave de API. Este nombre te ayudará a identificar la clave más adelante. Ingresa un nombre descriptivo, como **`Clave para proyecto X`**.
3. Selecciona los permisos que deseas otorgar a esta clave. Por defecto, todas las claves tienen permisos básicos, pero puedes personalizarlos según tus necesidades.
4. Haz clic en **Generate Key** (Generar clave).

## Paso 4: Guardar la clave de API

1. Una vez que hayas generado la clave, aparecerá en pantalla. **IMPORTANTE**: copia y guarda esta clave en un lugar seguro.
   
   - **Nota**: Por razones de seguridad, esta clave solo se mostrará una vez. Si la pierdes, tendrás que generar una nueva.

2. Utiliza esta clave en tus aplicaciones para autenticarte con los servicios de GroqCloud.

## Paso 5: Configurar tu entorno local

1. Para utilizar tu clave de API en un entorno de desarrollo local, establece la clave como una variable de entorno. Por ejemplo, en sistemas basados en UNIX (Linux, macOS), puedes ejecutar:

    ```bash
    export GROQCLOUD_API_KEY="tu_clave_aqui"
    ```

2. En Windows, puedes configurar una variable de entorno utilizando el siguiente comando en el **Símbolo del sistema**:

    ```cmd
    set GROQCLOUD_API_KEY="tu_clave_aqui"
    ```

## Notas de Seguridad

- No compartas tu clave de API públicamente. Trata tu clave como una contraseña secreta.
- Revoca cualquier clave que creas que ha sido comprometida inmediatamente desde la sección **API Keys** del panel de control de GroqCloud.
- Puedes generar varias claves para diferentes proyectos o servicios según sea necesario.

