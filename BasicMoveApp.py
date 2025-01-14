import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QHBoxLayout, QVBoxLayout

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Arm Basic Control App")
        b1=QPushButton('Grip')
        b2=QPushButton('Ungrip')
        b3=QPushButton('Move Left')
        b4=QPushButton('Move Right')
        b5=QPushButton('Move Up')
        b6=QPushButton('Move Down')
        layout1 = QVBoxLayout()
        layout2 = QHBoxLayout()
        layout3 = QVBoxLayout()
        layout1.addWidget(b1)
        layout1.addWidget(b2)
        layout1.addWidget(b3)
        layout3.addWidget(b4)
        layout3.addWidget(b5)
        layout3.addWidget(b6)
        layout2.addLayout(layout3)
        layout1.addLayout(layout2)
        widget = QWidget()
        widget.setLayout(layout1)
        self.setCentralWidget(widget)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()