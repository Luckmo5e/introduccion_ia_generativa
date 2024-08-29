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
($git add)
($git commit -m "UPDATE Manual LLM v2.md")
($git push -u origin main)
````