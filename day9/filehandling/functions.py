import os

def create(file_name):
    file = open(file_name,'w')
    file.close()
    
def write(file_name):
    text = input("enter content to write in file : ")
    try:
        with open(file_name,'a') as f:
            f.write(text)
        print("content added successfully")
    except Exception as e:
        print("Something went wrong", e)
        
def delete(file_name):
    if os.path.exists(file_name):
        os.remove(file_name)
        print("file  deleted successfully")
    else:
        print("file  does not exist")
        
def read(file_name):
    try:
        with open(file_name, 'r') as f:
            content = f.readlines()
        print(content)
    except Exception as e:
        print("Something went wrong:", e)
        