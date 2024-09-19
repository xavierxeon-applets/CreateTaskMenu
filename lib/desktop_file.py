# ~/.local/share/applications

from configparser import ConfigParser, InterpolationSyntaxError
import os
from pathlib import Path


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

   def create(self, exeName, fileName):

      self.config.add_section(DesktopFile.sectionName)
      self.config.set(DesktopFile.sectionName, 'Name', fileName)
      self.config.set(DesktopFile.sectionName, 'Exec', exeName)
      self.config.set(DesktopFile.sectionName, 'Path', str(Path(exeName).parent))

      self.config.set(DesktopFile.sectionName, 'Terminal', 'false')
      self.config.set(DesktopFile.sectionName, 'Type', 'Application')

      """
      echo "[Desktop Entry]" > $DEKTOP_FILE
      echo "Name=SDKUpdater2" >> $DEKTOP_FILE
      echo "Exec=/usr/local/SDKUpdater2/SDKUpdaterUI" >> $DEKTOP_FILE
      echo "Path=/usr/local/SDKUpdater2" >> $DEKTOP_FILE
      echo "Icon=/usr/local/SDKUpdater2/SDKUpdater.svg" >> $DEKTOP_FILE
      echo "Terminal=false" >> $DEKTOP_FILE
      echo "Type=Application" >> $DEKTOP_FILE
      echo "Categories=Development;" >> $DEKTOP_FILE
      """

   def write(self):

      print(self.config, self.fileName)

      with open(self.fileName, 'w') as outfile:
         self.config.write(outfile)

      print('sudo update-desktop-database')
      """
      echo "if hash desktop-file-install 2>/dev/null; then" >> $CONTROL_DIR/postinst
      echo "desktop-file-install /usr/share/applications/SDKUpdater2.desktop" >> $CONTROL_DIR/postinst
      echo "fi" >> $CONTROL_DIR/postinst
      """

   @staticmethod
   def findOrCreate(exeName):

      print(exeName)

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
