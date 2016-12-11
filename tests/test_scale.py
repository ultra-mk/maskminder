import unittest

from maskminder import maskminder as s


class ScaleTest(unittest.TestCase):

    @classmethod
    def setUpClass(ScaleTest):
        ScaleTest.c = s.Scale('C')

    def test_tonic_c(self):
        self.assertEqual('C', ScaleTest.c.tonic)

    def test_determine_cromatic_c(self):
        self.assertEqual(s.Scale.CROMATIC, ScaleTest.c.determine_chromatic())
