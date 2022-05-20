# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStackedWidget, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(700, 550)
        MainWindow.setMinimumSize(QSize(700, 550))
        MainWindow.setMaximumSize(QSize(700, 550))
        MainWindow.setStyleSheet(u"QObject {\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame_top = QFrame(self.centralwidget)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setGeometry(QRect(0, 0, 700, 100))
        self.frame_top.setMinimumSize(QSize(0, 100))
        self.frame_top.setMaximumSize(QSize(16777215, 100))
        self.frame_top.setStyleSheet(u"")
        self.frame_top.setFrameShape(QFrame.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_top)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(25, 21, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_2)

        self.about_us_btn = QPushButton(self.frame_top)
        self.about_us_btn.setObjectName(u"about_us_btn")
        self.about_us_btn.setMinimumSize(QSize(100, 100))
        self.about_us_btn.setMaximumSize(QSize(100, 100))
        self.about_us_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.about_us_btn.setStyleSheet(u"")
        self.about_us_btn.setText(u"")
        icon = QIcon()
        icon.addFile(u"Resources/phobo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.about_us_btn.setIcon(icon)
        self.about_us_btn.setIconSize(QSize(100, 100))
        self.about_us_btn.setCheckable(False)
        self.about_us_btn.setFlat(True)

        self.horizontalLayout_8.addWidget(self.about_us_btn)

        self.horizontalSpacer_3 = QSpacerItem(25, 21, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_3)

        self.label_1 = QLabel(self.frame_top)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setMinimumSize(QSize(80, 25))
        self.label_1.setMaximumSize(QSize(80, 25))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_1.setFont(font)
        self.label_1.setStyleSheet(u"color: rgb(85, 147, 161);")
        self.label_1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_1)

        self.host_inp = QLineEdit(self.frame_top)
        self.host_inp.setObjectName(u"host_inp")
        self.host_inp.setMinimumSize(QSize(150, 25))
        self.host_inp.setMaximumSize(QSize(16777215, 25))
        font1 = QFont()
        font1.setPointSize(12)
        self.host_inp.setFont(font1)
        self.host_inp.setStyleSheet(u"QLineEdit {\n"
"	border-color: rgb(85, 147, 161);\n"
"}")

        self.horizontalLayout_8.addWidget(self.host_inp)

        self.label_2 = QLabel(self.frame_top)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(50, 25))
        self.label_2.setMaximumSize(QSize(50, 25))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: rgb(85, 147, 161);")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_2)

        self.port_inp = QLineEdit(self.frame_top)
        self.port_inp.setObjectName(u"port_inp")
        self.port_inp.setMinimumSize(QSize(100, 25))
        self.port_inp.setMaximumSize(QSize(16777215, 25))
        self.port_inp.setFont(font1)

        self.horizontalLayout_8.addWidget(self.port_inp)

        self.horizontalSpacer_4 = QSpacerItem(25, 21, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_4)

        self.plug_btn = QPushButton(self.frame_top)
        self.plug_btn.setObjectName(u"plug_btn")
        self.plug_btn.setMinimumSize(QSize(40, 40))
        self.plug_btn.setMaximumSize(QSize(40, 40))
        self.plug_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.plug_btn.setStyleSheet(u"background-color: rgb(85, 147, 161);")
        icon1 = QIcon()
        icon1.addFile(u"Resources/plug.png", QSize(), QIcon.Normal, QIcon.Off)
        self.plug_btn.setIcon(icon1)
        self.plug_btn.setIconSize(QSize(25, 25))
        self.plug_btn.setFlat(False)

        self.horizontalLayout_8.addWidget(self.plug_btn)

        self.horizontalSpacer_1 = QSpacerItem(50, 21, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_1)

        self.frame_mid = QFrame(self.centralwidget)
        self.frame_mid.setObjectName(u"frame_mid")
        self.frame_mid.setGeometry(QRect(0, 100, 700, 50))
        self.frame_mid.setMinimumSize(QSize(0, 50))
        self.frame_mid.setMaximumSize(QSize(16777215, 50))
        self.frame_mid.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(239, 232, 206);\n"
"}")
        self.frame_mid.setFrameShape(QFrame.NoFrame)
        self.frame_mid.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_mid)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_7 = QSpacerItem(25, 21, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_7)

        self.label_3 = QLabel(self.frame_mid)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(100, 25))
        self.label_3.setMaximumSize(QSize(100, 25))
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: rgb(212, 76, 57);")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_3)

        self.horizontalSpacer_9 = QSpacerItem(25, 21, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_9)

        self.search_inp = QLineEdit(self.frame_mid)
        self.search_inp.setObjectName(u"search_inp")
        self.search_inp.setMinimumSize(QSize(150, 25))
        self.search_inp.setMaximumSize(QSize(16777215, 25))
        self.search_inp.setFont(font1)
#if QT_CONFIG(tooltip)
        self.search_inp.setToolTip(u"<html><head/><body><p>Enter ID of an member or '<span style=\" color:#5500ff;\">@All</span>' to select all members.</p></body></html>")
#endif // QT_CONFIG(tooltip)
        self.search_inp.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.search_inp.setMaxLength(20)
        self.search_inp.setClearButtonEnabled(False)

        self.horizontalLayout_10.addWidget(self.search_inp)

        self.horizontalSpacer_6 = QSpacerItem(25, 21, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_6)

        self.search_btn = QPushButton(self.frame_mid)
        self.search_btn.setObjectName(u"search_btn")
        self.search_btn.setMinimumSize(QSize(40, 40))
        self.search_btn.setMaximumSize(QSize(40, 40))
        self.search_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.search_btn.setStyleSheet(u"background-color: rgb(212, 76, 57);")
        icon2 = QIcon()
        icon2.addFile(u"Resources/search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.search_btn.setIcon(icon2)
        self.search_btn.setIconSize(QSize(25, 25))
        self.search_btn.setFlat(False)

        self.horizontalLayout_10.addWidget(self.search_btn)

        self.horizontalSpacer_8 = QSpacerItem(50, 21, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_8)

        self.log = QLabel(self.centralwidget)
        self.log.setObjectName(u"log")
        self.log.setGeometry(QRect(150, 155, 431, 20))
        font2 = QFont()
        font2.setPointSize(10)
        self.log.setFont(font2)
        self.pages = QStackedWidget(self.centralwidget)
        self.pages.setObjectName(u"pages")
        self.pages.setGeometry(QRect(10, 180, 681, 361))
        self.pages.setStyleSheet(u"")
        self.search_page = QWidget()
        self.search_page.setObjectName(u"search_page")
        self.scrollArea = QScrollArea(self.search_page)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(0, 0, 681, 361))
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 662, 359))
        self.scrollAreaWidgetContents.setStyleSheet(u"@QVBoxLayout {\n"
"border: none;\n"
"\n"
"}")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.pages.addWidget(self.search_page)
        self.info_page = QWidget()
        self.info_page.setObjectName(u"info_page")
        self.label = QLabel(self.info_page)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(280, 30, 80, 20))
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(240, 162, 21);")
        self.label_4 = QLabel(self.info_page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(280, 80, 80, 20))
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"color: rgb(240, 162, 21);")
        self.label_5 = QLabel(self.info_page)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(280, 130, 80, 20))
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"color: rgb(240, 162, 21);")
        self.label_6 = QLabel(self.info_page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(310, 170, 25, 25))
        self.label_6.setStyleSheet(u"")
        self.label_6.setPixmap(QPixmap(u"Resources/phone.png"))
        self.label_6.setScaledContents(True)
        self.label_7 = QLabel(self.info_page)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(310, 210, 25, 25))
        self.label_7.setStyleSheet(u"image: url(:/icons/Resources/mail.png);")
        self.label_7.setPixmap(QPixmap(u"Resources/mail.png"))
        self.label_7.setScaledContents(True)
        self.big_picture_out = QLabel(self.info_page)
        self.big_picture_out.setObjectName(u"big_picture_out")
        self.big_picture_out.setGeometry(QRect(30, 30, 200, 200))
        self.big_picture_out.setStyleSheet(u"border-color: rgb(240, 162, 21);")
        self.ID_out = QLineEdit(self.info_page)
        self.ID_out.setObjectName(u"ID_out")
        self.ID_out.setGeometry(QRect(370, 30, 300, 20))
        self.ID_out.setFont(font1)
        self.ID_out.setStyleSheet(u"QLineEdit {\n"
"border: none;\n"
"\n"
"}")
        self.ID_out.setReadOnly(True)
        self.ID_out.setClearButtonEnabled(False)
        self.back_btn = QPushButton(self.info_page)
        self.back_btn.setObjectName(u"back_btn")
        self.back_btn.setGeometry(QRect(610, 310, 40, 40))
        self.back_btn.setMinimumSize(QSize(40, 40))
        self.back_btn.setMaximumSize(QSize(40, 40))
        self.back_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.back_btn.setStyleSheet(u"background-color: rgb(240, 162, 21);")
        icon3 = QIcon()
        icon3.addFile(u"Resources/back.png", QSize(), QIcon.Normal, QIcon.Off)
        self.back_btn.setIcon(icon3)
        self.back_btn.setIconSize(QSize(25, 25))
        self.back_btn.setFlat(False)
        self.name_out = QLineEdit(self.info_page)
        self.name_out.setObjectName(u"name_out")
        self.name_out.setGeometry(QRect(370, 80, 300, 20))
        self.name_out.setFont(font1)
        self.name_out.setStyleSheet(u"QLineEdit {\n"
"border: none;\n"
"\n"
"}")
        self.name_out.setReadOnly(True)
        self.name_out.setClearButtonEnabled(False)
        self.phone_out = QLineEdit(self.info_page)
        self.phone_out.setObjectName(u"phone_out")
        self.phone_out.setGeometry(QRect(370, 170, 300, 20))
        self.phone_out.setFont(font1)
        self.phone_out.setStyleSheet(u"QLineEdit {\n"
"border: none;\n"
"\n"
"}")
        self.phone_out.setReadOnly(True)
        self.phone_out.setClearButtonEnabled(False)
        self.mail_out = QLineEdit(self.info_page)
        self.mail_out.setObjectName(u"mail_out")
        self.mail_out.setGeometry(QRect(370, 210, 300, 20))
        self.mail_out.setFont(font1)
        self.mail_out.setStyleSheet(u"QLineEdit {\n"
"border: none;\n"
"\n"
"}")
        self.mail_out.setReadOnly(True)
        self.mail_out.setClearButtonEnabled(False)
        self.pages.addWidget(self.info_page)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.pages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.about_us_btn.setToolTip(QCoreApplication.translate("MainWindow", u"About Us", None))
#endif // QT_CONFIG(tooltip)
        self.label_1.setText(QCoreApplication.translate("MainWindow", u"Server IP", None))
        self.host_inp.setText(QCoreApplication.translate("MainWindow", u"127.0.0.1", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Port", None))
        self.port_inp.setText(QCoreApplication.translate("MainWindow", u"1233", None))
#if QT_CONFIG(tooltip)
        self.plug_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Connect", None))
#endif // QT_CONFIG(tooltip)
        self.plug_btn.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.search_inp.setText("")
        self.search_inp.setPlaceholderText("")
#if QT_CONFIG(tooltip)
        self.search_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Search", None))
#endif // QT_CONFIG(tooltip)
        self.search_btn.setText("")
        self.log.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Contact", None))
        self.label_6.setText("")
        self.label_7.setText("")
        self.big_picture_out.setText("")
        self.ID_out.setText("")
        self.ID_out.setPlaceholderText("")
#if QT_CONFIG(tooltip)
        self.back_btn.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.back_btn.setStatusTip(QCoreApplication.translate("MainWindow", u"Back", None))
#endif // QT_CONFIG(statustip)
        self.back_btn.setText("")
        self.name_out.setText("")
        self.name_out.setPlaceholderText("")
        self.phone_out.setText("")
        self.phone_out.setPlaceholderText("")
        self.mail_out.setText("")
        self.mail_out.setPlaceholderText("")
    # retranslateUi

