from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Window(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)

		self.window_layout = QVBoxLayout()
		self.window_layout.setSpacing(0)
		self.window_layout.setContentsMargin(0, 0, 0, 0)
		self.window_layout.setAlignment(Qt.AlignCenter)

		self.setLayout(self.window_layout)
		self.intialization()

	def initialization(self):
		self.main_layout = QVBoxLayout()
		self.main_layout.setSpacing(0)
		self.main_layout.setContentsMargin(0, 0, 0, 0)
		self.main_layout.setAlignment(Qt.AlignCenter)

		self.main_group = QGroupBox()
		self.main_group.setLayout(self.main_layout)
		self.main_group.setStyleSheet(
			'''
			QGroupBox {
				border: 0px;
				background-color: rgb(200, 200, 200);
			}
			'''
		)

		self.window_layout.addWidget(self.main_group)

if __name__ == '__main__':
    appctxt = ApplicationContext()       
    window = Window()
    window.show()
    exit_code = appctxt.app.exec_()      
    sys.exit(exit_code)
