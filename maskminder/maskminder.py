frequencies = {'E': '41hz'}

# this will hold he collection of instruments and keys


class MaskMinder(object):

    def __init__(self, tonic):
        self.tonic = tonic

    @property
    def tonic_freq(self):
        return frequencies[self.tonic]

# this will be the parent class that the various instruments
# inherit from
# will map notes to frequencies.


class Frequencies(object):
    human_range = range(20, 20001)

    def __init__(self):
        self.low = Frequencies.human_range[0]
        self.high = Frequencies.human_range[-1]

#essentially a glorified hash table that will take a note and
#octave and return a frequncy.
#maybe thinking about eliminating Frequencies class and just
#building the instruments with note objects

class Note(object):
    FREQUENCIES = {'C':16.35, 'C#':17.32, 'Db':17.32, 'D':18.35, 'D#':19.45, 'Eb':19.45, 'E': 20.60,'F':21.83, 'F#':23.12, 'Gb':23.12, 'G':24.50, 'G#':25.96, 'Ab':25.96, 'A':27.50, 'A#':29.14, 'Bb':29.14, 'B':30.87}


    def __init__(self, name, octave):
        self.name = name
        self.octave = octave

    @property
    def frequency(self):
        return Note.FREQUENCIES[self.name] * (2**self.octave)

class Instrument(object):

    def __init__(self, low_note = None, high_note = None):
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


