"""
Tests for biased-stop-words
"""
import random
import unittest
from types import ListType

from biased_stop_words import get_stop_words, BiasedStopWordError


class TestBiasedStopWords(unittest.TestCase):

    def test_get_existing_stop_words(self):
        actual = get_stop_words('en-gendered')
        self.assertTrue(type(actual) is ListType)
        self.assertTrue(len(actual) > 0)

    def test_get_non_existing_stop_words(self):
        self.assertRaises(BiasedStopWordError, get_stop_words, 'non-existant-genre')


if __name__ == '__main__':
    unittest.main()
