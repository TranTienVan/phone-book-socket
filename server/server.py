import socket
import os
from _thread import *
from dotenv import load_dotenv
import re
import zipfile
import sqlite3
from datetime import datetime
import uuid
load_dotenv()
# client -> server (sdflasjkflad ) -> client
# 
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
    def log(ip, message):
        conn = sqlite3.connect('phone-book.db')
        data = [str(uuid.uuid4()), ip, datetime.now().strftime("%Y-%m-%d %H:%M:%M"), message]
        # Connect database
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT INTO log
            VALUES ('{}', '{}', '{}', '{}')
        """.format(data[0], data[1], data[2], data[3]))
        
        conn.commit()
        
        print("-".join(data[1:]))
        
        cursor.close()
        conn.close()
        
    while True:
        try:
            data = connection.recv(2048)
        except:
            break
        if data == b"@Exit()":
            break
        
        if data == b"@SelectAll":
            conn = sqlite3.connect('phone-book.db')
            
            # Connect database
            cursor = conn.cursor()
            cursor.execute("select id, name, phone, email, small_photo from member")
            members = cursor.fetchall()
            cursor.close()
            conn.close()
            
            # Send socket
            connection.sendall(" ||| ".join(["|".join(member) for member in members]).encode())
            
            
            zip_name = 'main.zip'
            
            # Compres image and send socket image
            with zipfile.ZipFile(zip_name, 'w') as file:
                for member in members:
                    file.write("." + member[4])
                    
            with open(zip_name, 'rb') as f:
                l = f.read()
                connection.sendall(l)
            
            os.remove(zip_name)
            log(address[0] + ":" + str(address[1]), "Selected all members successfully")
        
        # @Select:id
        
        if re.match("^@Select:\w\w\w\w\w\w\w\w$", data.decode()):
            conn = sqlite3.connect('phone-book.db')
            
            id = data.decode().split(":")[1]
            
            # Connect database
            cursor = conn.cursor()
            cursor.execute("select * from member where id = '{}'".format(id))
            members = cursor.fetchall()
            cursor.close()
            conn.close()
            
            if len(members) == 0:
                connection.send(b"Cannot find the member!")
                log(address[0] + ":" + str(address[1]), "Cannot find member {}".format(id))
                continue
            
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
            log(address[0] + ":" + str(address[1]), "Selected member {} successfully".format(id))
                
    connection.close()
    
    print('Client', address, 'disconnected')

def log(ip, message):
    conn = sqlite3.connect('phone-book.db')
    data = [str(uuid.uuid4()), ip, datetime.now().strftime("%Y-%m-%d %H:%M:%M"), message]
    # Connect database
    cursor = conn.cursor()
    
    cursor.execute("""
        INSERT INTO log
        VALUES ('{}', '{}', '{}', '{}')
    """.format(data[0], data[1], data[2], data[3]))
    
    conn.commit()
    
    print("-".join(data[1:]))
    
    cursor.close()
    conn.close()
    
while True:
    Client, address = ServerSocket.accept()
    
    # print('Connected to: ' + address[0] + ':' + str(address[1]))
    
    log(address[0] + ":" + str(address[1]), "User connected")
    start_new_thread(threaded_client, (Client, address))
    
    # print('Client', address, 'connected')
    log(address[0] + ":" + str(address[1]), "User disconnected")
    
ServerSocket.close()