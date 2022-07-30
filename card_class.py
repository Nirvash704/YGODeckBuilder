
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
    type refers to:
    Effect, Flip Effect, Flip Tuner Effect, Gemini, Normal, Normal Tuner,
    Pendulum Effect, Pendulum Flip Effect, Pendulum Normal, Pendulum Tuner Effect, Ritual Effect,
    Ritual, Spirit, Toon, Tuner, Union Effect
    Fusion, Link, Pendulum Effect Fusion, Synchro, Synchro Pendulum Effect,
    Synchro Tuner, XYZ, XYZ Pendulum
    '''

    def __init__(self, id, name, description, level, attribute, race, type, atk_pts, def_pts, scale, linkval, linkmarkers):
        super().__init__(id, name, description)
        self.level = level
        self.attribute = attribute
        self.race = race
        self.type = type
        self.atk_pts = atk_pts
        self.def_pts = def_pts
        self.scale = scale
        self.linkval = linkval
        self.linkmarkers = linkmarkers

    def __str__(self):
        return f'{self.name}, {self.level}, {self.atk_pts}, {self.def_pts} \n{self.description}'

class Spell(Card):
    '''
    Spell subclass
    type refers to normal, quick, continuous, field, or equip
    '''

    def __init__(self, id, name, description, type):
        super().__init__(id, name, description)
        self.type = type

    def __str__(self):
        return f'{self.name}, {self.type} \n{self.description}'

class Trap(Card):
    '''
    Trap subclass
    type refers to normal, continuous, counter
    '''

    def __init__(self, id, name, description, type):
        super().__init__(id, name, description)
        self.type = type

    def __str__(self):
        return f'{self.name}, {self.type} \n{self.description}'


mysticmine = Spell(69, 'mystic mine', 'floodgate', 'Field')
busterblader = Monster(332, 'buster blader', 'kills dragons', 7, 'EARTH', 'Warrior', 'Effect Monster', 2600, 2300, None, None, None)
imperialorder = Trap(222, 'imperial order', 'stops spells', 'Countinuous')

print(mysticmine)
print(busterblader)
print(imperialorder)