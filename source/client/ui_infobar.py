# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'infobar.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(680, 50)
        Form.setMinimumSize(QSize(0, 50))
        Form.setMaximumSize(QSize(16777215, 50))
        Form.setStyleSheet(u"@QWidget {\n"
"	background-color: rgb(240, 240, 240);\n"
"}")
        self.ID_name_out = QLineEdit(Form)
        self.ID_name_out.setObjectName(u"ID_name_out")
        self.ID_name_out.setGeometry(QRect(120, 15, 400, 20))
        font = QFont()
        font.setPointSize(12)
        self.ID_name_out.setFont(font)
        self.ID_name_out.setStyleSheet(u"QLineEdit {\n"
"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"}")
        self.ID_name_out.setReadOnly(True)
        self.ID_name_out.setClearButtonEnabled(False)
        self.small_picture_out = QLabel(Form)
        self.small_picture_out.setObjectName(u"small_picture_out")
        self.small_picture_out.setGeometry(QRect(70, 5, 40, 40))
        self.small_picture_out.setFont(font)
        self.forward_btn = QPushButton(Form)
        self.forward_btn.setObjectName(u"forward_btn")
        self.forward_btn.setGeometry(QRect(550, 5, 40, 40))
        self.forward_btn.setMinimumSize(QSize(40, 40))
        self.forward_btn.setMaximumSize(QSize(40, 40))
        self.forward_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.forward_btn.setStyleSheet(u"background-color: rgb(240, 162, 21);")
        icon = QIcon()
        icon.addFile(u"Resources/forward.png", QSize(), QIcon.Normal, QIcon.Off)
        self.forward_btn.setIcon(icon)
        self.forward_btn.setIconSize(QSize(25, 25))
        self.forward_btn.setFlat(False)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.ID_name_out.setText("")
        self.ID_name_out.setPlaceholderText("")
        self.small_picture_out.setText("")
#if QT_CONFIG(tooltip)
        self.forward_btn.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.forward_btn.setStatusTip(QCoreApplication.translate("Form", u"Back", None))
#endif // QT_CONFIG(statustip)
        self.forward_btn.setText("")
    # retranslateUi

