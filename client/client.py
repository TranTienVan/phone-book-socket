import socket
from dotenv import load_dotenv
import os
import zipfile
import shutil
import time

load_dotenv()

PREFIX_PATH = os.environ.get("PREFIX_PATH")
ClientSocket = socket.socket()
host = '127.0.0.1'
port = 1233


try:
    ClientSocket.connect((host, port))
    print("Connected to server")
except socket.error as e:
    print(str(e))

# Response = ClientSocket.recv(2048)
# print(Response.decode('utf-8'))

# while True:
#     try:
#         Input = input('Say Something: ')
#         ClientSocket.send(str.encode(Input))
#         if Input == "@Exit()":
#             break
#         Response = ClientSocket.recv(2048)
#         print(Response.decode('utf-8'))
#     except:
#         ClientSocket.send(b"@Exit()")
#         break
    
def SelectAll():
    ClientSocket.send(b"@SelectAll")
    
    chunk = ClientSocket.recv(2048)
    
    members = chunk.decode().split(" ||| ")
    
    time.sleep(2)
    # Receive Images
    with open("main.zip", 'wb') as f:
        l = ClientSocket.recv(2048)
    
        while(l):
            f.write(l)
            if len(l) < 2048:
                break
            l = ClientSocket.recv(2048)
            

    with zipfile.ZipFile("main.zip",  'r') as file:
        file.extractall()
    
    os.remove("main.zip")
    print("Selected all successfully".format(id))
        
    return members
        
def Select(id):
    ClientSocket.send("@Select:{}".format(id).encode())
    
    # Receive text
    chunk = ClientSocket.recv(2048)
    
    if chunk == b"Cannot find the member!":
        print(chunk.decode())
        return
    member = chunk.decode()
    id, name, phone, email, large_photo, small_photo, zip_photo = member.split("|")
    
    
    # Receive Images
    with open(zip_photo, 'wb') as f:
        l = ClientSocket.recv(2048)
    
        while(l):
            f.write(l)
            if len(l) < 2048:
                break
            l = ClientSocket.recv(2048)
            

    with zipfile.ZipFile(zip_photo,  'r') as file:
        
        file.extractall()
        
    os.remove(zip_photo)
    print("Selected {} successfully".format(id))
    
    return [id, name, phone, email, large_photo, small_photo, zip_photo]

def save_images(origin, destination):
    shutil.copy(origin, destination)
    
    return True

mems = SelectAll()
print(mems)

ClientSocket.send(b'@Exit()')
ClientSocket.close()