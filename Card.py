class Card:
    '''
    Class that represents the card. It as these attributes: suit, char and hidden.
    The card is hidden by default and can be revealed if needed.
    '''
    def __init__(self,suit,char):
        '''
        Initialises the card class.
        
        :param suit: Suit attribute signified by a string.
        :param char: Rank of card signified by a tuple that has 
        the rank signified by a string 
        and the value signified by an integer.
        '''
        self.suit=suit
        self.char=char
        self.hidden=True
    
    def __str__(self):
        '''
        Returns the card.
        Output: Returns a string.
        If card is hidden, returns "Card".
        If not, Returns the card saying the suit and rank.
        '''
        if self.hidden==True:
            return "Card"
        return f'Card({self.suit},{self.char[0]})'
    
    def isHidden(self):
        '''
        Reveals if the card is hidden or not.
        
        Output: self.hidden, a boolean value.
        '''
        return self.hidden
    
    def reveal(self):
        '''
        Flips self.hidden to false revealing the card.
        '''
        self.hidden=False
    
    def hide(self):
        '''
        Flips self.hidden to true concealing the card.
        '''
        self.hidden=True

    def get_value(self):
        '''
        Gets the value of the card from the tuple.
        Output: Integer value of the card's point value.
        '''
        return self.char[1]

