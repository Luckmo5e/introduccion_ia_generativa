import requests
import json

url = 'http://localhost:11434/api/generate'
myobj = {
    "model": "tinyllama",
    "prompt" : "why is the sky blue",
    "stream": False
    }

x = requests.post(url, json = myobj)

x = requests.post(url, json=myobj)


response_data = x.json()

print(response_data["response"])