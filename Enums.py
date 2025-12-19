from enum import Enum

class Suits(Enum):
    HEART = "♡"
    DIAMOND = "♢"
    SPADE = "♠"
    CLUB = "♣"

class Char(Enum):
    ACE = ("ACE",1)
    TWO = ("TWO",2)
    THREE = ("THREE", 3)
    FOUR = ("FOUR", 4)
    FIVE = ("FIVE", 5)
    SIX = ("SIX", 6)
    SEVEN = ("SEVEN", 7)
    EIGHT = ("EIGHT", 8)
    NINE = ("NINE", 9)
    TEN = ("TEN", 10)
    JACK = ("JACK", 10)
    QUEEN = ("QUEEN", 10)
    KING = ("KING", 10)
