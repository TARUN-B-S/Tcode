import requests
import json

def ask_ollama(model:str="gpt-oss:120b-cloud",tools:list[dict]=[],messages:list[dict]=[{"role":"user","content":"Hi"}])->dict:
    try:
        url="http://localhost:11434/api/chat"
        payload={
            "model":model,
            "messages":messages,
            "tools":tools,
            "stream":False
        }
        response=requests.post(url,json=payload)
        if response.status_code!=200:
            return "Request to model failed"
        response=response.json()
        return response["message"]
    except:
        return {"role":"tools","content":"Unknown exception when calling the model"} 

#def prune(model:str="gemma4:31b-cloud",messages:list[dict]):
 #   Prompt="""You are the context Pruner for a coding agent. Prune the given conversation history with the following rules :
  #  """
