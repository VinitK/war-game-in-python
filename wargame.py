from random import shuffle

suite = 'H D S C'.split()
ranks = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck:
    def __init__(self):
        print("Creating New Ordered Deck")
        self.allcards = [(s, r) for s in suite for r in ranks]

    def shuffle(self):
        print("Shuffling Deck")
        shuffle(self.allcards)

    def split_in_half(self):
        return self.allcards[:26], self.allcards[26:]


class Hand:
    def __init__(self, cards):
        self.cards = cards

    def __str__(self):
        return f"Contains {len(self.cards)} cards"

    def add(self, added_cards):
        self.cards.extend(added_cards)

    def remove_card(self):
        return self.cards.pop()


class Player:
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def play_card(self):
        drawn_card = self.hand.remove_card()
        print(f"{self.name} has placed {drawn_card[0]}{drawn_card[1]}")
        print("\n")
        return drawn_card

    def remove_war_cards(self):
        war_cards = []
        if len(self.hand.cards) < 3:
            return self.hand.cards
        else:
            for x in range(3):
                war_cards.append(self.hand.cards.pop())
            return war_cards

    def still_has_cards(self):
        """
        :return: True if player still has cards left
        """
        return len(self.hand.cards) != 0


print("Welcome to War, let's begin!")

d = Deck()
d.shuffle()
hand1, hand2 = d.split_in_half()

comp = Player("Computer", Hand(hand1))
name = input("What is your name? ")
user = Player(name, Hand(hand2))

total_rounds = 0
war_count = 0

while user.still_has_cards() and comp.still_has_cards():
    total_rounds += 1
    print(f"Time for round: {total_rounds}")
    print("Here are the current standings")
    print(f"{user.name} has the count: {str(len(user.hand.cards))}")
    print(f"{comp.name} has the count: {str(len(comp.hand.cards))}")
    print("Play a card")
    print("\n")

    table_cards = []

    c_card = comp.play_card()
    u_card = user.play_card()

    table_cards.append(c_card)
    table_cards.append(u_card)

    if c_card[1] == u_card[1]:
        war_count += 1

        print("War!")

        table_cards.extend(user.remove_war_cards())
        table_cards.extend(comp.remove_war_cards())

        if ranks.index(c_card[1]) < ranks.index(u_card[1]):
            user.hand.add(table_cards)
        else:
            comp.hand.add(table_cards)
    else:
        if ranks.index(c_card[1]) < ranks.index(u_card[1]):
            user.hand.add(table_cards)
        else:
            comp.hand.add(table_cards)

print("Game Over")
print(f"Number of Rounds: {str(total_rounds)}")
print(f"A war happened {str(war_count)} times")
if comp.still_has_cards():
    print(f"{user.name} won!")
else:
    print("Computer won!")