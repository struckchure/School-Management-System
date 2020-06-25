from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


# Custom Modules Imports

from views import mainWindow as mainWindowViews
from views import AuthentificationViews
from views import pageConfigurations

# Custom Modules End


class mainWindow(QWidget):
	def __init__(self):
		QWidget.__init__(self)

		self.main_layout = QVBoxLayout()
		self.main_layout.setContentsMargins(0, 0, 0, 0)
		self.main_layout.setAlignment(Qt.AlignTop)

		self.setLayout(self.main_layout)
		self.setObjectName('index')
		self.setWindowTitle('School Management System')
		self.showMaximized()

		self.initialization()

	def initialization(self):
		self.pageController()

	def pageController(self):
		'''
			Add widgets to this stacked widget, it acts like a layout
			when you add new widgets to it, use this to activate the widget visibilty

			self.pageControl.setCurrentIndex(self.pageControl.currentIndex() + 1)

			when you add widgets to a stacked widget, it adds like using index, so it's even easier to navigate using indexing
			just like in a list :)
		'''

		pageConfigurations.pageFinders['page'].append('indexPage')
		pageConfigurations.pageFinders['index'].append(0)
		
		self.pageControl = QStackedWidget()
		self.pageControl.addWidget(AuthentificationViews.Login(self.pageControl, pageConfigurations.pageFinders))
		self.pageControl.setCurrentIndex(0)


		self.main_layout.addWidget(self.pageControl)
