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
        b1.setCheckable(True)
        b1.clicked.connect(self.b1)
        b2.setCheckable(True)
        b2.clicked.connect(self.b2)
        b3.setCheckable(True)
        b3.clicked.connect(self.b3)
        b4.setCheckable(True)
        b4.clicked.connect(self.b4)
        b5.setCheckable(True)
        b5.clicked.connect(self.b5)
        b6.setCheckable(True)
        b6.clicked.connect(self.b6)
    def b1(self):

    def b2(self):

    def b3(self):
    
    def b4(self):

    def b5(self):

    def b6(self):
        
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()