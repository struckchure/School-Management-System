from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import cv2


class SchoolRegistration(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.setWindowTitle('School Management System')
        self.window_layout = QVBoxLayout()
        self.window_layout.setSpacing(0)
        self.window_layout.setContentsMargins(0, 0, 0, 0)
        self.window_layout.setAlignment(Qt.AlignCenter)
        x = QSpinBox()
        x.setFixedSize(400, 50)
        x.setMaximum(300)
        x.setCorrectionMode(True)

        print(dir(x))
        self.window_layout.addWidget(x)
        self.setLayout(self.window_layout)

print(dir())
if __name__ == '__main__':
    ctx = ApplicationContext()
    window = SchoolRegistration()
    window.show()
    exit_code = ctx.app.exec_()
    sys.exit(exit_code)

# appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
#     window = QMainWindow()
#     window.resize(250, 150)
#     window.show()
#     exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
#     sys.exit(exit_code)