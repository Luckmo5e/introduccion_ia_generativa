#LLM Pruebas

Repositiorio


#1. Intalacion 

Como primer paso descargamos [ollama]
(https://ollama.com/download/linux) de su pagina web, y ejecutamos el 
siguiente comando:

````bash
$ curl -fsSL https://ollama.com/install.sh | sh
````

##2. Ejecutar el servidor 

Una vez que se descargo e instalo ollama se puede iniciar y detener su ejecución para que no se ejecute en segundo plano.

Para iniciar el servidor se ejecuta el siguiente comando:
````
$ollama serve
````

##3. Descargar un modelo 

en la pagina web de ollama utilizar la siguiente URL [Modelo] (https://ollama.com/library)

````
$ollama pull tinyollama
````


##4. Algunos comandos importantes 

````
$ollama list # Permite visualizar las maquinas que se encuentran cargadas 

````


##5. Repositorios Importantes 
````
[API] (https://github.com/ollama/ollama/blob/main/docs/api.md)
````


##5. Realizar un Request sin Stream

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

##6. Guardar los cambios en Github
````
$git add
$git commit