import sys, os

from PySide6.QtWidgets import QApplication, QMainWindow, QScrollArea, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QStackedWidget
from PySide6.QtCore import Signal, Slot
from PySide6.QtGui import QIcon, QPixmap
from PySide6 import QtCore

import ClientSocket as cs
import utilities as util
import InfoBar as ib

from ui_mainwindow import Ui_MainWindow

COOKIE_PATH = "cookies.json"
MAX_QUERY_SIZE = 8

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

		self.big_picture_out = self.findChild(QLabel, "big_picture_out")
		self.ID_out = self.findChild(QLineEdit, "ID_out")
		self.name_out = self.findChild(QLineEdit, "name_out")
		self.phone_out = self.findChild(QLineEdit, "phone_out")
		self.mail_out = self.findChild(QLineEdit, "mail_out")
		self.picture_path_out = self.findChild(QLineEdit, "picture_path_out")
		
		self.scrollArea = self.findChild(QScrollArea, "scrollArea")
		self.pages = self.findChild(QStackedWidget, "pages")
		self.search_page = self.findChild(QWidget, "search_page")
		self.info_page = self.findChild(QWidget, "info_page")
		self.scrollWidget = self.findChild(QWidget, "scrollWidget")
		self.scrollArea.setWidgetResizable(True)

		self.vbox = QVBoxLayout()
		self.scrollWidget.setLayout(self.vbox)

		# Socket initiation
		self.socket = cs.ClientSocket()
		# Connecting server
		host, port = util.load_server_info(COOKIE_PATH)
		self.host_inp.setText(host)
		self.port_inp.setText(str(port))
		
		self.connected = False
		self.scroll_page_content_init_ed = False

		# Set search page as default
		self.pages.setCurrentWidget(self.search_page)

	def InitSrcollPage(self, members):
		try:
#			self.vbox = QVBoxLayout()
			self.clear_vboxlayout()
			for member in members:
				object = ib.InfoBar()
				object.setBar(member)
				self.vbox.addWidget(object)
				object.Forward_sig.connect(self.forward_btn_clicked)

#			self.scrollWidget.setLayout(self.vbox)

			self.scroll_page_content_init_ed = True
			self.pages.setCurrentWidget(self.search_page)
			self.show()
		except:
			pass
	
	def InitInfoPage(self, member):
		try:
			# member[] = [id, name, phone, email, large_photo, small_photo, zip_photo]
			self.ID_out.setText(member[0])
			self.name_out.setText(member[1])
			self.phone_out.setText(member[2])
			self.mail_out.setText(member[3])
			self.picture_path_out.setText(os.getcwd() + member[4])
			
			pixmap = QPixmap(member[4][1:]).scaled(self.big_picture_out.size(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
			self.big_picture_out.setPixmap(pixmap)
			self.pages.setCurrentWidget(self.info_page)
			self.show()
		except:
			pass
		
	def notic(self, flag: bool, msg: str):
		self.log.setText(msg)
		
		if flag:
			self.log.setStyleSheet("color:green")
		else:
			self.log.setStyleSheet("color:red")

		self.show()

	def clear_content(self):
		self.search_inp.clear()
		self.big_picture_out.clear()
		self.ID_out.clear()
		self.name_out.clear()
		self.phone_out.clear()
		self.mail_out.clear()
		self.picture_path_out.clear()
		self.scroll_page_content_init_ed = False
		self.pages.setCurrentWidget(self.search_page)

	def clear_vboxlayout(self):
		while self.vbox.count():
			widget = self.vbox.takeAt(0).widget()
			widget.setParent(None)
			widget.deleteLater()

	@Slot()
	def on_plug_btn_clicked(self):
		host = str(self.host_inp.text()).strip()
		port = int(self.port_inp.text())

		self.socket.close()
		self.socket = cs.ClientSocket()

		connected, err = self.socket.connect(host, port)
		self.notic(connected, err)

		if connected:
			self.connected = True
			util.store_server_info(COOKIE_PATH, host, port)
		else:
			self.connected = False
			self.clear_content()
			self.clear_vboxlayout()
			self.show()

	@Slot()
	def on_search_btn_clicked(self):
		if not self.connected:
			self.notic(False, "Server not connected.")

		query = str(self.search_inp.text()).strip()

		if len(query) > MAX_QUERY_SIZE:
			self.notic(False, "Too many characters!")
			return

		if query == "":
			return
		elif query == "@All":
			ok, msg, members = self.socket.SelectAll()
			self.notic(ok, msg)

			if ok:
				self.InitSrcollPage(members)
		else:
			ok, msg, member = self.socket.Select(query)
			self.notic(ok, msg)

			if ok:
				self.InitInfoPage(member)


	@Slot()
	def on_about_us_btn_clicked(self):
		f = True
		#TODO

	@Slot(str)
	def forward_btn_clicked(self, ID):
		if not self.connected:
			self.notic(False, "Server not connected.")

		ok, msg, member = self.socket.Select(ID)
		self.notic(ok, msg)

		if ok:
			self.InitInfoPage(member)
	
	@Slot()
	def on_back_btn_clicked(self):
		if self.scroll_page_content_init_ed:
			self.pages.setCurrentWidget(self.search_page)

###########################################################

if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = MainWindow()
	window.show()

	sys.exit(app.exec())