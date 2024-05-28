import configparser
from model.ancientPlaceEvent import AncientPlaceEvent
from model.ancientPlace import AncientPlace
class FileDb:
  def __init__(self):
    __config = configparser.RawConfigParser()
    __config.read('resources/app.properties')

    self.__ancientPlacesFile = __config.get('FileDataBase', 'ancientPlacesFile')
    self.__ancientPlaceEventsFile = __config.get('FileDataBase', 'ancientPlaceEventsFile')

  def printDbFiles(self):
    print("DbFiles " + self.__ancientPlacesFile + " " + self.__ancientPlaceEventsFile)

  def openAncientPlacesFile(self, type):
    return open(self.__ancientPlacesFile, type)
  
  def openAncientPlaceEventsFile(self, type):
    return open(self.__ancientPlaceEventsFile, type)
  
  def readAncientPlaces(self, places):
      try:
       file = self.openAncientPlacesFile("r")
       line = file.readline()
       while line:
           line = line.rstrip().split(';')
           place = AncientPlace(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8])
           places.append(place)
           line = file.readline()
      finally:
       file.close()

  def writeToAncientPlaces(self, data):
      try:
       file = self.openAncientPlacesFile("w")
       file.write(data)
      finally:
       file.close()

  def readAncientPlaceEvents(self, placeEvents):
        try:
         file = self.openAncientPlaceEventsFile("r")
         line = file.readline()
         while line:
             line = line.rstrip().split(';')
             event = AncientPlaceEvent(line[0], line[1], line[2], line[3], line[4])
             placeEvents.append(event)
             line = file.readline()
        finally:
         file.close()

  def writeToAncientPlaceEvents(self, data):
        try:
         file = self.openAncientPlaceEventsFile("w")
         file.write(data)
        finally:
         file.close()    
      