list_file_schema=[
        { 
            "type":"function",
            "function":{
                "name":"list_files",
                "discription":"list the files in the given directory",
                "parameters":{
                    "type":"object",
                    "properties":{
                       "dir_name":{
                        "type":"string",
                        "discription":"The directory to be listed , if you want to list the dir from which the program is invocated don't pass any args not even . , absolute path is prefered"
                        }
                    }
                }
            }
        }
]

read_file_schema=[
        { 
            "type":"function",
            "function":{
                "name":"read_file",
                "discription":"read a specific file using its name",
                "parameters":{
                    "type":"object",
                    "properties":{
                       "file_path":{
                        "type":"string",
                        "discription":"The path of the file to be read , the absolute path is prefered"
                        }
                    },
                    "required":["file_path"]
                }
            }
        }
]

write_file_schema=[
        { 
            "type":"function",
            "function":{
                "name":"write_file",
                "discription":"Erase all previous contents from a file or create a new file to write a new content, be careful about using this tool don't overwrite anything important",
                "parameters":{
                    "type":"object",
                    "properties":{
                       "file_name":{
                        "type":"string",
                        "discription":"The path of the file to be written , the absolute path is prefered"
                        },
                        "content":{
                        "type":"string",
                        "discription":"the new content to be written in the file"
                        }
                    }
                },
                "required":["file_path","content"]
            }
        }
]

edit_file_schema=[
        { 
            "type":"function",
            "function":{
                "name":"edit_file",
                "discription":"Replace a previous string in the file with a new string, there may be more than one occurence of the old string so make sure you added enough context or surrounding lines to make it unique",
                "parameters":{
                    "type":"object",
                    "properties":{
                       "file_name":{
                        "type":"string",
                        "discription":"The path of the file to be written , the absolute path is prefered"
                        },
                        "old_str":{
                        "type":"string",
                        "discription":"the old string to be replaced in the file"
                        },
                        "new_str":{
                        "type":"string",
                        "discription":"The new string to be replaced with in the file"
                        }
                    }
                },
                "required":["file_path","old_str","new_str"]
            }
        }
]

exec_command_schema=[
        { 
            "type":"function",
            "function":{
                "name":"exec_command",
                "discription":"execute a command in bash , the command is splited using shlex as command and arguments before executing, so don't use &&,|,*,;,chaining,background running",
                "parameters":{
                    "type":"object",
                    "properties":{
                       "command":{
                        "type":"string",
                        "discription":"The command to be executed"
                        }
                    }
                },
                "required":["command"]
            }
        }
]

all_tools_schema=list_file_schema+read_file_schema+write_file_schema+edit_file_schema+exec_command_schema
