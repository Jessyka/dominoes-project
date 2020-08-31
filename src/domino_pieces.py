import json
from random import shuffle

def get_random_sorted_pieces():
    pieces = []
    try:
        with open('src/domino_pieces.json') as json_file:
            data = json.load(json_file)
            for p in data['pieces']:
                pieces.append(DominoPiece(p['right_side'], p['left_side']))

    except:
        print('An error occurred when tried to read from domino_pieces repository file.')

    shuffle(pieces)
    return pieces


class DominoPiece:
    def __init__(self, right, left):
        self.right = right
        self.left = left