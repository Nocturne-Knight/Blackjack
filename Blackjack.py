import Card
import Enums
import random

def drewAce():
    '''
    This function triggers when an ace is drawn. 
    Outputs either 1 or 11 depending on player's input: the string 1 or 11.
    If in the event something other than 1 or 11 is the input, 
    the function will ask for 1 or 11 again.

    Output: The integer 1 or 11.
    '''
    while True:
        ace_val = input("You drew an Ace. Choose 1 or 11: ")
        if ace_val == "1":
            return 1
        elif ace_val == "11":
            return 11
        else:
            print("Please enter 1 or 11.")


def addToHand(card, hand, total):
    '''
    Adds cards to the player's hand
    
    :param card: Card object that will be added to hand.
    :param hand: The player's hand list that holds their cards.
    :param total: The combined integer points of the player's cards.
    Output total: The combined integer points of the player's cards.
    '''
    card.reveal()
    hand.append(card)

    value = card.get_value()

    if value == 1: 
        total += drewAce()
    else:
        total += value

    return total


def addToDealer(card, hand, total):
    '''
    Adds cards to the dealer's hand
    
    :param card: Card object that will be added to hand.
    :param hand: The dealer's hand list that holds their cards.
    :param total: The combined integer points of the dealer's cards.
    Output total: The combined integer points of the dealer's cards.
    '''
    hand.append(card)

    value = card.get_value()

    if value == 1:
        total += 11 if total + 11 <= 21 else 1
    else:
        total += value

    return total


def revealCards(cards):
    '''
    Docstring for revealCards
    
    :param cards: The list of cards that need to be printed.
    '''
    for card in cards:
        print(card)


def determineWinner(player, dealer):
    '''
    Docstring for determineWinner
    
    :param player: The player's total points as an integer.
    :param dealer: The dealer's total points as an integer.
    Output: String that says who wins and who loses or if it's a tie.
    '''
    if player > 21 and dealer > 21:
        return "Tie"
    elif dealer > 21:
        return "You win!"
    elif player > 21:
        return "You lose!"
    elif player > dealer:
        return "You win!"
    elif dealer > player:
        return "You lose!"
    else:
        return "Tie"


def buildDeck():
    '''
    Builds the deck that loops through the suits 
    and character enums and then shuffles them randomly.
    Output deck: the list of the shuffled cards.
    '''
    deck = []
    for suit in Enums.Suits:
        for char in Enums.Char:
            deck.append(Card.Card(suit.value, char.value))
    random.shuffle(deck)
    return deck


def dealerTurn(deck, dealerHand, dealerTotal):
    '''
    Function that deals with the dealer's turn. 
    
    :param deck: The deck list.
    :param dealerHand: The dealer's hand list.
    :param dealerTotal: The integer of the dealer's total points.
    Output dealerTotal: The integer of the dealer's total points.
    '''
    while dealerTotal < 17:
        dealerTotal = addToDealer(deck.pop(), dealerHand, dealerTotal)
    return dealerTotal


def main():
    '''
    Main game loop.
    '''
    try:
        while True:
            deck = buildDeck()
            playerHand = []
            dealerHand = []
            playerTotal = 0
            dealerTotal = 0
            playerCash = 200
            dealerCash = 200
            bet = None

            playerTotal = addToHand(deck.pop(), playerHand, playerTotal)
            playerTotal = addToHand(deck.pop(), playerHand, playerTotal)

            dealerTotal = addToDealer(deck.pop(), dealerHand, dealerTotal)
            dealerTotal = addToDealer(deck.pop(), dealerHand, dealerTotal)

            dealerHand[0].reveal() 
            
            while type(bet)!=int:
                try:
                    bet=int(input("Enter the amount of money you want to bet (input a positive integer): "))
                    while bet <= 0 or bet > min(playerCash, dealerCash): 
                        print("Error: The input must be positive and below both you and dealer's current cash")
                        bet=None
                        bet=int(input("Enter the amount of money you want to bet: "))
                except ValueError:
                    print("Error: Only positive integers are accepted as an input")
                    bet=None
            playerCash -= bet
            dealerCash -= bet
            while True:
                print("Your hand:")
                revealCards(playerHand)
                print("Total:", playerTotal)

                print("Dealer shows:")
                revealCards(dealerHand)

                if playerTotal >= 21:
                    break

                decision = input("Hit, stay, or quit? ").lower()
  
                if decision == "hit":
                    playerTotal = addToHand(deck.pop(), playerHand, playerTotal)
                elif decision == "stay":
                    break
                elif decision == "quit":
                    print("Exiting program.")
                    exit()
                else:
                    print("Invalid choice.")

            for card in dealerHand:
                card.reveal()

            dealerTotal = dealerTurn(deck, dealerHand, dealerTotal)

            print("Your final hand:")
            revealCards(playerHand)
            print("Total:", playerTotal)
            print("Dealer's final hand:")
            revealCards(dealerHand)
            print("Total:", dealerTotal)

            if playerTotal > 21 and dealerTotal > 21:
                print("Both of you have busted!")
            elif dealerTotal > 21:
                print("Dealer has busted!")
            elif playerTotal > 21:
                print("You busted!")
            else:
                pass
            outcome=determineWinner(playerTotal, dealerTotal)
            print(outcome)
            if outcome == "Tie":
                playerCash += bet
                dealerCash += bet
            elif outcome == "You win!":
                playerCash += bet * 2
            else:
                dealerCash += bet * 2
            if playerCash <= 0 or dealerCash <= 0:
                print("That's it. One of you have ran out of money!")
                print("Do you wish to reset?")
            else:
                print("New Round")
    except KeyboardInterrupt:
        print("Exiting program.")
        exit()

main()
