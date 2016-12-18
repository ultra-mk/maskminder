import unittest

from maskminder import maskminder as s


class ScaleTest(unittest.TestCase):
    Bb_chromatic = ['Bb', 'B', 'C', 'Db', 'D',
                    'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A']

    @classmethod
    def setUpClass(ScaleTest):
        ScaleTest.C = s.Scale('C', 'major')
        ScaleTest.Bb = s.Scale('Bb', 'major')

    def test_tonic_c(self):
        self.assertEqual('C', ScaleTest.C.tonic)

    def test_chromatic_scale_type(self):
        self.assertEqual(['C', 'C#', 'D', 'D#', 'E',
                          'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'], ScaleTest.C.chromatic_scale_type(s.Scale.CHROMATIC))

    def test_chromatic_scale_type(self):
        self.assertEqual(ScaleTest.Bb_chromatic, ScaleTest.Bb.chromatic_scale_type(
            s.Scale.CHROMATIC_FLAT))

    def test_determine_cromatic_c(self):
        self.assertEqual(s.Scale.CHROMATIC, ScaleTest.C.chromatic)

    def test_determine_cromatic_Bb(self):
        self.assertEqual(ScaleTest.Bb_chromatic, ScaleTest.Bb.chromatic)
