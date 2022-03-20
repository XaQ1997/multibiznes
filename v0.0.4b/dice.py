import random

class Dice:
    def __init__(self):
        pass

    def roll(self):
        left_dice=random.randint(1, 6)
        right_dice=random.randint(1, 6)
        double=False

        if left_dice==right_dice:
            double=True
        else:
            double=False

        return left_dice, right_dice, double