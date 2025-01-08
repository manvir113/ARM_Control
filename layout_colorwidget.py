from PyQt6.QtGui import QColor, QPalette
from PyQt6.QtWidgets import QWidget
from PyQt6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDial,
    QDoubleSpinBox,
    QLabel,
    QLineEdit,
    QListWidget,
    QMainWindow,
    QSlider,
    QSpinBox,
)

class Color(QWidget):
    def __init__(self, task):
        super().__init__()
        if (task=='t'):
            a=3
        elif (task=='s'):
            h=35
        elif (task=='g'):
            h=9