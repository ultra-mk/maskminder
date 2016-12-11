import unittest

from maskminder import maskminder as i


class ITest(unittest.TestCase):

    @classmethod
    def setUpClass(ITest):
        ITest.ins = i.Instrument(i.Note('E', 1), i.Note('E', 3))

    def test_generic_instrument_low(self):
        self.assertEqual(41.20, ITest.ins.low_frequency)

    def test_generic_instrument_high(self):
        self.assertEqual(164.8, ITest.ins.high_frequency)

    def test_frequency_range_in(self):
        self.assertTrue(ITest.ins.low_frequency < 51.91 < ITest.ins.high_frequency)

    def test_frequency_range_out(self):
        self.assertFalse(ITest.ins.low_frequency < 5588 < ITest.ins.high_frequency)