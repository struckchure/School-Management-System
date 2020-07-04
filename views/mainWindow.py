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

from resources.assets.customWidgets import customWidgets
from views import pageConfigurations
from views import DashBoard
from views import Students
from views import Teachers

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
		self.rightPage()

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

	def rightPage(self):
		self.rightPageStackedWidget = QStackedWidget()

		self.rightPageLayout = QVBoxLayout()
		self.rightPageLayout.setContentsMargins(0, 0, 0, 0)
		self.rightPageLayout.setSpacing(0)
		self.rightPageLayout.setAlignment(Qt.AlignTop | Qt.AlignHCenter)

		self.rightPageLayout.addWidget(self.rightPageStackedWidget, stretch=0, alignment=Qt.AlignTop | Qt.AlignHCenter)
		
		rightPageFinders = {
			'page':[],
			'index':[]
		}

		rightPageFinders['page'].append('DashBoard')
		rightPageFinders['index'].append(0)

		self.dashBoard = DashBoard.DashBoard(self.rightPageStackedWidget, rightPageFinders)
		self.rightPageStackedWidget.addWidget(self.dashBoard)

		self.rightPageGroup = QGroupBox()
		self.rightPageGroup.setObjectName('rightMainGroup')
		self.rightPageGroup.setLayout(self.rightPageLayout)

		self.rightPageScroll = QScrollArea()
		self.rightPageScroll.setObjectName('rightMainScroll')
		self.rightPageScroll.setWidgetResizable(True)
		self.rightPageScroll.setWidget(self.rightPageGroup)

		self.mainPageLayout.addWidget(self.rightPageScroll)
