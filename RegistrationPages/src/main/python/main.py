from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Window(QWidget):
	def __init__(self):
		QWidget.__init__(self)

		self.window_layout = QVBoxLayout()
		self.window_layout.setSpacing(0)
		self.window_layout.setContentsMargins(0, 0, 0, 0)
		self.window_layout.setAlignment(Qt.AlignTop)

		self.main_size = (400, 30)

		self.setLayout(self.window_layout)
		self.showMaximized()
		self.intialization()

	def intialization(self):
		self.main_layout = QVBoxLayout()
		self.main_layout.setSpacing(0)
		self.main_layout.setContentsMargins(0, 0, 0, 0)
		self.main_layout.setAlignment(Qt.AlignTop)

		self.main_group = QGroupBox()
		self.main_group.setLayout(self.main_layout)
		self.main_group.setStyleSheet(
			'''
			QGroupBox {
				border: 0px;
			}
			'''
		)

		self.window_layout.addWidget(self.main_group)

		# Split Layout

		self.splitLAYOUT()

	def splitLAYOUT(self):
		self.split_layout = QVBoxLayout()
		self.split_layout.setSpacing(0)
		self.split_layout.setContentsMargins(0, 0, 0, 0)
		self.split_layout.setAlignment(Qt.AlignTop)

		self.split_group = QGroupBox()
		self.split_group.setMaximumWidth(self.width())
		# self.split_group.showMaximized()
		self.split_group.setLayout(self.split_layout)
		self.split_group.setStyleSheet(
			'''
			QGroupBox {
				border: 0px;
				background-color: #004411;
			}
			'''
		)

		self.split_scroll = QScrollArea()
		self.split_scroll.setWidgetResizable(True)
		self.split_scroll.setWidget(self.split_group)
		self.split_scroll.setStyleSheet(
			'''
			QGroupBox {
				border: 0px;
			}
			'''
		)

		self.main_layout.addWidget(self.split_scroll)

	def topLAYOUT(self):
		pass

	def bottomLAYOUT(self):
		pass

if __name__ == '__main__':
    appctxt = ApplicationContext()       
    window = Window()
    window.show()
    exit_code = appctxt.app.exec_()      
    sys.exit(exit_code)
