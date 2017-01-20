from maskminder import note_instrument as ni
from maskminder import scale_chord as sc


def main():
    note = ni.Note('G', 1)
    scale = sc.Scale('C', 'mixolydian')
    print(note.frequency)
    print(scale.notes)

if __name__ == '__main__':
    main()
