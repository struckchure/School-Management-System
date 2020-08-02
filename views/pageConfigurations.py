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
sideBarSize = [260, 900]
pageWidth = 1 - sideBarWidth
sideBarButtonHeight = 35
sideBarSectionWidth = sideBarSize[0] * 8
sideBarWidgetWidthRatio = 0.45
sideBarButtonRatio = sideBarWidgetWidthRatio


def getSideBarWidth(windowWidth):
	return windowWidth * sideBarWidth


def getPageWidth(windowWidth):
	return windowWidth * pageWidth

# Authentification settings


minPasswordLength = 6
cardWidthRatio = 1.2
cardHeightRatio = 0.8

# DashBoard settings

DashButtonSize = [150, 100]


# Table configurations

tableSize = [300, 50]


# Card Defintions

pageHeaderBG = 'rgba(0, 0, 0, 0.05)'
pageHeaderBorder = 'rgba(0, 0, 0, 0)'
