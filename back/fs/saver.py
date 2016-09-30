import requests
import json
from fs.serializer import GustafSerializer

class Saver:

    def __init__(self):
        pass

    def save(self, episodes):

        for episode in episodes:
            json_episode = json.dumps(episode, cls=GustafSerializer, indent=4)
            headers = {'content-type': 'application/json'}
            response = requests.post("http://127.0.0.1:5001/episodes", data=json_episode, headers=headers)
            response.raise_for_status()

            with open("episode.json", "w") as json_file:
                json_file.write(json_episode)
