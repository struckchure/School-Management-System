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

		self.sideBarScroll = customWidgets.SideBar()

		self.sideBarLayout = self.sideBarScroll.sideBarLayout
		self.sideBarButtonRatio = pageConfigurations.sideBarButtonRatio
		
		self.title = 'smsUI'
		self.sideBarTitle = customWidgets.SideBarTitle(text=self.title)
		self.sideBarTitle.setMaximumWidth(self.sideBarWidth)
		self.sideBarLayout.addWidget(self.sideBarTitle)

		spacer1 = QLabel()
		spacer1.setFixedHeight(60)
		self.sideBarLayout.addWidget(spacer1)

		self.dashBoard = customWidgets.SideBarButton(title='DashBoard', image='resources/assets/images/icons/dashboard_icn.png')
		self.sideBarLayout.addWidget(self.dashBoard)

		self.studentSection = customWidgets.SideBarSection(title='Student', width=self.sideBarWidth)
		self.admissionButton = customWidgets.SideBarButton(title='Admission', image='resources/assets/images/icons/admission.png')
		self.admissionButton.setFixedWidth(int(self.sideBarWidth * self.sideBarButtonRatio))
		self.studentSection.widgetLayout.addWidget(self.admissionButton)

		self.studentPromotionButton = customWidgets.SideBarButton(title='Promotion', image='resources/assets/images/icons/promotion.png')
		self.studentPromotionButton.setFixedWidth(int(self.sideBarWidth * self.sideBarButtonRatio))
		self.studentSection.widgetLayout.addWidget(self.studentPromotionButton)

		self.allStudentsButton = customWidgets.SideBarButton(title='All Students', image='resources/assets/images/icons/all.png')
		self.allStudentsButton.setFixedWidth(int(self.sideBarWidth * self.sideBarButtonRatio))
		self.studentSection.widgetLayout.addWidget(self.allStudentsButton)

		self.sideBarLayout.addWidget(self.studentSection)

		self.teacherSection = customWidgets.SideBarSection(title='Teacher', width=self.sideBarWidth)
		self.addTeacherButton = customWidgets.SideBarButton(title='New Teacher', image='resources/assets/images/icons/new_teacher.png')
		self.addTeacherButton.setFixedWidth(int(self.sideBarWidth * self.sideBarButtonRatio))
		self.teacherSection.widgetLayout.addWidget(self.addTeacherButton)

		self.teacherPromotionButton = customWidgets.SideBarButton(title='Promotion', image='resources/assets/images/icons/promotion.png')
		self.teacherPromotionButton.setFixedWidth(int(self.sideBarWidth * self.sideBarButtonRatio))
		self.teacherSection.widgetLayout.addWidget(self.teacherPromotionButton)

		self.allTeachersButton = customWidgets.SideBarButton(title='All Teachers', image='resources/assets/images/icons/all.png')
		self.allTeachersButton.setFixedWidth(int(self.sideBarWidth * self.sideBarButtonRatio))
		self.teacherSection.widgetLayout.addWidget(self.allTeachersButton)

		self.sideBarLayout.addWidget(self.teacherSection)

		self.mainPageLayout.addWidget(self.sideBarScroll)

	def rightPage(self):
		self.rightPageStackedWidget = QStackedWidget()

		self.rightPageLayout = QVBoxLayout()
		self.rightPageLayout.setContentsMargins(0, 0, 0, 0)
		self.rightPageLayout.setSpacing(0)
		self.rightPageLayout.setAlignment(Qt.AlignTop)

		self.rightPageLayout.addWidget(self.rightPageStackedWidget, stretch=0, alignment=Qt.AlignLeft)
		
		rightPageFinders = {
			'page':[],
			'index':[]
		}

		rightPageFinders['page'].append('DashBoard')
		rightPageFinders['index'].append(0)

		self.dashBoard = DashBoard.DashBoard(self.rightPageStackedWidget, rightPageFinders)
		self.rightPageStackedWidget.addWidget(self.dashBoard)

		self.rightPageGroup = QGroupBox()
		self.rightPageGroup.setMaximumSize(1500, 900)
		self.rightPageGroup.setObjectName('rightMainGroup')
		self.rightPageGroup.setLayout(self.rightPageLayout)

		self.rightPageScroll = QScrollArea()
		self.rightPageScroll.setObjectName('rightMainScroll')
		self.rightPageScroll.setWidgetResizable(True)
		self.rightPageScroll.setWidget(self.rightPageGroup)

		self.mainPageLayout.addWidget(self.rightPageScroll)
