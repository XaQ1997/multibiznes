import csv
import os
import random

import chance_card
import chance_field
import policeman_field
import property_card
import property_field
import prison_field
import relax_field
import start_field
import tax_field

class Board:
    def __init__(self, board_id):
        self.id=board_id

        self.fields=[]
        self.cards={}

        with open(f'{board_id}/{board_id}.csv', newline='') as csvfile:
            filereader=csv.reader(csvfile, delimiter=';')
            next(filereader)

            for line in filereader:
                field_id=line[0]
                field_name=line[1]
                field_type=line[2]
                field_colour=line[3]
                field_value=line[4]

                field=None

                if field_type=='chance_field':
                    field=chance_field.ChanceField(field_id, field_name, field_colour)

                if field_type=='policeman_field':
                    field=policeman_field.PolicemanField(field_value, field_id, field_name)

                if field_type=='property_field':
                    field=property_field.PropertyField(field_id, field_name, field_colour, int(field_value))

                if field_type=='prison_field':
                    field=prison_field.PrisonField(field_id, field_name)

                if field_type=='relax_field':
                    field=relax_field.RelaxField(field_name, field_id)

                if field_type=='start_field':
                    field=start_field.StartField(int(field_value), field_id, field_name)

                if field_type=='tax_field':
                    field=tax_field.TaxField(field_id, field_name, int(field_value))

                self.fields.append(field)

        with open(f'{board_id}/{board_id}0.csv', newline='') as csvfile:
            filereader=csv.reader(csvfile, delimiter=';')
            next(filereader)

            self.cards['property_cards']=[]

            for line in filereader:
                card_id=line[0]
                card_name=line[1]
                card_colour=line[2]
                card_value=line[3]

                card=property_card.PropertyCard(card_id, card_name, card_colour, card_value)

                self.cards['property_cards'].append(card)

        files=os.listdir(f'{board_id}/{board_id}1')

        self.cards['chance_cards']={}

        err=0

        for index in range(len(files)):
            while os.path.isfile(f'{board_id}/{board_id}1/{board_id}1{index+err}'):
                err+=1

            id=''

            if index+err<10:
                id=f'0{index+err}'
            else:
                id=f'{index+err}'

            with open(f'{board_id}/{board_id}1/{board_id}1{id}.csv', newline='') as csvfile:
                filereader=csv.reader(csvfile, delimiter=';')
                next(filereader)

                card_colour=''

                if index+err==0:
                    card_colour='blue'
                if index+err==1:
                    card_colour='red'

                self.cards['chance_cards'][card_colour]=[]

                for line in filereader:
                    card_id=line[0]
                    card_description=line[1]
                    card_actions=line[2]

                    card=chance_card.ChanceCard(card_id, card_colour, card_description, card_actions)

                    self.cards['chance_cards'][card_colour].append(card)

            random.shuffle(self.cards['chance_cards'][card_colour])

    def Show(self):
        return self.fields