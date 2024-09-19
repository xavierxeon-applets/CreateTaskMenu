# ~/.local/share/applications

from configparser import ConfigParser, InterpolationSyntaxError
import os
import sys
from pathlib import Path

try:
   import clipboard
except ModuleNotFoundError:
   print('pip3 install --user clipboard')
   sys.exit(1)


class DesktopFile:

   folderPath = str(Path.home()) + '/.local/share/applications'
   sectionName = 'Desktop Entry'

   def __init__(self, fileName):

      self.fileName = fileName

      self.config = ConfigParser()
      self.config.optionxform = lambda option: option  # keep capital keys

   def read(self):

      self.config.read(self.fileName)

      if not self.config.has_section(DesktopFile.sectionName):
         raise ValueError()

      if not self.config.has_option(DesktopFile.sectionName, 'exec'):
         raise ValueError()

      try:
         self.exeName = self.config.get(DesktopFile.sectionName, 'exec')
      except InterpolationSyntaxError:
         self.exeName = None
         raise ValueError()

      print(self.fileName, self.exeName)

   def setIcon(self, iconFileName):

      self.config.set(DesktopFile.sectionName, 'Icon', iconFileName)

   def setCategory(self, category):

      self.config.set(DesktopFile.sectionName, 'Categories', category)

   def create(self, exeName, fileName):

      self.config.add_section(DesktopFile.sectionName)
      self.config.set(DesktopFile.sectionName, 'Name', fileName)
      self.config.set(DesktopFile.sectionName, 'Exec', exeName)
      self.config.set(DesktopFile.sectionName, 'Path', str(Path(exeName).parent))

      self.config.set(DesktopFile.sectionName, 'Terminal', 'false')
      self.config.set(DesktopFile.sectionName, 'Type', 'Application')

   def write(self):

      with open(self.fileName, 'w') as outfile:
         self.config.write(outfile)

      cmd = f'sudo desktop-file-install {self.fileName}'
      clipboard.copy(cmd)
      # print('sudo update-desktop-database')

   @staticmethod
   def findOrCreate(exeName):

      # print(exeName)

      for entry in os.scandir(DesktopFile.folderPath):
         if not entry.is_file():
            continue

         extension = Path(entry.path).suffix
         if '.desktop' != extension:
            continue

         file = DesktopFile(entry.path)
         try:
            file.read()
         except ValueError:
            continue

         if file.exeName == exeName:
            return file

      fileName = Path(exeName).name
      filePath = DesktopFile.folderPath + '/' + fileName + '.desktop'

      file = DesktopFile(filePath)
      file.create(exeName, fileName)
      return file
