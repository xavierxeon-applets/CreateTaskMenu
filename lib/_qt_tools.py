#

import subprocess
import os


def updateUI(uiFileName):

   thisDir = os.path.dirname(__file__)

   uiFile = thisDir + '/' + uiFileName
   uiTime = os.path.getmtime(uiFile)

   pyFile = os.path.basename(uiFileName)
   pyFile = 'ui_' + pyFile.replace('.ui', '.py')
   pyFile = thisDir + '/' + pyFile
   pyTime = 0
   if os.path.exists(pyFile):
      pyTime = os.path.getmtime(pyFile)

   if uiTime > pyTime:
      print('update ui file')
      os.remove(pyFile)
      subprocess.run(['pyside6-uic', uiFile, '-o', pyFile])
