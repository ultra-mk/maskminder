import unittest

from maskminder import maskminder as m


class MMTest(unittest.TestCase):

    @classmethod
    def setUpClass(MMTest):
        MMTest.ins = m.MaskMinder('E')

    def test_tonic_freq(self):
        self.assertEqual('41hz', MMTest.ins.tonic_freq)
