import unittest
from smalldsl.field_selection import generate_field_selection


class TestFieldSelection(unittest.TestCase):
    def test_field_selection(self):
        mylis = ["name", "code", "population"]
        self.assertEqual(generate_field_selection(mylis), 'name, code, population')
        mylis = ["name", "population"]
        self.assertEqual(generate_field_selection(mylis), 'name, spopulation')

if __name__ == '__main__':
    unittest.main()