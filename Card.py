class Card:
    def __init__(self,suit,char,val):
        self.suit=suit
        self.char=char
        self.val=val
        self.hidden=True
    
    def __str__(self):
        if self.hidden==True:
            return "Card"
        return f'Card({self.suit},{self.char})'
    
    def isHidden(self):
        return self.hidden
    
    def reveal(self):
        self.hidden=False

    def get_char(self):
        return self.char
