class Card:
    def __init__(self,suit,char):
        self.suit=suit
        self.char=char
        self.hidden=True
    
    def __str__(self):
        if self.hidden==True:
            return "Card"
        return f'Card({self.char})'
    
    def isHidden(self):
        return self.hidden
    
    def reveal(self):
        self.hidden=False

    def get_value(self):
        return self.char[1]

