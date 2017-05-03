import unittest
from unittest.mock import patch

from .mad_libs import MadLibs


class TestMadLibs(unittest.TestCase):

    def setUp(self):
        self.madlib = MadLibs("first_mad_lib.txt")

    def test_to_make_sure_mad_libs_intialzes_with_text_file(self):
        with open("first_mad_lib.txt") as ml:
            test_mad_lib = ml.read()
        self.madlib.mad_lib_text == test_mad_lib

    def test_that_mad_libs_find_replaceable_method_finds_all_replaceable_words(self):
        self.madlib.find_replaceable()
        self.assertEqual(self.madlib.replaceable_words, ["ADJECTIVE", "NOUN", "VERB", "NOUN"])

    @patch('builtins.input')
    def test_that_mad_libs_enter_new_words_updates_new_words(self, m_input):
        words = ["volumous", "Plymouth Voyager", "expired", "tea cup"]
        m_input.side_effect = words
        self.madlib.enter_new_words()
        self.assertEqual(self.madlib.new_words, words)

if __name__ == "__main__":
    unittest.main()
