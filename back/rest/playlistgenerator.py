from jinja2 import Environment, PackageLoader, select_autoescape
import requests
import pathlib


def tofileurl(absolute_path):
    return pathlib.Path(absolute_path).as_uri()
    


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
        
        self.env = Environment(
            loader=PackageLoader('rest', 'templates'),
            autoescape=select_autoescape(['j2, xspf'])
        )
        self.env.filters['tofileurl'] = tofileurl
        
    def generate(self):
        
        episodes = self.collect_episodes()
        if len(episodes):
            template = self.env.get_template('xspf.j2')
            return template.render(show=self.show, episodes=episodes)
        else:
            return None

    
    def collect_episodes(self):
        
        payload = {
            'where': '{"title":"%s"}' % self.show
        }
        return requests.get('http://localhost:5001/episodes', params=payload).json()['_items']
        