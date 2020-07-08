# Page configurations

pageFinders = {
	'page':[],
	'index':[]
}

# Window settings

windowWidth = 1500
windowHeight = 1200

navBarHeight = 40

sideBarWidth = 0.7
pageWidth = 1 - sideBarWidth
sideBarSectionWidth = sideBarWidth * windowWidth
sideBarWidgetWidthRatio = 0.71
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

DashButtonSize = [120, 120]
