class Player:
    def __init__(self, player_id, player_name, player_colour, player_money):
        self.id=player_id
        self.name=player_name
        self.colour=player_colour
        self.money=player_money

        self.position=[0, 1]
        self.cards={}

    def pay(self, tax):
        if tax>=0:
            self.money-=tax
        else:
            print("Nie można zapłacić podatku o ujemnej wartości")

    def get(self, salary):
        if salary>=0:
            self.money+=salary
        else:
            print("Nie można otrzymać pieniędzy o ujemnej wartości")

    def buy(self, card):
        self.cards[card.name]=card
        self.pay(card.value)

    def sell(self, card):
        self.cards[card.name]=None
        self.get(card.value/2)