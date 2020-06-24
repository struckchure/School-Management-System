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
	def __init__(self, pageController):
		QGroupBox.__init__(self)

		self.pageController = pageController

		self.groupLayout = QVBoxLayout()
		self.groupLayout.setContentsMargins(0, 0, 0, 0)
		self.groupLayout.setAlignment(Qt.AlignCenter)

		self.setLayout(self.groupLayout)
		self.setMinimumWidth(1000)
		self.setObjectName('home')
		self.setStyleSheet(
			'''
				QGroupBox#home {
					border: 0px;
					background-image: url(resources/assets/images/home_bg_color_particles.jpg);
					background-repeat: no-repeat;
					background-position: center;
				}
			'''
		)

		self.initialization()

	def initialization(self):
		self.navBarWidth = pageConfigurations.getNavBarWidth(self.width())
		self.pageWidth = pageConfigurations.getPageWidth(self.width())

		self.mainPage()
		self.navBar()
		self.Page()

	def mainPage(self):
		self.mainPageLayout = QHBoxLayout()
		self.mainPageLayout.setSpacing(0)
		self.mainPageLayout.setContentsMargins(0, 0, 0, 0)
		self.mainPageLayout.setAlignment(Qt.AlignCenter)

		self.mainPageGroup = QGroupBox()
		self.mainPageGroup.setLayout(self.mainPageLayout)
		self.mainPageGroup.setObjectName('mainPageGroup')
		self.mainPageGroup.setStyleSheet(
			'''
				QGroupBox#mainPageGroup {
					border: 0px;
					padding: 25px;
				}
			'''
		)

		self.groupLayout.addWidget(self.mainPageGroup)

	def navBar(self):
		self.navBarLayout = QVBoxLayout()
		self.navBarLayout.setContentsMargins(0, 0, 0, 0)
		self.navBarLayout.setAlignment(Qt.AlignTop)

		self.userInfo = customWidgets.NavBarUser()
		self.userInfo.setMaximumWidth(self.navBarWidth)
		self.navBarLayout.addWidget(self.userInfo)

		self.navBarGroup = QGroupBox()
		self.navBarGroup.setMaximumWidth(self.navBarWidth)
		self.navBarGroup.setLayout(self.navBarLayout)
		self.navBarGroup.setObjectName('navBarGroup')
		self.navBarGroup.setStyleSheet(
			'''
				QGroupBox#navBarGroup {
					border: 0px;
					border-bottom-left-radius: 20px;
					border-top-left-radius: 20px;
					background-color: #3E1818;
				}
			'''
		)

		self.navBarScroll = QScrollArea()
		self.navBarScroll.setMaximumWidth(self.navBarWidth)
		self.navBarScroll.setWidget(self.navBarGroup)
		self.navBarScroll.setWidgetResizable(True)
		self.navBarScroll.setObjectName('navBarScroll')
		self.navBarScroll.setStyleSheet(
			'''
				QScrollArea#navBarScroll {
					border: 0px;
					background-color: rgba(0, 0, 0, 0);
				}
			'''
		)

		self.mainPageLayout.addWidget(self.navBarScroll)

	def Page(self):
		self.pageLayout = QVBoxLayout()
		self.pageLayout.setContentsMargins(0, 0, 0, 0)
		self.pageLayout.setAlignment(Qt.AlignTop)

		self.pageGroup = QGroupBox()
		self.pageGroup.setMaximumWidth(self.pageWidth)
		self.pageGroup.setLayout(self.pageLayout)
		self.pageGroup.setObjectName('pageGroup')
		self.pageGroup.setStyleSheet(
			'''
				QGroupBox#pageGroup {
					border: 0px;
					border-bottom-right-radius: 20px;
					border-top-right-radius: 20px;
					background-color: #698A84;
				}
			'''
		)

		self.pageScroll = QScrollArea()
		self.pageScroll.setMaximumWidth(self.pageWidth)
		self.pageScroll.setWidget(self.pageGroup)
		self.pageScroll.setWidgetResizable(True)
		self.pageScroll.setObjectName('pageScroll')
		self.pageScroll.setStyleSheet(
			'''
				QScrollArea#pageScroll {
					border: 0px;
					background-color: rgba(0, 0, 0, 0);
				}
			'''
		)

		self.mainPageLayout.addWidget(self.pageScroll)
