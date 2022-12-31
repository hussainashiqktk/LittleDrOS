from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QTextEdit, QPushButton
from PyQt5 import uic
import sys
import os
import subprocess

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi("./QtUI.ui", self)

        self.btnTurnOn = self.findChild(QPushButton, "btn_turn_on")
        self.btnTurnOff = self.findChild(QPushButton, "btn_turn_off")
        self.lblStatus = self.findChild(QLabel, "lbl_status")

        self.btnTurnOn.clicked.connect(self.turn_on)
        self.btnTurnOff.clicked.connect(self.turn_off)

        self.show()

    def turn_off(self):
        os.system("sc stop WinDefend")
        self.lblStatus.setStyleSheet('color: red')
        self.lblStatus.setText("STOPPED")

    def turn_on(self):
        os.system("sc start WinDefend")
        self.lblStatus.setStyleSheet('color: green')
        self.lblStatus.setText("RUNNING")


    def check_defender_status():
        output = subprocess.run(["powershell.exe", "Get-MpComputerStatus"], capture_output=True).stdout
        return "Enabled" in output.decode()


# ---------------------


app = QApplication(sys.argv)
window = UI()

# ------------------------

app.exec_()
