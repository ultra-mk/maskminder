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

    def test_bass_low(self):
        bass = i.BassGuitar()
        self.assertEqual(41.20, bass.low_frequency)

    def test_bass_high(self):
        bass = i.BassGuitar()
        self.assertEqual(174.64, bass.high_frequency)

    def test_guitar_low(self):
        guitar = i.Guitar()
        self.assertEqual(82.4, guitar.low_frequency)

    def test_guitar_high(self):
        guitar = i.Guitar()
        self.assertEqual(587.2, guitar.high_frequency)