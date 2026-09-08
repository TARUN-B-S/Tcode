import tools
from tools_schema import all_tools_schema 
from models import ask_ollama
import traceback

DISPATCH={
    "list_files":  tools.list_files,
    "read_file":  tools.read_file,
    "write_file":  tools.write_file,
    "edit_file":  tools.edit_file,
    "exec_command":  tools.exec_command
}

SYSTEM_PROMPT={"role":"system","content":"You are an ai coding agent use the tools efficiently to complete the task"}
def Tcode(user_input:str):
    user_input={"role":"user","content":user_input}
    messages=[SYSTEM_PROMPT,user_input]
    while True:
        model_response=ask_ollama(model="gemma4:31b-cloud",tools=all_tools_schema,messages=messages)
        messages.append(model_response)
        try:
            if "tool_calls" not in model_response:
                print("Model Respone: ",model_response['content'])
                break;
            else:
                tool_call=model_response.get("tool_calls")[0]
                #print(tool_call)
                tool_call_result=DISPATCH[tool_call['function']['name']](**tool_call['function']['arguments'])
                print("tool call result is :",tool_call_result)
                messages.append({"role":'tools',"content":tool_call_result})
        except:
            print("some error:")
            traceback.print_exc()
            break
        print("\n\n\n")
        
if __name__=="__main__":
    print("hi form Tcode")
    Tcode(input())
