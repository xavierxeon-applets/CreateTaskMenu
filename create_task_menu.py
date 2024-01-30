#!/usr/bin/env python3

import os
import signal
import sys

from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QTimer

from lib import MainWidget


def signit_handler(*args):

   QApplication.quit()


def main():

   if len(sys.argv) != 2:
      print('need to supply name to executable')
      return

   exeName = sys.argv[1]
   exeName = os.path.abspath(exeName)

   if not os.path.exists(exeName):
      print('executable does not exist:', exeName)
      return

   app = QApplication([])

   app.setOrganizationName('SDU LSP')
   app.setOrganizationDomain('mmmi.sdu.dk')
   app.setApplicationName('Linux Task Menu')

   signal.signal(signal.SIGINT, signit_handler)
   timer = QTimer()
   timer.start(500)
   timer.timeout.connect(lambda: None)  # Let the interpreter run each 500 ms.

   mw = MainWidget(exeName)
   mw.show()

   sys.exit(app.exec())


if __name__ == '__main__':
   main()
