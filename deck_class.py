from card_class import *
import pandas as pd
from random import shuffle

class Deck:
    '''
    Simple deck class to manage groups of card data.
    MAX copies of same card name: 3
    Main Deck limit:  60 cards
    Extra Deck limit: 15 cards
    Side Deck limit:  15 cards
    '''
    
    def __init__(self, deck_name):
        self.deck_name = deck_name
        self.main = []
        self.extra = []
        self.side = []
    
    def __str__(self):
        deck_str = 'Main Deck \n'
        for card in self.main:
            deck_str += f'{card.name} \n'
        
        deck_str += '\nExtra Deck \n'
        for card in self.extra:
            deck_str += f'{card.name} \n'
            
        deck_str += '\nSide Deck \n'
        for card in self.side:
            deck_str += f'{card.name} \n'
        
        return deck_str
    
    def card_count(self, card_name):
        '''
        Return the amount of cards with card_name in all decks.
        '''
        count = 0
        for card in (self.main + self.extra + self.side):
            if card_name == card.name:
                count += 1
        return count

    def is_extra(self, card):
        '''
        Return True if card is extra deck type.
        Otherwise, return False.
        '''
        card_type = card.type
        extra_type = {'Fusion', 'Synchro', 'XYZ', 'Link'}
        if extra_type.intersection(card_type.split()) != set():
            return True
        else:
            return False
    
    def add(self, card):
        '''
        Add card to Main/Extra Deck.
        MAX copies of same card name: 3
        Main Deck limit:  60 cards
        Extra Deck limit: 15 cards
        '''
        if self.card_count(card.name) >= 3:
            print('Cannot add more than 3 copies of a card')
            return
        
        if self.is_extra(card):
            if len(self.extra) < 15:
                self.extra.append(card)
            else:
                print('Cannot add more than 15 cards in Extra deck')
        else:
            if len(self.main) < 60:
                self.main.append(card)
            else:
                print('Cannot add more than 60 cards in Main deck')
    
    def add_to_side(self, card):
        '''
        Add card to Side Deck.
        MAX copies of same card name: 3
        Side Deck limit: 15 cards
        '''
        if self.card_count(card.name) >= 3:
            print('Cannot add more than 3 copies of a card')
            return
        
        if len(self.side) < 15:
            self.side.append(card)
        else:
            print('Cannot add more than 15 cards in Side deck')
    
    def remove(self, card_name):
        '''
        Remove card with card_name from Main/Extra Deck.
        '''
        for card in self.main:
            if card.name == card_name:
                self.main.remove(card)
                return
        
        for card in self.extra:
            if card.name == card_name:
                self.extra.remove(card)
                return
    
    def remove_from_side(self, card_name):
        '''
        Remove card with card_name from Side Deck.
        '''
        for card in self.side:
            if card.name == card_name:
                self.side.remove(card)
                return
    
    def get_sort_priority(self, card):
        '''
        Return a priority value based on card type.
        '''
        priority_type = {Monster: 1, Spell: 2, Trap: 3}
        priority_extra = {
            'Pendulum': 0.01,
            'Ritual': 0.02,
            'Fusion': 0.1,
            'Synchro': 0.2,
            'XYZ': 0.3,
            'Link': 0.4
        }
        priority = priority_type.get(type(card), 0)
        if type(card) == Monster:
            for item in card.type.split():
                priority += priority_extra.get(item, 0)
        
        return priority
    
    def sort_deck(self):
        '''
        Sort Main, Extra, and Side Decks.
        '''
        self.main.sort(key=self.get_sort_priority)
        self.extra.sort(key=self.get_sort_priority)
        self.side.sort(key=self.get_sort_priority)
        
    def shuffle(self):
        '''
        Randomly shuffles contents of Main Deck.
        '''
        shuffle(self.main)
    
    def draw(self):
        '''
        Pop and return top card from Main Deck.
        '''
        if len(self.main) > 0:
            return self.main.pop()
        else:
            return None
    
    def search(self, card_name):
        '''
        Remove and return card from Main Deck. 
        If card not found, return None.
        '''
        for card in self.main:
            if card.name == card_name:
                self.main.remove(card)
                return card
            else:
                return None
    
    def export_csv(self):
        '''
        Export deck contents to CSV file.
        '''

        main_dict = []
        extra_dict = []
        side_dict = []

        for card in self.main:
            main_dict.append(card.data())

        for card in self.extra:
            extra_dict.append(card.data())

        for card in self.side:
            side_dict.append(card.data())


        df = pd.DataFrame(main_dict + extra_dict + side_dict)
        
        try:
            df.to_csv(f'{self.deck_name}.csv', index=False)
            print('Outputed to CSV')
        except:
            print('An error has occured')




mysticmine = Spell(69, 'mystic mine', 'floodgate', 'Field')
busterblader = Monster(332, 'buster blader', 'kills dragons', 7, 'EARTH', 'Warrior', 'Effect Monster', 2600, 2300, None, None, None)
Accesscode = Monster(332, 'Accesscode', 'popoff to close game', None, 'DARK', 'Cyberse', 'Link', 2300, None, None, 4, ["Top", "Left", "Bottom", "Right"])
imperialorder = Trap(222, 'imperial order', 'stops spells', 'Countinuous')

deck1 = Deck('Buster Blader')

deck1.add(mysticmine)
deck1.add(busterblader)
deck1.add(imperialorder)
deck1.add(imperialorder)
deck1.add(imperialorder)
deck1.add(imperialorder)
deck1.add(Accesscode)

deck1.add_to_side(Accesscode)

print(deck1.__str__())
print('-------------------------')

# deck1.remove('imperial order')
# deck1.remove('Accesscode')
# deck1.remove_from_side('Accesscode')

# print(deck1.__str__())

# deck1.export_csv()