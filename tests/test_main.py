import unittest

from maskminder import __main__ as m


class MainTest(unittest.TestCase):

    def get_key_from_user(self):
        self.assertEqual('is s thing on?', m.get_key_from_user())


if __name__ == '__main__':
    unittest.main()
