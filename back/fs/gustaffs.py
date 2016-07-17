from fs.filefinder import FileFinder
from fs.filemover import FileMover

import common.configurator as config


if __name__ == '__main__':

    settings = config.get()

    ff = FileFinder(settings['source_dirs'], ('mkv', 'avi', 'mp4'))
    fm = FileMover(settings['dest_dir'])

    episodes = ff.find()
    fm.move(episodes)
