class Scale(object):
    # ALERT - take a look at using integer notation
    # https://en.wikipedia.org/wiki/Pitch_class#Integer_notation
    CHROMATIC = ['C', 'C#', 'D', 'D#', 'E',
                 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    CHROMATIC_FLAT = ['C', 'Db', 'D', 'Eb',
                      'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']

    FLAT_KEYS = [('F', 'major'), ('C', 'natural minor'),
                 ('D', 'natural minor'), ('C', 'natural minor'),
                 ('G', 'natural minor'), ('C', 'harmonic minor'),
                 ('C', 'diminished'), ('F', 'diminished')]

    FORMULA = {'major': [0, 2, 4, 5, 7, 9, 11],
               'natural minor': [0, 2, 3, 5, 7, 8, 10],
               'harmonic minor': [0, 2, 3, 5, 7, 8, 11],
               'diminished': [0, 2, 3, 5, 6, 8, 9, 11],
               'augmented': [0, 3, 4, 7, 8, 11],
               'mixolydian': [0, 2, 4, 5, 7, 9, 10]}

    def __init__(self, tonic, scale_type):
        self.tonic = tonic
        if scale_type in Scale.FORMULA.keys():
            self.scale_type = scale_type
        else:
            raise Exception('This scale is not yet supported.')

    def chromatic_type(self, chromatic_scale):
        tonic_index = chromatic_scale.index(self.tonic)
        return chromatic_scale[tonic_index:] + chromatic_scale[0:tonic_index]

    @property
    def chromatic(self):
        if self.tonic[-1] == 'b' or self.key in Scale.FLAT_KEYS:
            return self.chromatic_type(Scale.CHROMATIC_FLAT)
        else:
            return self.chromatic_type(Scale.CHROMATIC)

    @property
    def key(self):
        return (self.tonic, self.scale_type)

    @property
    def notes(self):
        return [self.chromatic[i] for i in Scale.FORMULA[self.scale_type]]


class Chord(Scale):
    TYPES = {'m': 'minor', 'dim': 'diminished',
             'aug': 'augmented', '7': 'seventh', 'maj7': 'major seventh'}

    CHORD_TO_SCALE = {'minor': 'natural minor',
                      'seventh': 'mixolydian', 'major seventh': 'major'}

    def __init__(self, chord):
        self.tonic = self.tonic(chord)
        self.chord_type = self.chord_type(chord)
        self.scale_type = self.scale_type(self.chord_type)

    def scale_type(self, chord_type):
        return Chord.CHORD_TO_SCALE.get(chord_type, chord_type)

    def chord_type(self, chord):
        return Chord.TYPES.get(chord.replace(self.tonic, '').strip(), 'major')

    def tonic(self, chord):
        if len(chord) == 1:
            return chord[0]
        elif chord[1] == '#' or chord[1] == 'b':
            return chord[0:2]
        else:
            return chord[0]

    @property
    def root(self):
        return self.notes[0]

    @property
    def third(self):
        return self.notes[2]

    @property
    def fifth(self):
        return self.notes[4]

    @property
    def seventh(self):
        if self.chord_type == 'seventh' or self.chord_type == 'major seventh':
            return self.notes[6]
