Jakub Hass S25132

Prosta aplikacja do zarządzania starożytnymi miejscami.
Opis:

Twoim zadaniem jest stworzenie aplikacji konsolowej do zarządzania starożytnymi miejscami i zdarzeniami z nimi związanych.
Aplikacja powinna umożliwiać tworzenie, przeglądanie, edycję i usuwanie miejsc oraz pwoiązanych z nimi zdarzeniami.

Wymagania:
1. Aplikacja powinna umożliwiać dodawanie nowych miejsc.
2. Aplikacja powinna umożliwiać dodawanie nowych nowych zadrzeń do już istniejących miejsc.
3. Dane o miejscach i ich zdarzeniach powinny być przechowywane w plikach.
4. Aplikacja powinna umożliwiać przeglądanie listy miejsc.
5. Aplikacja powinna umożliwiać przeglądanie listy zdarzeń dla danego miejsca.
6. Aplikacja powinna umożliwiać edycję istniejących miejsc lub zdarzeń.
7. Użytkownik powinien móc zmieniać tytuł, opis i inne atrybuty miejsc i zdarzeń.
8. Aplikacja powinna umożliwiać usuwanie miejsc i zdarzeń.
9. Użytkownik powinien móc wybrać miejsce lub zadanie do usunięcia na podstawie identyfikatora.
10. Aplikacja powinna zapewniać interaktywny interfejs w konsoli.
11. Użytkownik powinien móc wybierać różne opcje, takie jak dodawanie miejsca/zdarzenia, wyświetlanie, edycję, usuwanie, a także wyjście z aplikacji.
12. Aplikacja powinna obsługiwać błędy, takie jak podanie nieprawidłowego identyfikatora zadania lub niewłaściwej opcji menu.
13. Użytkownik powinien otrzymywać odpowiednie komunikaty o błędach.
 
Zaimplementuj dodatkowe funkcje, takie jak sortowanie zdarzeń według daty, wyszukiwanie miejsc i zdarzeń po tytule lub opisie , filtorwanie miejsc po kraju i mieście.
Wykorzystaj bibliotekę datetime do obsługi dat i czasu w aplikacji.


Struktura plikowej bazy danych.
Dwa pliki txt:
ancient_places.txt
ancient_place_events.txt

Struktura ancient_places:
id;name;descritpion;ticketPrice;currency;city,country;latitude;longitude

Struktura ancient_place_events:
id;placeId;name;descritpion;date


Przykłady wywołań:
addEventToPlace 1 Test Test 2024-09-10

addPlace Test Test 20 USD TEST TEST 29.9792 31.1342

editEvent 9 Test Test 2024-09-10

editEvent 9 Test2

editEvent 9 Test3 Test3

editPlace 10 Test1 Test 20 USD

editPlace 10 Test2 Test2 20

editPlace 10 Test3 Test3

editPlace 10 Test4