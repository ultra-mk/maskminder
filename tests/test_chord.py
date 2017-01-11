import unittest

from maskminder import maskminder as s


class ChordTest(unittest.TestCase):

    @classmethod
    def setUpClass(ChordTest):
        ChordTest.Cmaj = s.Chord('C', 'major')
        ChordTest.Dmin = s.Chord('D', 'minor')
        ChordTest.Fdim = s.Chord('F', 'diminished')
        ChordTest.Csharpdim = s.Chord('C#', 'diminished')

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

    def test_f_dim_root(self):
        self.assertEqual('F', ChordTest.Fdim.root)

    def test_f_dim_third(self):
        self.assertEqual('Ab', ChordTest.Fdim.third)

    def test_f_dim_fifth(self):
        self.assertEqual('B', ChordTest.Fdim.fifth)

    def test_c_sharp_dim_root(self):
        self.assertEqual('C#', ChordTest.Csharpdim.root)

    def test_c_sharp_dim_root(self):
        self.assertEqual('E', ChordTest.Csharpdim.third)

    def test_c_sharp_dim_root(self):
        self.assertEqual('G', ChordTest.Csharpdim.fifth)
