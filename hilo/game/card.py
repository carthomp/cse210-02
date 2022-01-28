import random
class Card:
    def __init__(self):
        '''
        Initialize the card with a random number between 1 to 13 and
        assign the values of the letters A , J, Q, K.

        Attributes:
            self (Card): An instance of Card
        '''
        self.value_card = random.randint(1,13)
        self.value = 0
        if self.value_card == 1:
            self.value = "A"
        elif self.value_card == 11:
            self.value = "J"
        elif self.value_card == 12:
            self.value = "Q"
        elif self.value_card == 13:
            self.value = "K"
        else:
            self.value = self.value_card