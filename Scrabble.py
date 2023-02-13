import random
import string

class Scrabble:
    def __init__(self):
        self.letter_values = {'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10}
        self.tile_bag = [letter + str(self.letter_values[letter]) for letter in self.letter_values for i in range(self.letter_values[letter])]
        random.shuffle(self.tile_bag)
        self.players = []
        self.player_tiles = {}
        self.board = {}
        self.word_multipliers = {(7, 7): 3}
        self.letter_multipliers = {}

    def add_player(self, player_name):
        self.players.append(player_name)
        self.player_tiles[player_name] = []

    def draw_tiles(self, player_name, num_tiles=7):
        if not self.players:
            return None
        if player_name not in self.players:
            return None
        if not self.tile_bag:
            return None
        drawn_tiles = [self.tile_bag.pop() for i in range(num_tiles) if self.tile_bag]
        self.player_tiles[player_name].extend(drawn_tiles)
        return drawn_tiles

    def play_word(self, player_name, word, position, direction='across'):
        word = word.upper()
        if player_name not in self.players:
            return None
        if not all(letter in string.ascii_uppercase for letter in word):
            return None
        if not set(word).issubset(set(tile[0] for tile in self.player_tiles[player_name])):
            return None
        if direction not in ('across', 'down'):
            return None
        if not self.check_word_fit(word, position, direction):
            return None

        self.update_player_tiles(player_name, word)
        score = self.calculate_score(word, position, direction)
        self.update_board(word, position, direction)

        return score

    def check_word_fit(self, word, position, direction):
        if direction == 'across':
            x, y = position
            for i, letter in enumerate(word):
                if (x + i, y) in self.board and self.board[(x + i, y)][0] != letter:
                    return False
                if (x + i, y) not in self.board and any((x + i, j) in self.board
