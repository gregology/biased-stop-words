import json
import os

__VERSION__ = (2017, 5, 9, 1)
CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
STOP_WORDS_DIR = os.path.join(CURRENT_DIR, 'biased-stop-words')


def get_version():
    """
    :rtype: basestring
    """
    return ".".join(str(v) for v in __VERSION__)


class BiasedStopWordError(Exception):
    pass



def get_stop_words(genre):
    """
    :type genre: basestring

    :rtype: list
    """

    genre_filename = os.path.join(STOP_WORDS_DIR, genre + '.txt')
    try:
        with open(genre_filename, 'rb') as genre_file:
            stop_words = [line.decode('utf-8').strip()
                          for line in genre_file.readlines()]
    except IOError:
        raise BiasedStopWordError('genre not found, please consider adding it')

    return stop_words
