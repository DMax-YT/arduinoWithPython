# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui',
# licensing of 'design.ui' applies.
#
# Created: Tue Aug 20 21:33:36 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(305, 225)
        MainWindow.setStyleSheet(
            "*{\n"
            "    font-family: sans-serif;\n"
            "}\n"
            "QLabel {\n"
            "    font-size: 20px;\n"
            "}"
        )
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 10, 285, 167))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.blink = QtWidgets.QPushButton(self.widget)
        self.blink.setObjectName("blink")
        self.gridLayout.addWidget(self.blink, 9, 2, 1, 2)
        self.btn_connect = QtWidgets.QPushButton(self.widget)
        self.btn_connect.setObjectName("btn_connect")
        self.gridLayout.addWidget(self.btn_connect, 8, 3, 1, 1)
        self.status = QtWidgets.QLabel(self.widget)
        self.status.setObjectName("status")
        self.gridLayout.addWidget(self.status, 8, 0, 1, 1)
        self.speed = QtWidgets.QLabel(self.widget)
        self.speed.setMinimumSize(QtCore.QSize(61, 21))
        self.speed.setStyleSheet("")
        self.speed.setWordWrap(False)
        self.speed.setObjectName("speed")
        self.gridLayout.addWidget(self.speed, 5, 1, 1, 3)
        self.ports_list = QtWidgets.QComboBox(self.widget)
        self.ports_list.setObjectName("ports_list")
        self.gridLayout.addWidget(self.ports_list, 1, 0, 1, 4)
        self.connect_disconnect = QtWidgets.QLabel(self.widget)
        self.connect_disconnect.setObjectName("connect_disconnect")
        self.gridLayout.addWidget(self.connect_disconnect, 8, 1, 1, 1)
        self.on_off = QtWidgets.QPushButton(self.widget)
        self.on_off.setObjectName("on_off")
        self.gridLayout.addWidget(self.on_off, 9, 0, 1, 1)
        self.speed_list = QtWidgets.QComboBox(self.widget)
        self.speed_list.setObjectName("speed_list")
        self.gridLayout.addWidget(self.speed_list, 6, 0, 1, 4)
        self.ports = QtWidgets.QLabel(self.widget)
        self.ports.setMinimumSize(QtCore.QSize(61, 21))
        self.ports.setStyleSheet("")
        self.ports.setWordWrap(False)
        self.ports.setObjectName("ports")
        self.gridLayout.addWidget(self.ports, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 303, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Тест", None, -1))
        self.blink.setText(QtWidgets.QApplication.translate("MainWindow", "Мигать", None, -1))
        self.btn_connect.setText(QtWidgets.QApplication.translate("MainWindow", "Подключиться", None, -1))
        self.status.setText(QtWidgets.QApplication.translate("MainWindow", "Статус:", None, -1))
        self.speed.setText(QtWidgets.QApplication.translate("MainWindow", "Скорость:", None, -1))
        self.connect_disconnect.setText(QtWidgets.QApplication.translate("MainWindow", "Отключено", None, -1))
        self.on_off.setText(QtWidgets.QApplication.translate("MainWindow", "Включить", None, -1))
        self.ports.setText(QtWidgets.QApplication.translate("MainWindow", "Порт:", None, -1))
