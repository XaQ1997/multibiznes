import dice
import prison_field

class Game:
    def __init__(self, boards=[], players=[]):
        self.boards=boards
        self.players=players

        self.dices=dice.Dice()

        self.prisons=[]

        for board in range(len(self.boards)):
            for field in range(len(self.boards[board].fields)):
                if self.boards[board].fields[field] is prison_field.PrisonField:
                    self.prisons.append(self.boards[board].fields[field].id)

    def go(self, player, move=(0, 0)):
        if len(self.boards[move[0]].fields)<self.players[player].position[1]+move[1]:
            self.players[player].position[1]-=len(self.boards[move[0]].fields)
            self.players[player].get(self.boards[move[0]].fields[0].get_salary())

            is_prisoner=False

            for i in range(len(self.Game.prisons)):
                for board in range(len(self.boards)):
                    for field in range(len(self.boards[board].fields)):
                        if self.prisons[i]==self.boards[board].fields[field].id:
                            for p in self.boards[board].fields[field].get_prisoners():
                                if self.players[turn[1]].name==p:
                                    if self.boards[board].fields[field].get_prisoners()[p]>0:
                                        self.players[player].pay(self.boards[move[0]].fields[0].get_salary())
                                        is_prisoner=True
                                        break

                        if is_prisoner==True:
                            break

                    if is_prisoner==True:
                        break

                if is_prisoner==True:
                    break

        if self.players[player].position[1]+move[1]<0:
            self.players[player].position+=len(self.boards[move[0]].fields)

        self.players[player].position[0]+=move[0]
        self.players[player].position[1]+=move[1]