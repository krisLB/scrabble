import random

class Scrabble:
    def __init__(self):
        self.letter_values = {'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10}
        self.tile_bag = [letter + str(self.letter_values[letter]) for letter in self.letter_values for i in range(self.letter_values[letter])]
        self.player_tiles = {}
        random.shuffle(self.tile_bag)

    def draw_tile(self, player):
        tile = self.tile_bag.pop() if self.tile_bag else None
        if tile:
            self.player_tiles[player].append(tile)
        return tile

    def exchange_tiles(self, player, tiles):
        for tile in tiles:
            if tile in self.player_tiles[player]:
                self.player_tiles[player].remove(tile)
                self.tile_bag.append(tile)
        self.draw_tiles(player, len(tiles))

    def draw_tiles(self, player, count=7):
        for i in range(count - len(self.player_tiles[player])):
            tile = self.draw_tile(player)
            if not tile:
                break

    def play_word(self, player, word):
        score = 0
        for letter in word:
            if letter.upper() in self.player_tiles[player]:
                score += self.letter_values[letter.upper()]
                self.player_tiles[player].remove(letter.upper() + str(self.letter_values[letter.upper()]))
            else:
                return None
        self.draw_tiles(player)
        return score

game = Scrabble()
players = ['Player 1', 'Player 2', 'Player 3']
for player in players:
    game.player_tiles[player] = []
    game.draw_tiles(player)

current_player = 0
while True:
    player = players[current_player]
    print(f"{player}'s turn: {game.player_tiles[player]}")
    user_input = input("Enter a word to play or exchange tiles (or type 'QUIT' to end the game): ").strip().upper()
    if user_input == "QUIT":
        break
    if user_input.startswith("EXCHANGE"):
        tiles = user_input.split()[1:]
        game.exchange_tiles(player, tiles)
    else:
        score = game.play_word(player, user_input)
        if score:
            print
