import Card
import Enums
import random

def addToHand(card,h,total):
    card.reveal()
    h.append(card)
    if card.val==1:
        val=drewAce()
    else:
        val=card.val
    total+=val
    return total
    
def addToDealer(card,h,total):
    h.append(card)
    total+=card.val
    return total

def revealCards(lst):
    for card in lst:
        print(card)

def determineWinner(yourTotal,dealerTotal):
    if yourTotal > 21 and dealerTotal > 21:
        return "Tie"
    elif (yourTotal <= 21 and yourTotal > dealerTotal) or dealerTotal > 21:
        return "You win!"
    elif yourTotal < dealerTotal or yourTotal > 21:
        return "You lose!"
    else:
        return "Tie"
    
def drewAce():
    while True:
        ace_val=int(input(("You drew an ace. Do you wish to make it a 1 or 11?")))
        if ace_val==1:
            return 1
            break
        elif ace_val==11:
            return 11
            break
        else:
            print("please input either 1 or 11.")
    
    
def main():
    try:
        while True:
            deck=[]
            hand=[]
            dealer=[]
            yourTotal=0
            dealerTotal=0
            for suits in Enums.Suits:
                for char in Enums.Char:
                    deck.append(Card.Card(suits.value,char.name,char.value))
            random.shuffle(deck)
            yourTotal=addToHand(deck.pop(),hand,yourTotal)
            yourTotal=addToHand(deck.pop(),hand,yourTotal)
            addToDealer(deck.pop(),dealer,dealerTotal)
            dealerTotal=addToDealer(deck.pop(),dealer,dealerTotal)
            dealer[-1].reveal()
            print("You currently have these cards in your hand: ")
            revealCards(hand)
            print("Your total: ", yourTotal)
            print("The dealer currently have these cards in their hand: ")
            revealCards(dealer)
            print("Dealer's total: ", dealerTotal)
            while True:
                decision=input("Do you wish to stay or hit?").lower()
                if decision=="stay":
                    if dealerTotal < 17:
                        addToDealer(deck.pop(),dealer,dealerTotal)
                    print(determineWinner(yourTotal,dealerTotal))
                    print("At the end, you had these cards in your hand: ")
                    revealCards(hand)
                    print("Your total: ", yourTotal)
                    for card in dealer:
                        card.reveal()
                    print("At the end, the dealer had these cards in their hand: ")
                    revealCards(dealer)
                    print("Dealer's total: ", dealerTotal)
                    print("Starting new round")
                    break
                elif decision=="hit":
                    yourTotal=addToHand(deck.pop(),hand,yourTotal)
                    if dealerTotal < 17:
                        addToDealer(deck.pop(),dealer,dealerTotal)
                    if yourTotal>=21 or dealerTotal>=21:
                        print(determineWinner(yourTotal,dealerTotal))
                        print("At the end, you had these cards in your hand: ")
                        revealCards(hand)
                        print("Your total: ", yourTotal)
                        for card in dealer:
                            card.reveal()
                        print("At the end, the dealer had these cards in their hand: ")
                        revealCards(dealer)
                        print("Dealer's total: ", dealerTotal)
                        print("Starting new round")
                        break
                elif decision=="quit":
                    print("Exiting program now")
                    exit()
                else:
                    print("please input stay or hit.")
                print("You currently have these cards in your hand: ")
                revealCards(hand)
                print("Your total: ", yourTotal)
                print("The dealer currently have these cards in their hand: ")
                revealCards(dealer)
                print("Dealer's total: ", dealerTotal)
    except KeyboardInterrupt:
        print("Exiting program now")
        exit()
main()
