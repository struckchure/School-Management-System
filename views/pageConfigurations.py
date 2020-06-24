windowWidth = 950
navBarWidth = 0.2
pageWidth = 1 - navBarWidth


pageConfigurations = {
	'home': 1,
	'login': 2,
}


def getNavBarWidth(windowWidth=pageWidth):
	return windowWidth * navBarWidth


def getPageWidth(windowWidth=windowWidth):
	return windowWidth * pageWidth
