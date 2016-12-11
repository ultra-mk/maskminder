import unittest

from maskminder import maskminder as n


class NTest(unittest.TestCase):

    def test_C2(self):
        C2 = n.Note('C', 2)
        self.assertEqual(65.4, C2.frequency)

