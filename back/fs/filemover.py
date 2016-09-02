import os
import shutil


class FileMover:

    def __init__(self, destination):
        self.destination = destination

    def move(self, episodes, keep_original=False):
        
        dest_pattern = self.destination + '\\{title}\\{season}\\{episode}'
        for episode in episodes:
            dest_dir = dest_pattern.format_map(episode)

            source_url = os.path.join(episode['dir'], episode['filename'])
            dest_url = os.path.join(dest_dir, episode['filename'])

            if not os.path.exists(dest_dir):
                os.makedirs(dest_dir)

            if keep_original:
                shutil.copy2(source_url, dest_url)
            else:
                shutil.move(source_url, dest_url)

            episode['dir'] = dest_dir
