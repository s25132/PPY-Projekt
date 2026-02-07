from datetime import datetime

class ConsoleController:
    def __init__(self,ancientPlacesFileService, ancientPlaceEventsFileService):
        self.ancientPlacesFileService = ancientPlacesFileService
        self.ancientPlaceEventsFileService = ancientPlaceEventsFileService

    def loop(self):
     while True:
        command = input(">")
        if command is not None and command != "":
            result = self.tokenize(command, " ")
            if len(result) > 0:
                if len(result) == 1 and result[0] == 'show':
                    self.ancientPlacesFileService.show()
                elif len(result) == 1 and result[0] == 'help':
                   self.help()
                elif len(result) == 2 and result[0] == 'sortEvents':
                   id = result[1]
                   if self.validateInt(id) :
                      result = self.ancientPlaceEventsFileService.sortByDate(id)
                      self.ancientPlaceEventsFileService.show(result)
                   else :
                      print("Wrong Input")
                elif len(result) == 3 and result[0] == 'sortEvents' and result[1] == '-r':
                    id = result[2]
                    if self.validateInt(id) :
                      result = self.ancientPlaceEventsFileService.sortByDate(id, True)
                      self.ancientPlaceEventsFileService.show(result)
                    else :
                      print("Wrong Input")
                elif len(result) == 2 and result[0] == "showPlace":
                    id = result[1]
                    if self.validateInt(id) :
                        self.ancientPlacesFileService.showById(id)
                    else :
                        print("Wrong Input")
                elif len(result) == 2 and result[0] == "showEvent":
                    id = result[1]
                    if self.validateInt(id) :
                        self.ancientPlaceEventsFileService.showById(id)
                    else :
                        print("Wrong Input")
                elif len(result) == 3 and result[0] == "search" and result[1] == '-d':
                    text = result[2]
                    if self.validateString(text) :
                        result = self.ancientPlacesFileService.searchInDescription(text)
                        self.ancientPlacesFileService.showList(result)
                    else :
                        print("Wrong Input")
                elif len(result) == 3 and result[0] == "search" and result[1] == '-n':
                    text = result[2]
                    if self.validateString(text) :
                        result = self.ancientPlacesFileService.searchInName(text)
                        self.ancientPlacesFileService.showList(result)
                    else :
                        print("Wrong Input")
                elif len(result) == 3 and result[0] == "filter" and result[1] == '-ci':
                    text = result[2]
                    if self.validateString(text) :
                        result = self.ancientPlacesFileService.filterPlacesByCity(text)
                        self.ancientPlacesFileService.showList(result)
                    else :
                        print("Wrong Input")
                elif len(result) == 3 and result[0] == "filter" and result[1] == '-co':
                    text = result[2]
                    if self.validateString(text) :
                        result = self.ancientPlacesFileService.filterPlacesByCountry(text)
                        self.ancientPlacesFileService.showList(result)
                    else :
                        print("Wrong Input")
                elif len(result) == 2 and result[0] == "showPlaceEvents":
                    id = result[1]
                    if self.validateInt(id) :
                        result = self.ancientPlaceEventsFileService.showPlaceEvents(id)
                    else :
                        print("Wrong Input")
                elif len(result) == 2 and result[0] == "removePlace":
                    id = result[1]
                    if self.validateInt(id) :
                        result = self.removePlace(id)
                    else :
                        print("Wrong Input")
                elif len(result) == 2 and result[0] == "removeEvent":
                    id = result[1]
                    if self.validateInt(id) :
                        result = self.removeEvent(id)
                    else :
                        print("Wrong Input")
                elif len(result) == 5 and result[0] == "addEventToPlace":
                    placeId = result[1]
                    name = result[2]
                    description = result[3]
                    date = result[4]
                    self.addEventToPlace(placeId, name, description, date)
                elif len(result) == 9 and result[0] == "addPlace":
                     name = result[1]
                     description = result[2]
                     ticketPrice = result[3]
                     currency = result[4]
                     city = result[5]
                     country = result[6]
                     latitude = result[7]
                     longitude = result[8]
                     self.addPlace(name, description, ticketPrice, currency, city, country, latitude, longitude)
                elif len(result) == 5 and result[0] == "editEvent":
                    id = result[1]
                    name = result[2]
                    description = result[3]
                    date = result[4]
                    self.editEvent(id, name, description, date)
                elif len(result) == 3 and result[0] == "editEvent":
                    id = result[1]
                    name = result[2]
                    self.editEvent(id, name, None, None)
                elif len(result) == 4 and result[0] == "editEvent":
                    id = result[1]
                    name = result[2]
                    description = result[3]
                    self.editEvent(id, name, description, None)
                elif len(result) == 6 and result[0] == "editPlace":
                    id = result[1]
                    name = result[2]
                    description = result[3]
                    ticketPrice = result[4]
                    currency = result[5]
                    self.editPlace(id, name, description, ticketPrice, currency)
                elif len(result) == 5 and result[0] == "editPlace":
                    id = result[1]
                    name = result[2]
                    description = result[3]
                    ticketPrice = result[4]
                    self.editPlace(id, name, description, ticketPrice, None) 
                elif len(result) == 4 and result[0] == "editPlace":
                    id = result[1]
                    name = result[2]
                    description = result[3]
                    self.editPlace(id, name, description, None, None)
                elif len(result) == 3 and result[0] == "editPlace":
                    id = result[1]
                    name = result[2]
                    self.editPlace(id, name, None, None, None)        
                elif len(result) == 1 and result[0] == "exit":
                    break
                else : 
                   print("Wrong command")
            else : 
                print("Wrong command")
        else : 
            print("Wrong command, must not be empty")

    def help(self):
       print("show -> shows all places")
       print("showPlace <id> -> shows place with given id")
       print("showEvent <id> -> shows event with given id")
       print("showPlaceEvents <id> -> shows all events added to place with given id")

       print("search -d <text> -> searches by descritpion in places")
       print("search -n <text> -> searches by name in places")

       print("filter -ci <text> -> filters by city in places")
       print("filter -co <text> -> filters by country in places")

       print("sortEvents <id> -> sorts events added to place with given id")
       print("sortEvents -r <id> -> sorts events added to place with given id in reverse")

       print("addEventToPlace <placeId> <name> <description> <date> -> adds event to place with given placeId, date example -> 2024-09-10")
       print("editEvent <id> <name> -> edits event with given id")
       print("editEvent <id> <name> <description> -> edits event with given id")
       print("editEvent <id> <name> <description> <date> -> edits event with given id, date example -> 2024-09-10")

       print("addPlace <name> <description> <ticketPrice> <currency> <city> <country> <latitude> <longitude> -> adds new place")
       print("editPlace <id> <name> -> edits place with given id")
       print("editPlace <id> <name> <description>-> edits place with given id")
       print("editPlace <id> <name> <description> <ticketPrice> -> edits place with given id")
       print("editPlace <id> <name> <description> <ticketPrice> <currency> -> edits place with given id")

       print("removePlace <id> -> removes place with given id and its events")
       print("removeEvent <id> -> removes event with given id")

       print("exit -> exists app")

    def tokenize(self, str, delim):
        result = []
        s = ""
        for char in str:
            if char != delim:
             s += char
            else:
                result.append(s)
                s = ""
        if s:
            result.append(s)
        return result
    
    def editPlace(self, id, name=None, description=None, ticketPrice=None, currency=None):
        if self.validateInt(id):
             place = self.ancientPlacesFileService.getPlaceById(id)
             if place is not None:
                 if not self.validateString(name):
                    name = place.name
                 if not self.validateString(description):
                    description = place.description
                 if not self.validateFloat(ticketPrice):
                    ticketPrice = place.ticketPrice
                 if not self.validateString(currency):
                    currency = place.currency
                
                 if self.askYesNo():
                    self.ancientPlacesFileService.editPlace(id, name, description, ticketPrice, currency, place.city, place.country, place.latitude, place.longitude);
                    print("Place updated")
             else:
                print("No action taken")
        else:
            print("Wrong data")

    def editEvent(self, id, name=None, description=None, date=None):
        if self.validateInt(id):
             event = self.ancientPlaceEventsFileService.getEventById(id)
             if event is not None:
                 if not self.validateString(name):
                    name = event.name
                 if not self.validateString(description):
                    description = event.description
                 if not self.validateDate(date):
                    date = event.date
                
                 if self.askYesNo():
                    self.ancientPlaceEventsFileService.editEvent(id, name, description, date);
                    print("Event updated")
             else:
                print("No action taken")
        else:
            print("Wrong data")

    def addPlace(self, name, description, ticketPrice, currency, city, country, latitude, longitude):
        if self.validateString(name) and self.validateString(description) and self.validateFloat(ticketPrice) and self.validateString(currency) and self.validateString(city) and self.validateString(country) and self.validateFloat(latitude) and self.validateFloat(longitude):
            id = self.ancientPlacesFileService.addPlace(name, description, ticketPrice, currency, city, country, latitude, longitude)
            print("Place added with id " + str(id))
        else:
            print("Wrong data")

    def addEventToPlace(self, placeId, name, description, date):
            if self.validateInt(placeId) and self.validateString(name) and self.validateString(description) and self.validateDate(date):
                 ancientPlace = self.ancientPlacesFileService.getPlaceById(placeId)
                 if ancientPlace is not None:
                     id = self.ancientPlaceEventsFileService.addEventToPlace(placeId, name, description, date)
                     print("Event added with id " + str(id))
                 else:
                     print("No action taken")
            else:
                print("Wrong data")

    def removeEvent(self,id):
        if self.validateInt(id):
            event = self.ancientPlaceEventsFileService.getEventById(id)
            if event is not None and self.askYesNo():
                self.ancientPlaceEventsFileService.removeEventById(id)
                print("Event with id " + id + " has been removed")
            else:
                print("No action taken")
        else:
            print("Wrong data")

    def removePlace(self, id):
        if self.validateInt(id):
            ancientPlace = self.ancientPlacesFileService.getPlaceById(id)
            if ancientPlace is not None and self.askYesNo():
                self.ancientPlaceEventsFileService.removeEventsFormPlace(id)
                print("Events added tp palce with id " + id + " has been removed")
                self.ancientPlacesFileService.removePlaceById(id)
                print("Palce with id " + id + " has been removed")
            else:
                print("No action taken")
        else:
            print("Wrong data")

    def askYesNo(self):
        while True:
         command = input("Do you want do that? yes/no ")
         if command == 'yes':
             return True
         elif command == 'no':
             return False
         else :
              print("Wrong command") 

    def validateInt(self, value):
        if value is None:
            return False
        try:
            int(value)
            return True
        except ValueError:
            return False
        
    def validateFloat(self, value):
        if value is None:
            return False
        try:
            float(value)
            return True
        except ValueError:
            return False

    def validateString(self, value):
       if value is not None and value != "":
          return True
       return False
    
    def validateDate(self, date_text):
        if date_text is None:
            return False
        try:
            if date_text != datetime.strptime(date_text, "%Y-%m-%d").strftime('%Y-%m-%d'):
                raise ValueError
            return True
        except ValueError:
            return False
        