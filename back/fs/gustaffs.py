from celery import Celery

from fs.filefinder import FileFinder
from fs.filemover import FileMover
from fs.subtitler import Subtitler
from fs.saver import Saver

import common.configurator as config


#Specify mongodb host and datababse to connect to
BROKER_URL = 'mongodb://server:27017/gustaf_fs'

celery_fs = Celery('gustaf_fs',broker=BROKER_URL)

#Loads settings for Backend to store results of jobs 
celery_fs.config_from_object('fs.celeryconfig')

@celery_fs.task
def refresh():
    settings = config.get()

    ff = FileFinder(settings['source_dirs'], tuple(settings['source_extensions']))
    fm = FileMover(settings['dest_dir'])
    subtitler = Subtitler(settings['subtitle_languages'], settings['subtitle_providers'])
    saver = Saver()

    episodes = ff.find()
    fm.move(episodes, keep_original=False)
    subtitler.subtitle(episodes)
    saver.save(episodes)



