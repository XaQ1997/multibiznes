import csv
import datetime
import itertools
import random

import board
import chance_field
import game
import player
import policeman_field
import prison_field
import property_field
import start_field
import tax_field

class TextInterface:
    def __init__(self):
        self.boards=[]
        self.players=[]
        self.Game=None
        self.start_date=None
        self.log=None
        self.path=''

    def menu(self):
        while True:
            print('Wybierz opcję:')
            print('[N]owa gra')
            print('[W]czytaj grę')
            print('W[y]jdź z gry')

            choice=input()

            if choice=='n' or choice=='N':
                self.new_game()
            if choice=='w' or choice=='W':
                self.load()
            if choice=='y' or choice=='Y':
                return

    def load(self):
        pass

    def new_game(self):
        self.path=input("Podaj ścieżkę bezwględną zapisów: ")

        self.start_date=datetime.datetime.now()
        self.log=open(f'{self.path}/{self.start_date}/log.txt', 'w')

        number_players=int(input("Podaj liczbę graczy: "))

        for i in range(number_players):
            player_name=input("Podaj nazwę gracza: ")
            player_colour=input("Podaj kolor gracza: ")

            play=player.Player(i, player_name, player_colour, 3000)

            self.players.append(play)

            self.log.write(f'<{datetime.datetime.now()}> \tDodano gracza {player_name} o kolorze {player_colour}')
            self.log.close()

            print('DODANO GRACZA')

        self.log=open(f'{self.path}/{self.start_date}/log.txt', 'w')

        random.shuffle(self.players)

        self.log.write(f'<{datetime.datetime.now()}> \tPrzestosowano graczy')

        b=board.Board('000')
        self.boards.append(b)

        self.Game=game.Game(self.boards, self.players)

        self.log.write(f'<{datetime.datetime.now()}> \tUruchomiono grę')

        self.log.close()

        f=open(f'{self.path}/{self.start_date}/start_configs.txt', 'w')

        f.write(f'Liczba graczy: {len(self.players)}')

        for player in range(len(self.players)):
            f.write(f'\tGracz {self.players[player].name} posiadający pionek o kolorze {self.players[player].colour}')

        f.write('')

        for board in range(self.boards):
            f.write(f'Plansza o id {self.boards[board].id}')

        f.close()
        self.log.close()

        self.game()

    def game(self):
        number_players=len(self.players)
        number_rolls=0

        turn=[0, 0]

        for index in itertools.count(0):
            self.log = open(f'{self.path}/{self.start_date}/log.txt', 'w')

            if turn[1]+1==number_players:
                turn[1]=0
                turn[0]+=1
            else:
                turn[1]+=1

            self.log.write(f'<{datetime.datetime.now()}> \tTura: {turn[0]} \n\tKolej gracza {self.players[turn[1]].name}')

            self.close()

            print(f'Tura gracza {self.players[turn[1]].name}')

            f=open(f'{self.path/{self.start_date}/turns.txt', 'w')
            f.write(f'Tura: {turn}')

            for board in range(len(self.boards)):
                print(f'\nPlansza o id {self.boards[board].id}')

                for field in range(len(self.boards[board].fields)):
                    if len(self.player_locate(board, field))==0:
                        print(f'\t[{self.boards[board].fields[field].id}]')
                    else:
                        print(f'\t[{self.boards[board].fields[field].id}] \t{self.player_locate(board, field)}')

                print('\n')

            for i in range(len(self.Game.prisons)):
                for board in range(len(self.boards)):
                    for field in range(len(self.boards[board].fields)):
                        if self.Game.prisons[i]==self.boards[board].fields[field].id:
                            for p in self.boards[board].fields[field].get_prisoners():
                                if self.players[turn[1]].name==p:
                                    if self.boards[board].fields[field].get_prisoners()[p]>0:
                                        self.boards[board].fields[field].get_prisoners()[p]-=1
                                        print(f'Gracz {p} siedzi w więzieniu. Pozostało mu {self.boards[board].fields[field].get_prisoners()[p]}')

                                for play in range(len(self.players)):
                                    if p==play:
                                        f.write(f'\t[{self.players[play].colour}]'
                                                f'\t{self.boards[self.players[play].position[0]]}'
                                                f'\t{self.boards[self.players[play].position[0]].fields[self.players[play].position[1]]}'
                                                f'\tWięzień \t{3-self.boards[board].fields[field].get_prisoners[p]}')
                                        continue

                                    if play==len(self.players)-1 and i==len(self.Game.prisons)-1:
                                        f.write(f'\t[{self.players[play].colour}]'
                                                f'\t{self.boards[self.players[play].position[0]]}'
                                                f'\t{self.boards[self.players[play].position[0]].fields[self.players[play].position[1]]}'
                                                '\tPoza więzieniem \t0')

            f.close()

            choice=''

            f=open(f'{self.path}/{self.start_date}/data.txt', 'w')

            for play in range(len(self.players)):
                f.write(f'Gracz {self.players[play].name} \n\tPieniądze: {self.players[play].money} \n\tKarty:')

                for card in range(len(self.players[play].cards)):
                    f.write(f'\t\t{self.players[play].cards[card]}')

                print('')

            f.close()

            while True:
                print(f"Menu gracza {self.players[turn[1]].name}:")
                print('\t[P]okaż moje dane')
                print('\tPokaż [k]arty innych graczy')
                print('\t[R]usz się')

                choice=input('Wybierz opcję; ')

                if choice=='p' or choice=='P':
                    print(f'Pieniądze: {self.players[turn[1]].money}')
                    print('Karty:')

                    for card in self.players[turn[1]].cards:
                        print(f'\t[{card}]: {self.players[turn[1]].cards[card]}')

                if choice=='k' or choice=='K':
                    for p in range(len(self.players)):
                        if p==turn[1]:
                            continue

                        print(f'Gracz {self.players[p].name}: ')

                        for card in self.players[p]:
                            print(f'\t[{card}]: {self.players[p].cards[card]}')

                if choice=='r' or choice=='R':
                    number_double=0

                    while number_double<3:
                        left_dice, right_dice, double=self.Game.dices.roll()

                        number_rolls+=1

                        f=open(f'{self.path}/{self.start_date}/rolls.txt' 'w')
                        f.write(f'[{number_rolls}] \t<{left_dice}; {right_dice}> \t{double} ({number_double})')
                        f.close()

                        print(f'Wynik rzutu koścmi: {left_dice} {right_dice} \nDubel: {double}')

                        self.log=open(f'{self.path}/{self.start_date}/log.txt', 'w')
                        self.log.write(f'<{datetime.datetime.now()}> \tWynik rzutu koścmi: {left_dice} {right_dice} \nDubel: {double}')

                        self.Game.go(turn[1], (0, left_dice+right_dice))

                        print(f'Gracz {self.players[turn[1]].name} wylądował na polu {self.players[turn[1]].position} \n')

                        self.log.write(f'<{datetime.datetime.now()}> \tGracz {self.players[turn[1]].name} wylądował na polu {self.players[turn[1]].position}')
                        self.log.close()

                        input()

                        if double==False:
                            break

                        for board in range(len(self.boards)):
                            for field in range(len(1, self.boards[board].fields+1)):
                                if self.players[turn[1]].position==[board, field]:
                                    if self.boards[board].fields[field] is start_field.StartField:
                                        self.players[turn[1]].money==self.boards[board].fields[field].get_salary()

                                        break

                                    if self.boards[board].fields[field] is policeman_field.PolicemanField:
                                        self.players[player].position[board, self.boards[board].fields[field].sending_id]

                                        for id in range(len(self.boards[board].fields)):
                                            if self.boards[board].fields[id].id==sending_id:
                                                self.boards[board].fields[id].add_prisoner(self.players[turn[1]])
                                                break

                                        break

                                    if self.boards[board].fields[field] is tax_field.TaxField:
                                        self.players[turn[1]].pay(self.boards[board].fields[field].tax)

                                        break

                                    if self.players[board].fields[field] is chance_field.ChanceField:
                                        card=self.boards[board].cards['chance_cards'][self.boards[board].fields[field].colour].pop(0)
                                        self.boards[board].cards['chance_cards'][self.boards[board].fields[field].colour].append(card)

                                        card.Show()
                                        card.Action()

                                        break

                                    if self.boards[board].fields[field] is property_field.PropertyField:
                                        for card in range(len(self.boards[board].cards['property_cards'])):
                                            id=self.boards[board].cards['property_cards'][card].id
                                            if self.boards[board].fields[field].id==f'{id[:3]}{id[6:]}':
                                                if self.boards[board].cards['property_cards'][card].owners is None:
                                                    print(f'Czy gracz {self.players[turn[1]]} chce kupić kartę właśności {self.boards[board].fields[field].name}?')
                                                    print('\t[T]ak \n\t[N]ie?')
                                                    choice=input("Wybierz opcję: ")
                                                    if choice=='t' or choice=='T':
                                                        self.boards[board].cards['property_cards'][card].add_owner(self.players[turn[1]])
                                                        self.players[turn[1]].cards.append(card)

                                                    break

                                                if self.boards[board].cards['property_cards'][card].owners!=self.players[turn[1]]:
                                                    self.players[turn[1]].pay(self.boards[board].cards['property_cards'][card].value)

                                                    for owner in range(len(self.boards[board].cards['property_cards'][card].owners)):
                                                        self.boards[board].cards['property_cards'][card].owners.get(self.boards[board].cards['property_cards'][card].value)

                                        break

                        number_double+=1

                    break

            if self.players[turn[1]].money<0:
                turn[1]-=1
                for board in range(len(self.boards)):
                    for card in range(len(sef.boards[board].cards['property_cards'])):
                        for owner in range(len(self.boards[board].cards['property_cards'][card].owners)):
                            if self.boards[board].cards['property_cards'][card].owners[owner]==self.players[turn[1]]:
                                self.boards[board].cards['property_card'][card].del_owner(self.players[turn[1]])

                self.players.pop(turn[1])
                self.Game.players.pop(turn[1])

            if len(self.players)==1:
                print('KONIEC GRY!!!')
                exit()

    def player_locate(self, board, field):
        result=[]

        for i in range(len(self.players)):
            if self.players[i].position==[board, field+1]:
                result.append(self.players[i].colour)

        return result

interface=TextInterface()

interface.menu()