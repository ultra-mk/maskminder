import unittest

from maskminder import maskminder as s


class ScaleTest(unittest.TestCase):

    @classmethod
    def setUpClass(ScaleTest):
        ScaleTest.c = s.Scale('C', 'major')
        ScaleTest.Bb = s.Scale('Bb', 'major')

    def test_tonic_c(self):
        self.assertEqual('C', ScaleTest.c.tonic)

    def test_determine_cromatic_c(self):
        self.assertEqual(s.Scale.CROMATIC, ScaleTest.c.chromatic)

    def test_determine_cromatic_Bb(self):
        self.assertEqual(s.Scale.CROMATIC_FLAT, ScaleTest.Bb.chromatic)
