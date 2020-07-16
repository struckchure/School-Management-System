#!/usr/bin/env python3
import os
import sys
# import sass


try:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
    from django.core.wsgi import get_wsgi_application

    application = get_wsgi_application()
except Exception as e:
    print(e)

from PyQt5.QtWidgets import QApplication
from viewManagers.mainWindowManager import mainWindow


def main():
	try:
		# theme = sass.compile_string(
		# 	open('resources/assets/qss/theme.qss', 'r').read().encode('utf-8')
		# ).decode()
		
		# theme += open('resources/assets/qss/boostrap.qss', 'r').read()

		theme = open('resources/assets/qss/boostrap.qss', 'r').read()

		app = QApplication(sys.argv)
		window = mainWindow()
		window.setStyleSheet(theme)
		window.show()

		sys.exit(app.exec_())
	except KeyboardInterrupt:
		sys.exit()


if __name__ == '__main__':
	main()
