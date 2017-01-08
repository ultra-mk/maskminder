import unittest

from maskminder import maskminder as s


class ChordTest(unittest.TestCase):

    @classmethod
    def setUpClass(ChordTest):
        ChordTest.Cmaj = s.Chord('C', 'major')
        ChordTest.Dmin = s.Chord('D', 'minor')

    def test_c_major_root(self):
        self.assertEqual('C', ChordTest.Cmaj.root)

    def test_c_major_third(self):
        self.assertEqual('E', ChordTest.Cmaj.third)

    def test_c_major_fifth(self):
        self.assertEqual('G', ChordTest.Cmaj.fifth)

    def test_d_minor_root(self):
        self.assertEqual('D', ChordTest.Dmin.root)

    def test_d_minor_third(self):
        self.assertEqual('F', ChordTest.Dmin.third)

    def test_d_minor_fifth(self):
        self.assertEqual('A', ChordTest.Dmin.fifth)
