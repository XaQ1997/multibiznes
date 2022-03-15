import card

class PropertyCard(card.Card):
    def __init__(self, card_id, card_name, card_colour, card_value):
        super().__init__(card_id, card_colour)
        self.name=card_name
        self.value=card_value
        self.rent=card_value
        self.owners=[]

    def add_owner(self, player):
        self.owners.append(player)

    def del_owner(self, player):
        for owner in range(len(self.owners)):
            if self.owners[owner]==player:
                self.owners.pop(owner)
                return