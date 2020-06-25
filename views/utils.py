'''
	
	Custom Utilities

'''



def findPage(pageFinders, pageName):
	pages = pageFinders['page']
	index = pageFinders['index']

	page = pages.index(pageName)

	return index[page]
