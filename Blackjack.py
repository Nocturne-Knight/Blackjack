import Card
import Enums
import random

def drewAce():
    while True:
        ace_val = int(input("You drew an Ace. Choose 1 or 11: "))
        if ace_val == "1":
            return 1
        elif ace_val == "11":
            return 11
        else:
            print("Please enter 1 or 11.")


def addToHand(card, hand, total):
    card.reveal()
    hand.append(card)

    value = card.get_value()

    if value == 1: 
        total += drewAce()
    else:
        total += value

    return total


def addToDealer(card, hand, total):
    hand.append(card)

    value = card.get_value()

    if value == 1:
        total += 11 if total + 11 <= 21 else 1
    else:
        total += value

    return total


def revealCards(cards):
    for card in cards:
        print(card)


def determineWinner(player, dealer):
    if player > 21:
        return "You lose!"
    if dealer > 21:
        return "You win!"
    if player > dealer:
        return "You win!"
    if dealer > player:
        return "You lose!"
    return "Tie"


def buildDeck():
    deck = []
    for suit in Enums.Suits:
        for char in Enums.Char:
            deck.append(Card.Card(suit.value, char.value))
    random.shuffle(deck)
    return deck


def dealerTurn(deck, dealerHand, dealerTotal):
    while dealerTotal < 17:
        dealerTotal = addToDealer(deck.pop(), dealerHand, dealerTotal)
    return dealerTotal


def main():
    try:
        while True:
            deck = buildDeck()
            playerHand = []
            dealerHand = []
            playerTotal = 0
            dealerTotal = 0

            playerTotal = addToHand(deck.pop(), playerHand, playerTotal)
            playerTotal = addToHand(deck.pop(), playerHand, playerTotal)

            dealerTotal = addToDealer(deck.pop(), dealerHand, dealerTotal)
            dealerTotal = addToDealer(deck.pop(), dealerHand, dealerTotal)

            dealerHand[0].reveal() 

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

            print("Final hands:")
            print("Your hand:")
            revealCards(playerHand)
            print("Total:", playerTotal)
            print("Dealer hand:")
            revealCards(dealerHand)
            print("Total:", dealerTotal)

            print("Result:", determineWinner(playerTotal, dealerTotal))
            print("New Round")

    except KeyboardInterrupt:
        print("Exiting program.")
        exit()

main()