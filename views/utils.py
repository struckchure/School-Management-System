'''
	
	Custom Utilities

'''



def findPage(pageFinders, pageName):
	pages = pageFinders['page']
	index = pageFinders['index']

	page = pages.index(pageName)

	return index[page]


def paginator(line, max_word=70, show_end=False, end_length=10):
	line_copy = line
	if len(line) > max_word:
		line = line[:max_word] + ' ... '
		if show_end:
			line += line_copy[-end_length:]
	else:
		line = line

	return line
