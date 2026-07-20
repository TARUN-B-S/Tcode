from pathlib import Path 
import shlex
import subprocess

def read_file(file_path:str)->str:
    try:
        with open(file_path,'r') as f:
            return f.read()
    except FileNotFoundError:
        return "Reading failed: File not found"

def write_file(file_name:str,content:str)->str:
    with open(file_name,'w') as f:
        f.write(content)
    return "Write sucessfull"
    
def edit_file(file_name:str,old_str:str,new_str:str)->str:
    try:
        content=read_file(file_name)
        if content.count(old_str)>1:
            return "Edit failed: More than one match of old_str found"
        if content.count(old_str)==0:
            return "Edit failed: old_str not found"
        content=content.replace(old_str,new_str)
        write_file(file_name,content)
        return "Edit sucessfull"
    except FileNotFoundError:
        return "Edit failed: File not found"

def list_files(dir_name:str=Path.cwd().name)->str:
    try:
        files=f"Files in the directory {dir_name}\n"+' \n '.join([f.name for f in Path(dir_name).iterdir()])
        return files
    except:
        return "Lisitng failed: Unknown error"

def exec_command(command:str)->str:
    try:
        result=subprocess.run(shlex.split(command),capture_output=True,text=True)
        op=f"return code:{result.returncode}\nstdout:{result.stdout}\nstderr:{result.stderr}"
        return op 
    except:
        return "execution failed: Unknown error"
