'''
	-_- Authors -_-
	Names - Mohammed Al Ameen Bolutife, Omoyajowo Solomon
	E-Mails - ameenmohammed2311@gmail.com, solo@gamil.com
	GitHub - Mohammed2702, Soloskido
'''

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
import cv2


# Custom Modules Imports

from views import pageConfigurations
from resources.assets.customWidgets import customWidgets

# Custom Modules End


'''
	Home Views
'''


class Home(QGroupBox):
	def __init__(self, pageController, user):
		QGroupBox.__init__(self)

		self.pageController = pageController
		self.user = user

		self.groupLayout = QVBoxLayout()
		self.groupLayout.setSpacing(0)
		self.groupLayout.setContentsMargins(0, 0, 0, 0)
		self.groupLayout.setAlignment(Qt.AlignTop)

		qss = open('resources/assets/qss/boostrap.qss').read()

		self.setStyleSheet(qss)
		self.setLayout(self.groupLayout)
		self.setMaximumSize(pageConfigurations.windowWidth, pageConfigurations.windowHeight)
		self.setObjectName('home')
		self.showMaximized()

		self.initialization()

	def initialization(self):
		self.navBarHeight = pageConfigurations.navBarHeight
		self.sideBarWidth = pageConfigurations.getSideBarWidth(self.width())
		self.pageWidth = pageConfigurations.getPageWidth(self.width())

		self.navBar()
		self.mainPage()
		self.sideBar()

	def navBar(self):
		self.navBarWidget = customWidgets.NavBar(self.user)
		self.groupLayout.addWidget(self.navBarWidget)

	def mainPage(self):
		self.mainPageLayout = QHBoxLayout()
		self.mainPageLayout.setSpacing(0)
		self.mainPageLayout.setContentsMargins(0, 0, 0, 0)
		self.mainPageLayout.setAlignment(Qt.AlignTop)

		self.mainPageGroup = QGroupBox()
		self.mainPageGroup.setObjectName('mainPageGroup')
		self.mainPageGroup.setLayout(self.mainPageLayout)

		self.mainPageScroll = QScrollArea()
		self.mainPageScroll.setObjectName('mainPageScroll')
		self.mainPageScroll.setWidgetResizable(True)
		self.mainPageScroll.setWidget(self.mainPageGroup)

		self.groupLayout.addWidget(self.mainPageScroll)

	def sideBar(self):
		'''
			Add widgets to the sideBar
			self.sideBarWidget.sideBarLayout.addWidget(self.sideBarTitle)
		'''
		
		# SideBar

		self.sideBarWidget = customWidgets.SideBar()
		
		self.sideBarTitle = customWidgets.SideBarTitle('School Management System')
		self.sideBarWidget.sideBarLayout.addWidget(self.sideBarTitle)

		spacer = QLabel()
		spacer.setFixedHeight(30)

		self.sideBarWidget.sideBarLayout.addWidget(spacer)

		# Sidebar eneded
		############################
		# Student section started

		self.studentSection = customWidgets.SideBarSection('Students')
		self.studentSection.setFixedWidth(self.sideBarWidget.width())
		self.sideBarWidget.sideBarLayout.addWidget(self.studentSection)

		self.newStudentButton = customWidgets.SideBarButton('Admission')
		self.studentSection.widgetLayout.addWidget(self.newStudentButton)
		
		# Student section ended
		#############################
		# Teacher section started

		self.teacherSection = customWidgets.SideBarSection('Teachers')
		self.teacherSection.setFixedWidth(self.sideBarWidget.width())
		self.sideBarWidget.sideBarLayout.addWidget(self.teacherSection)

		self.newTeacherButton = customWidgets.SideBarButton('New Teacher')
		self.teacherSection.widgetLayout.addWidget(self.newTeacherButton)

		# Teacher section ended

		self.mainPageLayout.addWidget(self.sideBarWidget)
