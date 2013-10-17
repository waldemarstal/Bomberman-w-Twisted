

Jest to prosta gra siecia w architekturze klient - serwer, korzystajacej z komunikacji za pomoca frameworka Twisted. Jest to komunikacja miedzyprocesowa w jezyku
Python (strukture komunikacyjna za pomoca m.in. modułu cPickle*).

Zasady gry:
	Celem gry dla kazdego z graczy jest zajecie jak najwiekszej czesci planszy przez otoczenie tej czesci minami. 
		Gracz moze:
			 - poruszyc sie o jedno pole w góre, dół, lewo lub prawo,
			 - połozyc mine na polu, w którym aktualnie sie znajduje,
			 - zakonczyc gre przez wysłanie do serwera komendy sprawdzajacej ile pól zajał kazdy z graczy,
			 - wysłac pusta wiadomosc do serwera w celu pobrania aktualnej listy min

	Gracz zajał tyle pól, ile miesci sie w obszarze, w którym sie aktualnie znajduje, ograniczonym brzegami planszy i
	minami. Miny ograniczaja obszar z czterech boków, nigdy po przekatnej. Jesli którys z graczy wejdzie na pole, na którym
	jest mina (bez znaczenia który z graczy ja postawił), ginie. Jesli dwóch graczy znajdzie sie na tym samym obszarze, ich
	wynik jest taki sam. Oznacza to, ze gracz powinien zakonczyc gre tylko, jesli jest pewien, ze
	znajduje sie w zamknietym obszarze.

Gra składa sie z dwóch aplikacji:
	 serwer — nasłuchuje na porcie. Obsługuje cała mechanike gry: przechowuje aktualny rozkład min i połozenie kazdego z graczy oraz odpowiada na akcje wysyłane od 		klientów.
	 klient — podłacza sie do serwera gry. Wyswietla na ekranie aktualny stan gry (połozenia miny i graczy).
			Obsługuje akcje gracza: odczytuje który klawisz wcisnał gracz i wysyła odpowiednia informacje do serwera.

Position — obiekt opisujacy pozycje na planszy. Ma dwa pola: y i x, gdzie y oznacza numer wiersza, a x numer kolumny. 
Mine  —instancja tego obiektu oznacza jedna mine. Kazda mina przechowuje swoja pozycje (position) i identyfikator
	gracza, który ta mine postawił (playerId).
Countdown — obiekt uzyty przy odliczaniu przed rozpoczeciem gry. Przechowuje numer pokazywany przy odliczaniu
	(number), wielkosc planszy (mapSize) w obiekcie Position, przesyłana, zeby klient mógł wyswietlic plansze jeszcze
	przez poczatkiem gry, oraz identyfikator gracza, potrzebny klientowi, zeby wyswietlił informacje którym pionkiem
	steruje gracz.
Map — przechowuje wszystkie informacje, o aktualnym stanie gry: rozmieszczenie min (mines), w postaci listy
	obiektów Mine, oraz pozycje kazdego z graczy (playersPositions) - liste obiektów Position.
PlayerAction — opisuje akcje gracza. Posiada tylko jedno pole - action, w którym trzyma pojedynczy znak przyporzadkowany do którejs z akcji klienta.
Result — obiekt przechowujacy wynik całej gry, w dwóch polach.

* cPickle do serializacji i deserializacji obiektów przesyłanych miedzy serwerem a klientami.
--------------------------------------------------

Twisted - to właściwie nie serwer aplikacyjny ale duży framework oparty na zdarzeniach i asynchronicznej pracy. Posiada spore możliwości i wygląda na dojrzały projekt. Twisted 2.0 korzysta z interfejsów Zope3. Niestety jest trudny do nauki ze wzgl na koniecznośc uwzględniania specyfiki pracy asynchronicznej. Dokumentacja też jest słaba i wyłącznie w języku angielskim.

Twisted implementuje wzorzec reaktora.

---------------------------------------------------

http://twistedmatrix.com/trac/wiki

http://twistedmatrix.com/documents/12.2.0/core/howto/servers.html

http://krondo.com/blog/?page_id=1327

http://twistedmatrix.com/documents/current/core/howto/index.html

http://www.python.rk.edu.pl/w/p/python-i-programowanie-sieciowe/

http://www.ii.uni.wroc.pl/~marcinm/dyd/obiekty/projekty.html

--------------------------------------------------