#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import unittest

import exercice


class TestExercice(unittest.TestCase):
    def setUp(self):
        with open('./data/sample_countries.txt') as f:
            self.countries = [name.replace('\n', '') for name in f.readlines()]

    def test_capitalize_first_letter(self):
        names = [
            'Angola',
            'The Bahamas',
            'Andorra',
            'Antigua and Barbuda',
            'Georgia'
        ]
        altered_names = [x[0].lower() + x[1:] for x in names]
        output = list(map(exercice.capitaliser_pays, altered_names))
        output_first_letters = list(map(lambda name: name[0], output))
        expected_first_letters = list(map(lambda name: name[0], names))
        self.assertListEqual(
            output_first_letters,
            expected_first_letters,
            'Mettre la permiere lettre en majuscule'
        )

    def test_lower_case_names(self):
        altered_names = [country.lower() for country in self.countries]
        output = list(map(exercice.capitaliser_pays, altered_names))
        self.assertListEqual(
            output,
            self.countries,
            'Certaines lettres ne doivent pas etre en minuscules'
        )

    def test_upper_case_names(self):
        altered_names = [country.upper() for country in self.countries]
        output = list(map(exercice.capitaliser_pays, altered_names))
        self.assertListEqual(
            output,
            self.countries,
            'Certaines lettres ne doivent pas etre en majuscule'
        )

    def test_linking_words(self):
        names = [
            'Antigua and Barbuda',
            'Bosnia and Herzegovina'
        ]
        altered_names = [
            'Antigua aNd Barbuda',
            'Bosnia ANd Herzegovina'
        ]
        output = list(map(exercice.capitaliser_pays, altered_names))
        self.assertListEqual(
            output,
            names,
            'Les mots de liaison doivent etre en minuscule'
        )


if __name__ == '__main__':
    if not os.path.exists('logs'):
        os.mkdir('logs')
    with open('logs/tests_results.txt', 'w') as f:
        loader = unittest.TestLoader()
        suite = loader.loadTestsFromModule(sys.modules[__name__])
        unittest.TextTestRunner(f, verbosity=2).run(suite)
