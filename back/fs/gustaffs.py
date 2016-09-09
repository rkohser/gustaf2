from celery import Celery

from fs.filefinder import FileFinder
from fs.filemover import FileMover
from fs.filesubtitler import FileSubtitler

import common.configurator as config


#Specify mongodb host and datababse to connect to
BROKER_URL = 'mongodb://localhost:27017/gustaf_fs'

celery_fs = Celery('gustaf_fs',broker=BROKER_URL)

#Loads settings for Backend to store results of jobs 
celery_fs.config_from_object('celeryconfig')

@celery_fs.task
def refresh():
    settings = config.get()

    ff = FileFinder(settings['source_dirs'], settings['source_extensions'])
    fm = FileMover(settings['dest_dir'])
    fs = FileSubtitler(settings['subtitle_languages'], settings['subtitle_providers']);

    episodes = ff.find()
    fm.move(episodes, keep_original=True)
    fs.subtitle(episodes)

