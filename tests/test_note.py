import unittest

from maskminder import note_instrument as n


class NTest(unittest.TestCase):

    def test_C2(self):
        C2 = n.Note('C', 2)
        self.assertEqual(65.4, C2.frequency)

    def test_A4(self):
        A4 = n.Note('A', 4)
        self.assertEqual(440.0, A4.frequency)

    def test_C_sharp_6(self):
        Csharp = n.Note('C#', 6)
        self.assertEqual(1108.48, Csharp.frequency)

    def test_d_flat_6(self):
        Db = n.Note('Db', 6)
        self.assertEqual(1108.48, Db.frequency)

if __name__ == '__main__':
    unittest.main()
