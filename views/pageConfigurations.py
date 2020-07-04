# Window settings

windowWidth = 1500
navBarHeight = 45
sideBarWidth = 0.2
pageWidth = 1 - sideBarWidth
sideBarButtonRatio = 0.7

pageFinders = {
	'page':[],
	'index':[]
}


def getSideBarWidth(windowWidth):
	return windowWidth * sideBarWidth


def getPageWidth(windowWidth):
	return windowWidth * pageWidth


# Authentification settings

minPasswordLength = 6
cardWidthRatio = 1.2
cardHeightRatio = 0.8
