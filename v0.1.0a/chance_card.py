import card

class ChanceCard(card.Card):
    def __init__(self, card_id, card_colour, card_description, card_actions):
        super().__init__(card_id, card_colour)
        self.description=card_description
        self.actions=card_actions

    def Show(self):
        return self.description

    def Action(self):
        return self.actions