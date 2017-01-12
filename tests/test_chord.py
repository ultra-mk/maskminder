import unittest

from maskminder import maskminder as s


class ChordTest(unittest.TestCase):

    @classmethod
    def setUpClass(ChordTest):
        ChordTest.Cmaj = s.Chord('C', 'major')
        ChordTest.Dmin = s.Chord('D', 'minor')
        ChordTest.Fdim = s.Chord('F', 'diminished')
        ChordTest.Csharpdim = s.Chord('C#', 'diminished')
        ChordTest.Caug = s.Chord('C', 'augmented')
        # this is holding a mock chord object so I can develop the chord parser
        ChordTest.parser = s.Chord('C', 'major')

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

    def test_c_aug_root(self):
        self.assertEqual('C', ChordTest.Caug.root)

    def test_c_aug_third(self):
        self.assertEqual('E', ChordTest.Caug.third)

    def test_c_aug_fifth(self):
        self.assertEqual('G#', ChordTest.Caug.fifth)

    def test_chord_parser_major(self):
        self.assertEqual(
            ('C', 'major'), ChordTest.parser.parser('C'))

    def test_chord_parser_minor(self):
        self.assertEqual(('D', 'minor'), ChordTest.parser.parser('Dm'))

    def test_chord_parser_dim(self):
        self.assertEqual(('E', 'diminished'),
                         ChordTest.parser.parser('E dim'))

    def test_chord_parser_dom_seventh(self):
        self.assertEqual(('G', 'seventh'), ChordTest.parser.parser('G7'))
