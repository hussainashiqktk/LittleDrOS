from PyQt5.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget

def button_clicked():
    print("Button clicked!")

app = QApplication([])
window = QWidget()
layout = QVBoxLayout(window)

button = QPushButton("Click me!")
button.clicked.connect(button_clicked)
layout.addWidget(button)

window.show()
app.exec_()
