# import sass
from resources.assets.qss import qssVariables
import secrets
import random
import datetime
import string


'''
	
	Custom Utilities

'''

signs = [
	'!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+',
		'-', '=', '\\', '//', '`', '|'
	]
numbers = [i for i in range(0, 9)]
alphabets_lower = [i for i in string.ascii_lowercase]
alphabets_upper = [i for i in string.ascii_uppercase]

all_keys = numbers + alphabets_lower + alphabets_upper


def findPage(pageFinders, pageName):
	pages = pageFinders['page']
	index = pageFinders['index']

	page = pages.index(pageName)

	return index[page]


def paginator(line, max_word=70, show_end=False, end_length=10):
	line_copy = str(line)
	if len(str(line)) > max_word:
		line = str(line)
		line = line[:max_word] + ' ... '
		if show_end:
			line += line_copy[-end_length:]
	else:
		line = str(line)

	return line


# def readQSS(file='resources/assets/qss/boostrap.qss'):
# 	theme = open(file, 'r').read()
# 	scss = open('resources/assets/scss/boostrap.scss', mode='w')
# 	scss.write(theme)

# 	sass.compile(dirname=('resources/assets/scss', 'resources/assets/qss'), output_style='expanded')
# 	css = open('resources/assets/qss/boostrap.css', 'r').read()

# 	return css


def readQSS(qss='resources/assets/qss/boostrap.qss', qssVariables=qssVariables.variables):
	qss = open(qss, mode='r').read()

	variables = list(qssVariables.keys())
	values = list(qssVariables.values())

	for i in variables:
		qss = qss.replace(f'${i}', values[variables.index(i)])
	
	theme = open('resources/assets/qss/boostrap.css', mode='w')
	theme.write(qss)

	qss = open('resources/assets/qss/boostrap.css', mode='r').read()

	return qss


def findReplace(old, new, keywords):
	qss = readQSS()
	qss = qss.split(keywords)[1].split(keywords)[0].replace(
		f'{old}',
		f'{new}'
	)

	return qss


def generate_admission_number(exisiting_list, length=4):
	date = datetime.datetime.now()
	year = date.year
	extra = ''

	for i in range(length):
		extra += random.choice(alphabets_upper)

	new_number = f'{year}{extra}'
	
	while new_number not in exisiting_list:
		break
	else:
		new_number = f'{year}{extra}'
	
	return new_number
