import unittest

from maskminder import maskminder as s


class ChordTest(unittest.TestCase):

    @classmethod
    def setUpClass(ChordTest):
        ChordTest.Cmaj = s.Chord('C')
        ChordTest.Dmin = s.Chord('Dm')
        ChordTest.Fdim = s.Chord('F dim')
        ChordTest.Csharpdim = s.Chord('C# dim')
        # ChordTest.Caug = s.Chord('C aug')

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

    def test_c_sharp_dim_third(self):
        self.assertEqual('E', ChordTest.Csharpdim.third)

    def test_c_sharp_dim_fifth(self):
        self.assertEqual('G', ChordTest.Csharpdim.fifth)

    # def test_c_aug_root(self):
    #     self.assertEqual('C', ChordTest.Caug.root)

    # def test_c_aug_third(self):
    #     self.assertEqual('E', ChordTest.Caug.third)

    # def test_c_aug_fifth(self):
    #     self.assertEqual('G#', ChordTest.Caug.fifth)
