from model.ancientPlace import AncientPlace
#id;name;description;ticketPrice;currency;city,country;latitude;longitude
class AncientPlacesFileService:
    def __init__(self, fileDb):
        self.fileDb = fileDb
        self.places = []
        self.fileDb.readAncientPlaces(self.places)
        
    def printPlace(self,place):
           print("id: " + place.id + "\n" +
                "name: " + place.name + "\n" +
                "description: " + place.description + "\n" +
                "ticketPrice: " + str(place.ticketPrice) + "\n" +
                "currency: " + place.currency + "\n" +
                "city: " + place.city + "\n" +
                "country: " + place.country + "\n" +
                "latitude: " + str(place.latitude) + "\n" +
                "longitude: " + str(place.longitude)
            )
           print("----------------------------------------------------------\n")

    def getNextIndex(self):
        max = 0
        for i in range(len(self.places)):
            cId = int(self.places[i].id)
            if cId > max:
                max = cId
        return str(max + 1)

    
    def searchInDescription(self, phrase):
        result = []
        for i in range(len(self.places)):
            if self.places[i] is not None and self.places[i].description is not None and self.places[i].description.find(phrase) != -1:
                result.append(self.places[i])

        return result

    def searchInName(self, phrase):
        result = []
        for i in range(len(self.places)):
            if self.places[i] is not None and self.places[i].name is not None and self.places[i].name.find(phrase) != -1:
                result.append(self.places[i])

        return result
    
    def checkCountry(self, place, country):
        if country is not None:
            if str(country) == str(place.country):
                return True  
        return False
    
    def filterPlacesByCountry(self, country):
        filteredPlaces = []
        for i in range(len(self.places)):
            if self.checkCountry(self.places[i], country):
                filteredPlaces.append(self.places[i])
        return filteredPlaces
        
    def checkCity(self, place, city):
        if city is not None:
            if str(city) == str(place.city):
                return True  
        return False
    
    def filterPlacesByCity(self, city):
        filteredPlaces = []
        for i in range(len(self.places)):
            if self.checkCity(self.places[i], city):
                filteredPlaces.append(self.places[i])
        return filteredPlaces
        
    def addPlace(self, name, description, ticketPrice, currency, city, country, latitude, longitude):
        id = self.getNextIndex()
        place = AncientPlace(id, name, description, ticketPrice, currency, city, country, latitude, longitude)
        self.places.append(place)
        placesString = self.placesToString()
        self.fileDb.writeToAncientPlaces(placesString)
        return id

    def removePlaceById(self, id):
          for i in range(len(self.places)):
            placeId = self.places[i].id
            if int(id) == int(placeId):
                del self.places[i]
                placesString = self.placesToString()
                self.fileDb.writeToAncientPlaces(placesString)
                break

    def editPlace(self, id, name, description, ticketPrice, currency, city, country, latitude, longitude):
          for i in range(len(self.places)):
            placeId = self.places[i].id
            if int(id) == int(placeId):
                place = self.places[i]
                place.name = name
                place.description = description
                place.ticketPrice = ticketPrice
                place.currency = currency
                place.city = city
                place.country = country
                place.latitude = latitude
                place.longitude = longitude
                placesString = self.placesToString()
                self.fileDb.writeToAncientPlaces(placesString)
                break
   
    def showById(self, id):
        for i in range(len(self.places)):
            placeId = self.places[i].id
            if int(id) == int(placeId):
                self.printPlace(self.places[i])
                break

    def getPlaceById(self, id):
        for i in range(len(self.places)):
            placeId = self.places[i].id
            if int(id) == int(placeId):
                return self.places[i]
        return None

    def showList(self, list):
        for i in range(len(list)):
            self.printPlace(list[i])

    def show(self):
        for i in range(len(self.places)):
            self.printPlace(self.places[i])

    def placesToString(self):
        lines = ""
        for i in range(len(self.places)):
            lines += self.places[i].id + ";"  + self.places[i].name + ";" + self.places[i].description + ";" + str(self.places[i].ticketPrice) + ";" + self.places[i].currency + ";" + self.places[i].city + ";"  + self.places[i].country + ";" + str(self.places[i].latitude) + ";" + str(self.places[i].longitude) + "\n"
        return lines