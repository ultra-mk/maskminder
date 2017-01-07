class MaskMinder(object):

    def __init__(self, tonic):
        self.tonic = tonic


class Note(object):
    FREQUENCIES = {'C': 16.35, 'C#': 17.32, 'Db': 17.32, 'D': 18.35, 'D#': 19.45, 'Eb': 19.45, 'E': 20.60, 'F': 21.83,
                   'F#': 23.12, 'Gb': 23.12, 'G': 24.50, 'G#': 25.96, 'Ab': 25.96, 'A': 27.50, 'A#': 29.14, 'Bb': 29.14, 'B': 30.87}

    def __init__(self, name, octave):
        self.name = name
        self.octave = octave

    @property
    def frequency(self):
        return Note.FREQUENCIES[self.name] * (2**self.octave)


class Instrument(object):

    def __init__(self, low_note=None, high_note=None):
        self.low_note = low_note
        self.high_note = high_note

    @property
    def low_frequency(self):
        return self.low_note.frequency

    @property
    def high_frequency(self):
        return self.high_note.frequency

    @property
    def frequency_range(self):
        return range(self.low_frequency, self.high_frequency)


class BassGuitar(Instrument):

    def __init__(self):
        Instrument.__init__(self, Note('E', 1), Note('F', 3))


class Guitar(Instrument):

    def __init__(self):
        Instrument.__init__(self, Note('E', 2), Note('D', 5))


class Scale(object):
    CHROMATIC = ['C', 'C#', 'D', 'D#', 'E',
                 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    CHROMATIC_FLAT = ['C', 'Db', 'D', 'Eb',
                      'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']

    FLAT_KEYS = [('F', 'major'), ('C', 'natural minor'),
                 ('D', 'natural minor'), ('C', 'natural minor'), ('G', 'natural minor')]

    FORMULA = {'major': [0, 2, 4, 5, 7, 9, 11],
               'natural minor': [0, 2, 3, 5, 7, 8, 10]}

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
