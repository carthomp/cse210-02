import random


class Deck:
    def __init__(self): 
        self.deck = [1,2,3,4,5,6,7,8,9,10,11,12,13]

    def first_card(self):
        return random.choice(self.deck)

    def second_card(self):
        # remove_number = self.deck.index(self.first_card)
        # self.deck.pop(remove_number)
        return random.choice(self.deck)

    # def high(self):
    #     if (self.first_card) < (self.second_card):
    #         return True
    #     else:
    #         return False

        


deck=Deck()

print (deck.first_card())
print(deck.second_card())
# print(deck.high())