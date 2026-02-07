from model.ancientPlaceEvent import AncientPlaceEvent
from datetime import datetime
#id;placeId;name;description;date
class AncientPlaceEventsFileService:
    def __init__(self, fileDb):
        self.fileDb = fileDb
        self.placeEvents = []
        self.fileDb.readAncientPlaceEvents(self.placeEvents)

    def getNextIndex(self):
        max = 0
        for i in range(len(self.placeEvents)):
            cId = int(self.placeEvents[i].id)
            if cId > max:
                max = cId
        return str(max + 1)


    def addEventToPlace(self, placeId, name, description, date):
            id = self.getNextIndex()
            event = AncientPlaceEvent(id, placeId, name, description, date)
            self.placeEvents.append(event)
            eventsString = self.eventsToString()
            self.fileDb.writeToAncientPlaceEvents(eventsString)
            return id
    
    def editEvent(self, id, name, description, date):
          for i in range(len(self.placeEvents)):
            eventId = self.placeEvents[i].id
            if int(id) == int(eventId):
                event = self.placeEvents[i]
                event.name = name
                event.description = description
                event.date = date
                placesString = self.eventsToString()
                self.fileDb.writeToAncientPlaceEvents(placesString)
                break
    
    def removeEventById(self, id):
          for i in range(len(self.placeEvents)):
            eventId = self.placeEvents[i].id
            if int(id) == int(eventId):
                del self.placeEvents[i]
                eventsString = self.eventsToString()
                self.fileDb.writeToAncientPlaceEvents(eventsString)
                break

    def removeEventsFormPlace(self, placeId):
          events = self.getPlaceEvents(placeId)
          for i in range(len(events)):
              self.removeEventById(events[i].id)

    def printEvent(self, event):
           print("id: " + str(event.id) + "\n" +
                "placeId: " + str(event.placeId) + "\n" +
                "name: " + event.name + "\n" +
                "description: " + event.description + "\n" +
                "date: " + str(event.date)
            )
           print("----------------------------------------------------------\n")

    def showPlaceEvents(self, placeId):
        for i in range(len(self.placeEvents)):
            id = self.placeEvents[i].placeId
            if int(id) == int(placeId):
                self.printEvent(self.placeEvents[i])

    def getPlaceEvents(self, placeId):
        events = []
        for i in range(len(self.placeEvents)):
            id = self.placeEvents[i].placeId
            if int(id) == int(placeId):
                events.append(self.placeEvents[i])
        return events
        
    def sortByDate(self,placeId, rev=False):
        events = self.getPlaceEvents(placeId)
        return sorted(events, key=lambda event: datetime.strptime(event.date, '%Y-%m-%d'), reverse=rev)

    def showById(self, id):
        for i in range(len(self.placeEvents)):
            eventId = self.placeEvents[i].id
            if int(id) == int(eventId):
                self.printEvent(self.placeEvents[i])
                break

    def getEventById(self, id):
        for i in range(len(self.placeEvents)):
            eventId = self.placeEvents[i].id
            if int(id) == int(eventId):
                return self.placeEvents[i]
        return None
            
    def show(self, list):
        for i in range(len(list)):
            self.printEvent(list[i])

    def eventsToString(self):
        lines = ""
        for i in range(len(self.placeEvents)):
            lines += str(self.placeEvents[i].id) + ";"  + str(self.placeEvents[i].placeId) + ";" + self.placeEvents[i].name + ";" + self.placeEvents[i].description + ";" + str(self.placeEvents[i].date) + "\n"
        return lines