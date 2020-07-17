import sass


'''
	
	Custom Utilities

'''


def findPage(pageFinders, pageName):
	pages = pageFinders['page']
	index = pageFinders['index']

	page = pages.index(pageName)

	return index[page]


def paginator(line, max_word=70, show_end=False, end_length=10):
	line_copy = str(line)
	if len(str(line)) > max_word:
		line = line[:max_word] + ' ... '
		if show_end:
			line += line_copy[-end_length:]
	else:
		line = line

	return line


def readQSS(file='resources/assets/qss/boostrap.qss'):
	theme = open(file, 'r').read()
	scss = open('resources/assets/scss/boostrap.scss', mode='w')
	scss.write(theme)

	sass.compile(dirname=('resources/assets/scss', 'resources/assets/qss'), output_style='expanded')
	css = open('resources/assets/qss/boostrap.css', 'r').read()
	
	return css


def findReplace(old, new, keywords):
	qss = readQSS()
	qss = qss.split(keywords)[1].split(keywords)[0].replace(
		f'{old}',
		f'{new}'
	)

	return qss
