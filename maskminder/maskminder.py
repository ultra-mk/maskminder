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
