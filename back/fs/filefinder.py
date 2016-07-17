import os
import guessit


class FileFinder:

    def __init__(self, dirs_, types=tuple()):
        self._dirs = dirs_
        self.types = types

    def find(self):
        episodes = list()

        for dir_ in self._dirs:
            for root, dummy, files_ in os.walk(dir_):
                for filename in files_:
                    if filename.endswith(self.types):
                        info = guessit.guessit(os.path.join(root, filename))
                        if info and info['type'] == 'episode':
                            info['dir'] = root
                            info['filename'] = filename
                            episodes.append(info)
        return episodes

