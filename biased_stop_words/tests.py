"""
Tests for biased-stop-words
"""
import random
import unittest
from types import ListType, StringType

from biased_stop_words import BiasedStopWordError, Genre, genres, get_stop_words


class TestGetStopWords(unittest.TestCase):

    def test_get_existing_stop_words(self):
        actual = get_stop_words('gendered')
        self.assertTrue(type(actual) is ListType)
        self.assertTrue(actual)

    def test_get_multiple_existing_stop_words(self):
        actual = get_stop_words('gendered', 'us-names')
        self.assertTrue(type(actual) is ListType)
        self.assertTrue(actual)

    def test_get_no_supplied_genres(self):
        self.assertRaises(BiasedStopWordError, get_stop_words)

    def test_get_non_existing_genre(self):
        self.assertRaises(BiasedStopWordError, get_stop_words, 'non-existant-genre')


class TestGenre(unittest.TestCase):

    def test_existing_genre(self):
        actual = Genre('gendered').get_words()
        self.assertTrue(type(actual) is ListType)
        self.assertTrue(actual)

    def test_not_existing_genre(self):
        self.assertRaises(BiasedStopWordError, Genre, 'non-existant-genre')


class TestGenres(unittest.TestCase):

    def test_existing_genre(self):
        actual = genres()
        self.assertTrue(type(actual) is StringType)
        self.assertTrue(actual)


if __name__ == '__main__':
    unittest.main()
