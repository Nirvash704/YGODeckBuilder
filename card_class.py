
class Card:
    '''
    Card super class
    '''
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description
    
    def __str__(self):
        return f'{self.name}'


class Monster(Card):
    '''
    Monster subclass
    '''

    def __init__(self, id, name, description, level, attribute, race, type, atk_pts, def_pts):
        super().__init__(id, name, description)
        self.level = level
        self.attribute = attribute
        self.race = race
        self.type = type
        self.atk_pts = atk_pts
        self.def_pts = def_pts

    def __str__(self):
        return f'{self.name}, {self.level}, {self.atk_pts}, {self.def_pts}'

class Spell(Card):
    '''
    Spell subclass
    type refers to normal, quick, continuous, field, or equip
    '''

    def __init__(self, id, name, description, type):
        super().__init__(id, name, description)
        self.type = type

    def __str__(self):
        return f'{self.name}, {self.type}'

class Trap(Card):
    '''
    Trap subclass
    type refers to normal, continuous, counter
    '''

    def __init__(self, id, name, description, type):
        super().__init__(id, name, description)
        self.type = type

    def __str__(self):
        return f'{self.name}, {self.type}'
