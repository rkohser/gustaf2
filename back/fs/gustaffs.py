from fs.filefinder import FileFinder
from fs.filemover import FileMover
from fs.filesubtitler import FileSubtitler

import common.configurator as config


if __name__ == '__main__':

    settings = config.get()

    ff = FileFinder(settings['source_dirs'], ('mkv', 'avi', 'mp4'))
    fm = FileMover(settings['dest_dir'])
    fs = FileSubtitler(settings['subtitle_languages'], settings['subtitle_providers']);

    episodes = ff.find()
    fm.move(episodes)
    fs.subtitle(episodes)
