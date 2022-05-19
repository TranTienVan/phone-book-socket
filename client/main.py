import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QScrollArea
from PySide6.QtCore import QFile
from PySide6.QtGui import QIcon, QPixmap
import ClientSocket

from ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.setWindowIcon(QIcon(QPixmap("Resources\\phobo.png")))
		self.setWindowTitle("Phobo")
		
		self.scrollArea = self.findChild(QScrollArea, "scrollArea")
		self.scrollArea.setWidgetResizable(True)
		


	


if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = MainWindow()
	window.show()

	sys.exit(app.exec())