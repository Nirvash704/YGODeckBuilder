import requests

class Database:
    '''
    Yugioh Card Database
    '''

    def __init__(self):
        self.card_list = []

# search_name = 'Accesscode Talker'
# params = {'name': search_name}
# r = requests.get('https://db.ygoprodeck.com/api/v7/cardinfo.php', params).json()
# print(r)