import requests
import json

def call_ollama_model(model,prompt,stream = False):
    url= 'http://localhost:11434/api/generate'
    parameters = {
        'model':model,
        'prompt':prompt,
        'stream':stream,
        
    }
    payload = json.dumps(parameters)
    response = requests.post(url,data=payload,
                             headers={'content-type':'application/json'})
    if response.status_code != 200:
        return 'ERROR'
    else :
        response= response.json()['response']
        return response 
    
if __name__ == '__main__':
    prompt = input('ask your question?')
    model = 'gemma3:1b'
    response = call_ollama_model(model,prompt)
    print('result:',response)


