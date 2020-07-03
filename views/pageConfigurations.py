# Page configurations

pageFinders = {
	'page':[],
	'index':[]
}

# Window settings

windowWidth = 1500
windowHeight = 1200

navBarHeight = 40

sideBarWidth = 0.18
pageWidth = 1 - sideBarWidth
sideBarWidgetWidthRatio = 0.65
sideBarSize = [500, 900]



def getSideBarWidth(windowWidth):
	return windowWidth * sideBarWidth


def getPageWidth(windowWidth):
	return windowWidth * pageWidth


# Authentification settings

minPasswordLength = 6
cardWidthRatio = 1.2
cardHeightRatio = 0.8
