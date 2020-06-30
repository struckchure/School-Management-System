# Window settings

windowWidth = 1500
windowHeight = 1200

navBarHeight = 35

sideBarWidth = 0.2
sideBarButtonRatio = 0.7
pageWidth = 1 - sideBarWidth

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
