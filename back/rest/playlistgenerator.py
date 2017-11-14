import lxml
import requests

'''
Created on 14 nov. 2017

@author: roland
'''

class PlaylistGenerator(object):
    '''
    classdocs
    '''


    def __init__(self, show):
        '''
        Constructor
        '''
        self.show = show
        
    def generate(self):
        
        episodes = self.collect_episodes()
        for episode in episodes:
            pass
    
    def collect_episodes(self):
        
        payload = {
            'where': '{"title":"%s"}' % self.show
        }
        return requests.get('http://localhost:5001/episodes', params=payload).json()['_items']
        