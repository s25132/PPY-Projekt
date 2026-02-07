from repository.fileDb import FileDb
from service.ancientPlacesFileService import AncientPlacesFileService
from service.ancientPlaceEventsFileService import AncientPlaceEventsFileService
from controller.consoleController import ConsoleController

def main():
    fileDb = FileDb()
    ancientPlacesService = AncientPlacesFileService(fileDb)
    ancientPlaceEventsFileService = AncientPlaceEventsFileService(fileDb)
    consoleController = ConsoleController(ancientPlacesService, ancientPlaceEventsFileService)
    fileDb.printDbFiles()
    print("Walcome!")
    consoleController.loop()


def test():
    ancientPlacesService = AncientPlacesFileService(FileDb())
    ancientPlaceEventsFileService = AncientPlaceEventsFileService(FileDb())

    #6;Acropolis of Athens;The Acropolis of Athens is an asortncient citadel located on a rocky outcrop above the city of Athens, Greece. It contains several ancient buildings of great architectural and historic significance, the most famous being the Parthenon. The Acropolis is a UNESCO World Heritage Site.;25;EUR;Athens,Greece;37.9715;23.7262
    id = ancientPlacesService.addPlace('Acropolis of Athens','sortThe Acropolis of Athens is an ancient citadel located on a rocky outcrop above the city of Athens, Greece. It contains several ancient buildings of great architectural and historic significance, the most famous being the Parthenon. The Acropolis is a UNESCO World Heritage Site.',
                                   25,'EUR','Athens','Greece', 37.9715, 23.7262)
    
    ancientPlacesService.showById(id)
    ancientPlacesService.removePlaceById(id)

    ancientPlacesService.show()

    #7;Chichen Itza;Chichen Itza is a large pre-Columbian archaeological site located in the Yucatán Peninsula, Mexico. It was a major focal point in the northern Maya lowlands from the Late Classic through the Terminal Classic and into the early portion of the Early Postclassic period. The site exhibits a multitude of architectural styles, reminiscent of styles seen in central Mexico and of the Puuc and Chenes styles of the northern Maya lowlands. Chichen Itza was one of the largest Maya cities and it was likely to have been one of the mythical great cities, or Tollans, referred to in later Mesoamerican literature.;600;MXN;Yucatán,Mexico;20.6831;-88.5692
    id = ancientPlacesService.addPlace('Chichen Itza','Chichen Itza is a large pre-Columbian archaeological site located in the Yucatán Peninsula, Mexico. It was a major focal point in the northern Maya lowlands from the Late Classic through the Terminal Classic and into the early portion of the Early Postclassic period. The site exhibits a multitude of architectural styles, reminiscent of styles seen in central Mexico and of the Puuc and Chenes styles of the northern Maya lowlands. Chichen Itza was one of the largest Maya cities and it was likely to have been one of the mythical great cities, or Tollans, referred to in later Mesoamerican literature.',
                                    600,'MXN','Yucatán','Mexico',20.6831,-88.5692)
    
    ancientPlacesService.editPlace(id, 'Chichen Itza','Chichen Itza is a large pre-Columbian archaeological site located in the Yucatán Peninsula, Mexico. It was a major focal point in the northern Maya lowlands from the Late Classic through the Terminal Classic and into the early portion of the Early Postclassic period. The site exhibits a multitude of architectural styles, reminiscent of styles seen in central Mexico and of the Puuc and Chenes styles of the northern Maya lowlands. Chichen Itza was one of the largest Maya cities and it was likely to have been one of the mythical great cities, or Tollans, referred to in later Mesoamerican literature.',
                                    700,'MXN','Yucatán','Mexico',20.6831,-88.5692)
    
    ancientPlacesService.showById(id)
    ancientPlacesService.removePlaceById(id)

    place = ancientPlacesService.getPlaceById(10)
    if place is not None:
        print(place.name)


    ancientPlaceEventsFileService.showPlaceEvents(2)
    ancientPlaceEventsFileService.showPlaceEvents(1)

    filtered = ancientPlacesService.filterPlacesByCity('Rome')
    for i in range(len(filtered)):
        print(filtered[i].city)

    filtered = ancientPlacesService.filterPlacesByCountry('Italy')
    for i in range(len(filtered)):
        print(filtered[i].country)

    sorted = ancientPlaceEventsFileService.sortByDate(2)
    for i in range(len(sorted)):
        print(sorted[i].date)

    print("----------------------------------------------------")
    
    sorted = ancientPlaceEventsFileService.sortByDate(2, True)
    for i in range(len(sorted)):
        print(sorted[i].date)

    print("----------------------------------------------------")
    results = ancientPlacesService.searchInDescription('located')
    for i in range(len(results)):
        print(results[i].description)

    print("----------------------------------------------------")
    results = ancientPlacesService.searchInName('Athens')
    for i in range(len(results)):
        print(results[i].name)

if __name__ == "__main__":
    main()