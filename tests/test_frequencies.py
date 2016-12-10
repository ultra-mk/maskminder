import unittest

from maskminder import maskminder as f


class FTest(unittest.TestCase):

    @classmethod
    def setUpClass(FrequencyTest):
        FTest.ins = f.Frequencies()

    def test_low_frequency(self):
        self.assertEqual(20, FTest.ins.low)

    def test_high_frequency(self):
        self.assertEqual(20000, FTest.ins.high)
