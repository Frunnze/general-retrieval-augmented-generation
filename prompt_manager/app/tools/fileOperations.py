import mimetypes
from chardet import detect
import os

def detect_encoding(filePath : str):
    with open(filePath, 'rb') as file:
        content = file.read()

    encoding = detect(content)
    return encoding['encoding']

def read_file_content(filePath : str):
    if not os.path.exists(filePath):
        return f"Error : File {filePath} does not exist"

    type,_ = mimetypes.guess_type(url=filePath)
    
    if not type.startswith('text') or type is None:
        return f"Error : Cannot read file with {type} filetype"
    
    try:
        with open(filePath, 'r', encoding='utf-8') as file:
            content = file.read()
    except UnicodeDecodeError as e:
        print(f"Error : Cannot decode {filePath} file with UTF-8")

        with open(filePath, 'r', encoding=detect_encoding(filePath)) as file:
            content = file.read()

    return content.strip()

# print(read_file_content(r"app\tools\embeddor.py"))