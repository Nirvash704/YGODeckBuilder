import requests
import pandas as pd

class Database:
    '''
    Yugioh Card Database
    '''

    def __init__(self):
        self.card_db = []
    
    def __string__(self):
        output = ''
        for item in self.card_db:
            output += item.get('name') + '\n'
        return output
    
    # Getter for card_db
    def card_db(self):
        return self.card_db
    
    def ygopro_search(self, card_name):
        '''
        Returns card data matching card_name. 
        If no match is found, return None.
        '''

        url = 'https://db.ygoprodeck.com/api/v7/cardinfo.php?'
        params = {'name': card_name}
        r = requests.get(url, params)

        # r.raise_for_status()  # Raise exception for status error codes

        if r.json().get('data') == None:
            return None
        return r.json().get('data')[0]

    def search(self, card_name):
        '''
        Returns card data matching card_name. 
        If no match is found, return None. 
        If card_name does not match any locally stored cards, 
        call ygopro_search(). Store result locally if match is found.
        '''

        for item in self.card_db:
            if item['name'].lower() == card_name.lower():
                return item
        
        card_data = self.ygopro_search(card_name)
        if not card_data == None:
            self.card_db.append(card_data)
        
        return card_data
    
    def export_csv(self):
        '''
        Exports contents of Database into CSV file.
        '''
        
        df = pd.DataFrame(self.card_db)
        df.to_csv('local_card_database.csv', index=False)
        print('Output to CSV')