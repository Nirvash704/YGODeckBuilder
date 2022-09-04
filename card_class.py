
from asyncio import protocols


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

    @classmethod
    def from_dict(cls, data):
        '''
        Create Card object from dictionary
        '''
        id = data.get('id', None)
        name = data.get('name', None)
        description = data.get('desc', None)
        return cls(id, name, description)

    def data(self):
        '''
        Return dictionary of class attributes
        '''
        attribute_dict = {
            'id': self.id,
            'name': self.name,
            'description': self.description
        }
        return attribute_dict

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

    def __init__(self, id, name, description, level, attribute, race, type, atk_pts, def_pts, scale = None, linkval = None, linkmarkers = None):
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

    @classmethod
    def from_dict(cls, data):
        '''
        Create Monster Card object from dictionary
        '''
        id = data.get('id', None)
        name = data.get('name', None)
        description = data.get('desc', None)
        level = data.get('level', None)
        attribute = data.get('attribute', None)
        race = data.get('race', None)
        type = data.get('type', None)
        atk_pts = data.get('atk', None)
        def_pts = data.get('def', None)
        scale = data.get('scale', None)
        linkval = data.get('linkval', None)
        linkmarkers = data.get('linkmarkers', None)
        return cls(id, name, description, level, attribute, race, type, atk_pts, def_pts, scale, linkval, linkmarkers)
    
    def data(self):
        '''
        Return dictionary of class attributes
        '''
        attribute_dict = {
            'id': self.id,
            'name': self.name,
            'level': self.level,
            'atk_pts': self.atk_pts,
            'def_pts': self.def_pts,
            'attribute': self.attribute,
            'race': self.race,
            'type': self.type,
            'scale': self.scale,
            'linkval': self.linkval,
            'linkmarkers': self.linkmarkers,
            'description': self.description
        }
        return attribute_dict

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

    @classmethod
    def from_dict(cls, data):
        '''
        Create Spell Card object from dictionary
        '''
        id = data.get('id', None)
        name = data.get('name', None)
        description = data.get('desc', None)
        type = data.get('type', None)
        return cls(id, name, description, type)
    
    def data(self):
        '''
        Return dictionary of class attributes
        '''
        attribute_dict = {
            'id': self.id,
            'name': self.name,
            'type': self.type,
            'description': self.description
        }
        return attribute_dict


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

    @classmethod
    def from_dict(cls, data):
        '''
        Create Trap Card object from dictionary
        '''
        id = data.get('id', None)
        name = data.get('name', None)
        description = data.get('desc', None)
        type = data.get('type', None)
        return cls(id, name, description, type)
    
    def data(self):
        '''
        Return dictionary of class attributes
        '''
        attribute_dict = {
            'id': self.id,
            'name': self.name,
            'type': self.type,
            'description': self.description
        }
        return attribute_dict


# mysticmine = Spell(69, 'mystic mine', 'floodgate', 'Field')
# busterblader = Monster(332, 'buster blader', 'kills dragons', 7, 'EARTH', 'Warrior', 'Effect Monster', 2600, 2300, None, None, None)
# imperialorder = Trap(222, 'imperial order', 'stops spells', 'Countinuous')

# dark_magician = {
#     'id': 12341,
#     'name': 'Dark Magician',
#     'desc': 'This is a strong monster!',
#     'level': 7,
#     'attribute': 'DARK',
#     'race': 'Spellcaster',
#     'type': 'Effect Monster',
#     'atk': 2500,
#     'def': 2100
# }

# card1 = Spell.from_dict(dark_magician)

# raigeki = {
#     'id': 31231,
#     'name': 'Raigeki',
#     'desc': 'Destroy all of your opponent\' monsters',
#     'type': 'Spell Card'
# }


# protocol = {
#     'id': 4242121,
#     'name': 'Altergeist Protocol',
#     'desc': 'Does Altergeist stuff!',
#     'type': 'Trap Card'
# }

# card1 = Monster.from_dict(dark_magician)
# card2 = Spell.from_dict(raigeki)
# card3 = Trap.from_dict(protocol)

# print(card1.data())
# print(card2.data())
# print(card3.data())

# print(mysticmine.data().items())
# print(busterblader.data().items())
# print(imperialorder.data().items())