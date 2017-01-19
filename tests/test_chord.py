import unittest

from maskminder import scale_chord as s


class ChordTest(unittest.TestCase):

    @classmethod
    def setUpClass(ChordTest):
        ChordTest.Cmaj = s.Chord('C')
        ChordTest.Dmin = s.Chord('Dm')
        ChordTest.Fdim = s.Chord('F dim')
        ChordTest.Csharpdim = s.Chord('C# dim')
        ChordTest.Caug = s.Chord('C aug')
        ChordTest.G7 = s.Chord('G7')
        ChordTest.Dmaj7 = s.Chord('Dmaj7')

    def test_c_major_root(self):
        self.assertEqual('C', ChordTest.Cmaj.root)

    def test_c_major_third(self):
        self.assertEqual('E', ChordTest.Cmaj.third)

    def test_c_major_fifth(self):
        self.assertEqual('G', ChordTest.Cmaj.fifth)

    def test_c_major_seventh(self):
        self.assertEqual(None, ChordTest.Cmaj.seventh)

    def test_d_minor_root(self):
        self.assertEqual('D', ChordTest.Dmin.root)

    def test_d_minor_third(self):
        self.assertEqual('F', ChordTest.Dmin.third)

    def test_d_minor_fifth(self):
        self.assertEqual('A', ChordTest.Dmin.fifth)

    def test_d_minor_seventh(self):
        self.assertEqual(None, ChordTest.Dmin.seventh)

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

    def test_c_aug_root(self):
        self.assertEqual('C', ChordTest.Caug.root)

    def test_c_aug_third(self):
        self.assertEqual('E', ChordTest.Caug.third)

    def test_c_aug_fifth(self):
        self.assertEqual('G#', ChordTest.Caug.fifth)

    def test_g7_root(self):
        self.assertEqual('G', ChordTest.G7.root)

    def test_g7_third(self):
        self.assertEqual('B', ChordTest.G7.third)

    def test_g7_fifth(self):
        self.assertEqual('D', ChordTest.G7.fifth)

    def test_g7_seventh(self):
        self.assertEqual('F', ChordTest.G7.seventh)

    def test_Dmaj7_root(self):
        self.assertEqual('D', ChordTest.Dmaj7.root)

    def test_Dmaj7_third(self):
        self.assertEqual('F#', ChordTest.Dmaj7.third)

    def test_Dmaj7_fifth(self):
        self.assertEqual('A', ChordTest.Dmaj7.fifth)

    def test_Dmaj7_seventh(self):
        self.assertEqual('C#', ChordTest.Dmaj7.seventh)

if __name__ == '__main__':
    unittest.main()
