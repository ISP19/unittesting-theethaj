import unittest
from listutil import unique


class ListUtilTest(unittest.TestCase):
    """Test the results of the unique class in many cases. """

    def test_single_item_list(self):
        self.assertEqual(['hi'], unique(['hi']))
        self.assertEqual([5], unique([5]))
        self.assertEqual(['20'], unique(['20']))

    def test_more_than_one_items_list(self):
        self.assertEqual(['b', 'a'], unique(['b', 'a', 'a', 'b', 'b', 'b', 'a', 'a']))
        self.assertEqual(['apple', 'bat', 'cat'], unique(['apple', 'bat', 'cat', 'cat', 'apple']))
        self.assertEqual(['1', '2', '3', '4', '5'], unique(['1', '2', '3', '4', '5']))

    def test_list_in_list(self):
        self.assertEqual([['b'], 'a', 'b'], unique([['b'], 'a', 'a', 'b', 'b', 'b', 'a', 'a']))
        self.assertEqual(['apple', 'bat', ['cat'], 'cat'], unique(['apple', 'bat', ['cat'], 'cat', 'apple']))
        self.assertEqual(['1', '2', ['3'], '4', ['5']], unique(['1', '2', ['3'], '4', ['5']]))

    def test_empty_list(self):
        self.assertEqual([], unique([]))

if __name__ == '__main__':
    unittest.main()