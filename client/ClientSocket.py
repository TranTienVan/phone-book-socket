from asyncio import constants
import socket
from dotenv import load_dotenv
import os
import zipfile
import shutil
import time

class ClientSocket:
	def __init__(self):
		self.socket = socket.socket()

	def connect(self, host, port):
		try:
			self.socket.connect((host, port))
			return True, "Successfully connected!"

		except:
			return False, "Failed to connect to host"

	def SelectAll(self):
		self.socket.send(b"@SelectAll")
		
		chunk = self.socket.recv(2048)
		
		members = chunk.decode().split(" ||| ")
		
		time.sleep(2)
		# Receive Images
		with open("main.zip", 'wb') as f:
			l = self.socket.recv(2048)
		
			while(l):
				f.write(l)
				if len(l) < 2048:
					break
				l = self.socket.recv(2048)
				
		with zipfile.ZipFile("main.zip",  'r') as file:
			file.extractall()
		
		os.remove("main.zip")
		return members, "Selected all successfully!"

	def Select(self, id):
		ClientSocket.send("@Select:{}".format(id).encode())
		
		# Receive text
		chunk = ClientSocket.recv(2048)
		
		if chunk == b"Cannot find the member!":
			return None, "Cannot find the member!"
		
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
		
		return [id, name, phone, email, large_photo, small_photo, zip_photo], "Selected {} successfully!".format(id)

	def saveImages(self, origin, destination):
		shutil.copy(origin, destination)

		return True

	def __del__(self):
		self.socket.send(b'@Exit()')
		self.socket.close()