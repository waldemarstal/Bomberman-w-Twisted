class Position( object ):
    """
    Klasa posiadajaca dwa pola (wspolrzedne):
        - x
        - y
    """
    def __init__(self, y, x):
        """
        Inicjalizacja klasy Position.

        uwaga: wspolrzedne podawane sa w postaci: y, x 
        """
        self.y = y # int
        self.x = x # int
    
    def __str__(self):
        """
        Metoda zwracajaca wspolrzedne w postaci string'a
        """
        return "(%d, %d)" % (self.y, self.x)
    
    def __eq__(self, other):
        """
        Metoda sprawdzajaca rownosc wspolrzednych
        """
        return self.y == other.y and self.x == other.x

class Mine( object ):
    """
    Klasa posiadajaca dwa pola:
        - objekt klasy Position
        - id gracza stawiajacego mine
    """
    def __init__(self, position, playerId):
        """
        Inicjalizacja klasy Mine
        """
        self.position = position # objekt Position
        self.playerId = playerId # id gracza, ktory podlozyl bombe

class Countdown( object ):
    """
    Klasa posiadajaca pola:
        - numer (odliczania)
        - wielkosc mapy
        - id gracza
    """
    def __init__(self, number, mapSize, playerId):
        """
        Inicjalizacja klasy Countdown
        """
        self.number = number # int
        self.mapSize = mapSize # objekt Position
        self.playerId = playerId # int

class Map( object ):
    """
    Klasa posiadajaca pola:
        - liste min
        - liste pozycji graczy
    """
    def __init__(self, mines, playersPositions):
        """
        Inicjalizacja klasy Map
        """
        self.mines = mines # lista objektow Mine
        self.playersPositions = playersPositions # lista objektow Position 

class PlayerAction( object ):
    """
    Klasa posiadajaca pole  wskazujace na rodzaj akcji gracza
    """
    def __init__(self, action):
        """
        Inicjalizacja klasy PlayerAction
        """
        self.action = action # znak identyfikujacy akcje gracza

class Result( object ):
    """
    Klasa posiadajaca pola:
        - liste zwyciescow
        - liste wynikow
    """
    def __init__(self, winners, scores):
        """
        Inicjalizacja klasy Result
        """
        self.winners = winners # lista zwyciescow
        self.scores = scores # lista wynikow