import random

# Define the Card class
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit


    def __str__(self):
        return f"{self.rank} of {self.suit}"

# Define the Deck class
class Deck:
    def __init__(self):
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        self.cards = [Card(rank, suit) for suit in suits for rank in ranks]

    def shuffle(self):
        random.shuffle(self.cards)

    def count(self):
        return len(self.cards)

    def deal(self, num):
        dealt_cards = []
        for _ in range(num):
            if self.cards:
                dealt_cards.append(self.cards.pop())
        return dealt_cards

    # Main program
def main():
    print("Card Dealer\n")
    deck = Deck()
    deck.shuffle()
    print(f"I have shuffled a deck of {deck.count()} cards.")

    num_cards = int(input("\nHow many cards would you like?: "))
    dealt_cards = deck.deal(num_cards)

    print("\nHere are your cards:")
    for card in dealt_cards:
        print(card)

    print(f"\nThere are {deck.count()} cards left in the deck.")
    print("\nGood luck!")

if __name__ == "__main__":
        main()
