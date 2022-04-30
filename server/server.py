from distutils.sysconfig import PREFIX
import socket
import os
from _thread import *
import psycopg2
from dotenv import load_dotenv
import re
import zipfile

load_dotenv()

ServerSocket = socket.socket()
host = os.environ.get("HOST")
port = int(os.environ.get("PORT"))

try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Waitiing for a Connection..')
ServerSocket.listen(5)
# https://codezup.com/socket-server-with-multiple-clients-model-multithreading-python/

def threaded_client(connection, address):
    # Set up secret key
    POSTGRES_HOST = os.environ.get("POSTGRES_HOST")
    POSTGRES_USERNAME = os.environ.get("POSTGRES_USERNAME")
    POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
    POSTGRES_DATABASE_NAME = os.environ.get("POSTGRES_DATABASE_NAME")
    PREFIX_PATH = os.environ.get("PREFIX_PATH")
    
    while True:
        try:
            data = connection.recv(2048)
        except:
            break
        if data == b"@Exit()":
            break
        
        if data == b"@SelectAll":
            conn = psycopg2.connect(
                host=POSTGRES_HOST,
                database=POSTGRES_DATABASE_NAME,
                user=POSTGRES_USERNAME,
                password=POSTGRES_PASSWORD
            )
            
            # Connect database
            cursor = conn.cursor()
            cursor.execute("select id, name, phone, email from member")
            members = cursor.fetchall()
            cursor.close()
            conn.close()
            
            # Send socket
            connection.sendall(" ||| ".join(["|".join(member) for member in members]).encode())
            
            continue
        
        # @Select:id
        
        if re.match("^@Select:\d\d\d\d\d\d\d\d$", data.decode()):
            conn = psycopg2.connect(
                host=POSTGRES_HOST,
                database=POSTGRES_DATABASE_NAME,
                user=POSTGRES_USERNAME,
                password=POSTGRES_PASSWORD
            )
            
            id = data.decode().split(":")[1]
            
            # Connect database
            cursor = conn.cursor()
            cursor.execute("select * from member where id = %s", (id, ))
            members = cursor.fetchall()
            cursor.close()
            conn.close()
            
            
            large_photo_path = members[0][4]
            small_photo_path = members[0][5]
            
            member = "|".join(members[0])
            zip_name = 'main.zip'
            member += "|" + zip_name
            
            # Send socket text
            connection.send(member.encode())
            
            # Compres image and send socket image
            with zipfile.ZipFile(zip_name, 'w') as file:
                
                file.write("." + large_photo_path)
                file.write("." + small_photo_path)
            
            
            with open(zip_name, 'rb') as f:
                l = f.read()
                connection.sendall(l)
            
            os.remove(zip_name)
                
                    
        
        
        
    connection.close()
    
    print('Client', address, 'disconnected')

while True:
    Client, address = ServerSocket.accept()
    
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(threaded_client, (Client, address))
    
    print('Client', address, 'connected')
    
ServerSocket.close()