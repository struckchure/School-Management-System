# Window settings

windowWidth = 950
navBarWidth = 0.25
pageWidth = 1 - navBarWidth


pageFinders = {
	'page':[],
	'index':[]
}


def getNavBarWidth(windowWidth=pageWidth):
	return windowWidth * navBarWidth


def getPageWidth(windowWidth=windowWidth):
	return windowWidth * pageWidth


# Authentification settings

minPasswordLength = 6
cardWidthRatio = 1.2
cardHeightRatio = 0.8
