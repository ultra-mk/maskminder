import unittest

from maskminder import maskminder as s


class ScaleTest(unittest.TestCase):
    Bb_chromatic = ['Bb', 'B', 'C', 'Db', 'D',
                    'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A']

    @classmethod
    def setUpClass(ScaleTest):
        ScaleTest.Cmaj = s.Scale('C', 'major')
        ScaleTest.Bbmaj = s.Scale('Bb', 'major')
        ScaleTest.Cnatmin = s.Scale('C', 'natural minor')
        ScaleTest.Dnatmin = s.Scale('D', 'natural minor')
        ScaleTest.Gnatmin = s.Scale('G', 'natural minor')
        ScaleTest.Fmaj = s.Scale('F', 'major')
        ScaleTest.Charm = s.Scale('C', 'harmonic minor')
        ScaleTest.Cdim = s.Scale('C', 'diminished')
        ScaleTest.Caug = s.Scale('C', 'augmented')
        ScaleTest.Gmix = s.Scale('G', 'mixolydian')

    def test_tonic_c(self):
        self.assertEqual('C', ScaleTest.Cmaj.tonic)

    def test_init_scale_not_supported(self):
        self.assertRaises(Exception, s.Scale,
                          'D', 'melodic minor')

    def test_chromatic_scale_type_c(self):
        self.assertEqual(['C', 'C#', 'D', 'D#', 'E',
                          'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'], ScaleTest.Cmaj.chromatic_type(s.Scale.CHROMATIC))

    def test_chromatic_scale_type_Bb(self):
        self.assertEqual(ScaleTest.Bb_chromatic, ScaleTest.Bbmaj.chromatic_type(
            s.Scale.CHROMATIC_FLAT))

    def test_determine_cromatic_C(self):
        self.assertEqual(s.Scale.CHROMATIC, ScaleTest.Cmaj.chromatic)

    def test_determine_cromatic_Bb(self):
        self.assertEqual(ScaleTest.Bb_chromatic, ScaleTest.Bbmaj.chromatic)

    def test_notes_C_major(self):
        self.assertEqual(['C', 'D', 'E', 'F', 'G', 'A', 'B'],
                         ScaleTest.Cmaj.notes)

    def test_notes_Bb_major(self):
        self.assertEqual(['Bb', 'C', 'D', 'Eb', 'F', 'G', 'A'],
                         ScaleTest.Bbmaj.notes)

    def test_notes_C_natural_minor(self):
        self.assertEqual(['C', 'D', 'Eb', 'F', 'G', 'Ab',
                          'Bb'], ScaleTest.Cnatmin.notes)

    def test_notes_D_natural_minor(self):
        self.assertEqual(['D', 'E', 'F', 'G', 'A', 'Bb', 'C'],
                         ScaleTest.Dnatmin.notes)

    def test_notes_g_natural_minor(self):
        self.assertEqual(['G', 'A', 'Bb', 'C', 'D', 'Eb',
                          'F'], ScaleTest.Gnatmin.notes)

    def test_notes_f_major(self):
        self.assertEqual(['F', 'G', 'A', 'Bb', 'C', 'D', 'E'],
                         ScaleTest.Fmaj.notes)

    def test_notes_c_harmonic_minor(self):
        self.assertEqual(['C', 'D', 'Eb', 'F', 'G', 'Ab',
                          'B'], ScaleTest.Charm.notes)

    def test_notes_c_dim(self):
        self.assertEqual(['C', 'D', 'Eb', 'F', 'Gb', 'Ab', 'A', 'B'],
                         ScaleTest.Cdim.notes)

    def test_notes_c_aug(self):
        self.assertEqual(['C', 'D#', 'E', 'G', 'G#', 'B'],
                         ScaleTest.Caug.notes)

    def test_notes_G_mix(self):
        self.assertEqual(['G', 'A', 'B', 'C', 'D', 'E', 'F'],
                         ScaleTest.Gmix.notes)
