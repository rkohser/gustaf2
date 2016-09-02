import os

from subliminal import download_best_subtitles, save_subtitles
from subliminal.video import Episode
from subliminal.core import search_external_subtitles

from babelfish.language import Language


class FileSubtitler:

    def __init__(self, languages, providers):
        self.languages = languages
        self.providers = providers

    def subtitle(self, episodes):

        # Parse babelfish languages
        bb_lang = {Language.fromietf(l) for l in self.languages}

        # Create subliminal episode set
        sub_episodes = set()
        for episode in episodes:

            ep_path = os.path.join(episode['dir'], episode['filename'])
            sub_episode = Episode.fromguess(ep_path, episode)

            # Look for external subtitles (not done automatically, apparently)
            sub_episode.subtitle_languages |= set(search_external_subtitles(sub_episode.name).values())

            sub_episodes.add(sub_episode)

        # download subtitles in the specified language
        subl_subtitles = download_best_subtitles(sub_episodes, bb_lang, providers=self.providers)

        for video, subtitles in subl_subtitles.items():

            save_subtitles(video, subtitles)

            # save subtitle languages in episode dict