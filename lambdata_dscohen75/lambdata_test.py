""" Tests for lambdata modules"""

import unittest
from random import randint


from example_module import increment, COLORS, TEST_DF
from oop_example_ds19 import ExoticAnimals


class ExampleUnitTests(unittest.TestCase):
    """Making sure our examples behave as expected"""
    def test_increment(self):
        """Testing that increment adds one to a number."""
        x1 = 5
        y1 = increment(x1)
        x2 = -106
        y2 = increment(x2)
        # Now we make sure the output is as expected with assertions
        self.assertEqual(y1, 6)
        self.assertEqual(y2, -105)

    def test_increment_random(self):
        """Test increment with randomly generated input"""
        x1 = randint(1, 1000000)
        y1 = increment(x1)
        self.assertEqual(y1, x1 + 1)

    def test_colors(self):
        """Testing presence/absence of expected colors. """
        self.assertIn('Orange', COLORS)
        self.assertNotIn('Aquamarine', COLORS)
        self.assertEqual(len(COLORS), 6)


class ExoticAnimalsTests(unittest.TestCase):
    """Tests the instantiation and use of ExoticAnimals """
    def test_name(self):
        """Test that the name field is assigned correctly """
        animal1 = ExoticAnimals('Fred')
        animal2 = ExoticAnimals('Lucy')
        self.assertEqual(animal1.name, 'Fred')
        self.assertEqual(animal2.name, 'Lucy')

    def test_default_color(self):
        """ Test that the default color of a new animal is 'brown'. """
        animal1 = ExoticAnimals('Fred')
        self.assertEqual(animal1.color, 'brown')

    def test_default_mammal(self):
        """ Test that by default a new animal is a mammal """
        animal1 = ExoticAnimals('Fred')
        self.assertEqual(animal1.mammal, True)


if __name__ == '__main__':
    # This conditional is for code that will be run
    # when we execute our file from the command line
    unittest.main()