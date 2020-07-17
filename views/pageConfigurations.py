# Page configurations

pageFinders = {
	'page': [],
	'index': []
}

# Window settings

windowWidth = 1500
windowHeight = 1200

# NavBar settings

navBarHeight = 40
navSideMargins = 20

# SideBar settings

sideBarWidth = 0.7
pageWidth = 1 - sideBarWidth
sideBarButtonHeight = 35
sideBarSectionWidth = 0.5 * windowWidth
sideBarWidgetWidthRatio = 0.45
sideBarButtonRatio = sideBarWidgetWidthRatio
sideBarSize = [230, 900]


def getSideBarWidth(windowWidth):
	return windowWidth * sideBarWidth


def getPageWidth(windowWidth):
	return windowWidth * pageWidth

# Authentification settings


minPasswordLength = 6
cardWidthRatio = 1.2
cardHeightRatio = 0.8

# DashBoard settings

DashButtonSize = [115, 120]


# Table configurations

tableSize = [300, 50]
