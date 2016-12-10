import unittest

from maskminder import maskminder as m


class MMTest(unittest.TestCase):

    @classmethod
    def setUpClass(MMTest):
        MMTest.ins = m.MaskMinder()

    def test_init(self):
        self.assertEqual("This is the init method", MMTest.ins.stuff)
