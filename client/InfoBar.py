from PySide6.QtWidgets import QWidget, QLabel, QPushButton
from PySide6.QtCore import Signal, Slot
from PySide6 import QtCore
from PySide6.QtGui import QPixmap

from ui_infobar import Ui_Form

class InfoBar(QWidget, Ui_Form):
	Forward_sig = Signal(str)

	def __init__(self, parent=None):
		super(InfoBar, self).__init__(parent)
		self.ui = Ui_Form()
		self.ui.setupUi(self)

		self.forward_btn = self.findChild(QPushButton, "forward_btn")
	
	def setBar(self, member):
		try:
			data = member.split('|')
			self.ui.ID_name_out.setText(data[0] + ' - ' + data[1] + ' - ' + data[2])
			pixmap = QPixmap(data[-1][1:]).scaled(self.ui.small_picture_out.size(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
			self.ui.small_picture_out.setPixmap(pixmap)
		except:
			pass
	
	@Slot()
	def on_forward_btn_clicked(self):
		data = self.ui.ID_name_out.text().split(' - ')
		ID = data[0]
		self.Forward_sig.emit(str(ID))

