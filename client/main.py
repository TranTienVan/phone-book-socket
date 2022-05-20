from http.cookiejar import Cookie
from socket import socket
import sys
from turtle import forward
from PySide6.QtWidgets import QApplication, QMainWindow, QScrollArea, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PySide6.QtCore import Signal, Slot
from PySide6.QtGui import QIcon, QPixmap, QCloseEvent

import ClientSocket as cs
import utilities as util
import InfoBar as ib

from ui_mainwindow import Ui_MainWindow

COOKIE_PATH = "cookies.json"

class MainWindow(QMainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.setWindowIcon(QIcon(QPixmap("Resources\\phobo.png")))
		self.setWindowTitle("Phobo")
		
		# Get child QObjects
		self.host_inp = self.findChild(QLineEdit, "host_inp")
		self.port_inp = self.findChild(QLineEdit, "port_inp")
		self.search_inp = self.findChild(QLineEdit, "search_inp")

		self.about_us_btn = self.findChild(QPushButton, "about_us_btn")
		self.plug_btn = self.findChild(QPushButton, "plug_btn")
		self.search_btn = self.findChild(QPushButton, "search_btn")
		self.back_btn = self.findChild(QPushButton, "back_btn")

		self.log = self.findChild(QLabel, "log")
		
		# Socket initiation
		self.socket = cs.ClientSocket()
		# Connecting server
		host, port = util.load_server_info(COOKIE_PATH)
		self.host_inp.setText(host)
		self.port_inp.setText(str(port))
		self.connected = False


	def InitSrcollPage(self, members):
		self.scroll = self.findChild(QScrollArea, "scrollArea")
		self.widget = QWidget()
		self.vbox = QVBoxLayout()

		for member in members:
			object = ib.InfoBar()
			object.setBar(member)
			self.vbox.addWidget(object)
			object.Forward_sig.connect(self.forward_btn_clicked)

		self.widget.setLayout(self.vbox)
		self.scroll.setWidgetResizable(True)
		self.scroll.setWidget(self.widget)

		self.show()
	
	def InitInfoPage(self, member):
		self.big_picture_out = self.findChild(QLabel, "big_picture_out")
		self.ID_out = self.findChild(QLineEdit, "ID_out")
		self.name_out = self.findChild(QLineEdit, "name_out")
		self.phone_out = self.findChild(QLineEdit, "phone_out")
		self.mail_out = self.findChild(QLineEdit, "mail_out")

		pixmap = QPixmap()
		#TODO

	def notic(self, flag: bool, msg: str):
		self.log.setText(msg)
		
		if flag:
			self.log.setStyleSheet("color:green")
		else:
			self.log.setStyleSheet("color:red")

		self.show()

	
	@Slot()
	def on_plug_btn_clicked(self):
		host = str(self.host_inp.text()).strip()
		port = int(self.port_inp.text())

		self.socket.close()
#		print(host, type(host)) #debug
#		print(port, type(port)) #debug
		connected, err = self.socket.connect(host, port)
		self.notic(connected, err)

		if connected:
			self.connected = True
			util.store_server_info(COOKIE_PATH, host, port)
		else:
			self.connected = False

	
	@Slot()
	def on_search_btn_clicked(self):
		if not self.connected:
			self.notic(False, "Server not connected.")

		query = str(self.search_inp.text()).strip()

		if query == "@All":
			ok, msg, members = self.socket.SelectAll()
			self.InitSrcollPage(members)

	@Slot()
	def on_about_us_btn_clicked(self):
		f = True
		#TODO

	@Slot(str)
	def forward_btn_clicked(self, ID):
		#s = self.sender()
		print(ID)
		# send ID


if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = MainWindow()
	window.show()

	sys.exit(app.exec())