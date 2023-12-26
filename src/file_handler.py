from os import  listdir , mkdir
from os.path import exists , join

BUFFER_SIZE = 8192 

def already_exist(PATH:str,file_name:str) -> None:
   if exists(PATH):
         files = listdir(PATH)
         if file_name in files:
            return True
   else:
      mkdir(PATH)
   return False

def write_summary(folder_path:str,file_name:str,summary:str) -> None:
   text_path = join(folder_path , file_name)
   with open(text_path ,'w',buffering=BUFFER_SIZE) as file:
      file.write(summary)
   return 

def read_summary(file_path:str) -> None:
   with open(file_path , 'r') as file:
      text = file.read()
      print(text)
   return 