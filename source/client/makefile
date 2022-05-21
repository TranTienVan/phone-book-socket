all: ui_mainwindow.py ui_infobar.py
#	pyinstaller -n Phobo -F -w -i Resources/phobo.ico main.py
	python main.py

ui_mainwindow.py: mainwindow.ui
	pyside6-uic mainwindow.ui > ui_mainwindow.py

ui_infobar.py: infobar.ui
	pyside6-uic infobar.ui > ui_infobar.py