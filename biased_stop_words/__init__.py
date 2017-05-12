import yaml
import os

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
STOP_WORDS_DIR = os.path.join(CURRENT_DIR, 'biased-words')
MAPPING_FILE = os.path.join(STOP_WORDS_DIR, 'stop-word-mapping.yaml')
MAPPING = yaml.load(open(MAPPING_FILE))


def genres():
    return ', '.join(MAPPING.keys())

def get_stop_words(*args):
    if not args:
        raise BiasedStopWordError('include at least one stop word genre')
    stop_words = []
    for genre_name in args:
        stop_words += Genre(genre_name).get_words()
    return list(set(stop_words))


class BiasedStopWordError(Exception):
    pass


class Genre(object):
    def __init__(self, name):
        if name not in MAPPING.keys():
            raise BiasedStopWordError('included genre not ' + genres())
        self.name = name

    def get_words(self):
        words = []
        genre = MAPPING[self.name]
        for filename in genre['files']:
            words += self.__load_words_from_file(filename, genre.get('limit'))
        return words

    def __load_words_from_file(self, filename, limit):
        genre_filename = os.path.join(STOP_WORDS_DIR, filename)
        with open(genre_filename, 'rb') as genre_file:
            if limit:
                return [line.decode('utf-8').strip() for line in genre_file.readlines()][:limit]
            else:
                return [line.decode('utf-8').strip() for line in genre_file.readlines()]
