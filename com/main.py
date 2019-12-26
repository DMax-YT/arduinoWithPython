import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtGui import QIcon
from com.design import Ui_MainWindow
from com import get_ports
import serial


class MainWindow(QMainWindow):
    connected = False
    led_on = False
    led_blinking = False

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.ports_list.addItems(get_ports.serial_ports())
        # self.ui.speed_list.addItems(get_ports.speed)
        for speed in get_ports.speed:
            self.ui.speed_list.addItem(str(speed))
        self.ui.connect_disconnect.setStyleSheet('font-size: 18px;')
        self.ui.ports.setStyleSheet('text-align: center;')
        self.ui.speed.setStyleSheet('text-align: center;')
        self.realport = None
        self.ui.btn_connect.clicked.connect(self.connect_arduino)
        self.ui.on_off.clicked.connect(self.led_power)
        self.ui.blink.clicked.connect(self.led_blink)

    def connect_arduino(self):
        if not self.connected:
            try:
                self.realport = serial.Serial(self.ui.ports_list.currentText(), int(self.ui.speed_list.currentText()))
                self.ui.btn_connect.setText('Отключиться')
                self.ui.connect_disconnect.setText('Подключено')
                self.connected = True
            except Exception as e:
                print(e)
        else:
            try:
                self.realport.write(b'd')
                self.realport.close()
                self.ui.blink.setText('Мигать')
                self.ui.on_off.setText('Включить')
                self.ui.btn_connect.setText('Подключиться')
                self.ui.connect_disconnect.setText('Отключено')
                self.connected = False
            except Exception as e:
                print(e)

    def led_power(self):
        if not self.led_on:
            if self.realport:
                self.realport.write(b'e')
                self.led_on = True
                self.led_blinking = False
                self.ui.on_off.setText('Выключить')
                self.ui.blink.setText('Мигать')
            else:
                self.connect_arduino()
        else:
            if self.realport:
                self.realport.write(b'd')
                self.led_on = False
                self.ui.on_off.setText('Включить')
            else:
                self.connect_arduino()

    def led_blink(self):
        if not self.led_blinking:
            if self.realport:
                self.realport.write(b'b')
                self.led_blinking = True
                self.led_on = False
                self.ui.blink.setText('Выключить')
                self.ui.on_off.setText('Включить')
            else:
                self.connect_arduino()
        else:
            if self.realport:
                self.realport.write(b'd')
                self.led_blinking = False
                self.ui.blink.setText('Мигать')
            else:
                self.connect_arduino()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    window.setWindowIcon(QIcon('icon.png'))

    sys.exit(app.exec_())
