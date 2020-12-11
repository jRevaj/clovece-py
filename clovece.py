import random

# Global variables
# Prompt user to input board size.
board_size_input = int(input('Enter board size: '))
# Initialization of main elements.
sachovnica = [[''] * (board_size_input + 1) for i in range(board_size_input + 1)]
player_list = []


# Classes
class Point:
    """Class for one point in game board."""
    x = 0
    y = 0
    image = ''


class Pawn:
    """Constructing pawns for each player."""
    image = ''
    is_in_home = False

    def __init__(self, image, is_in_home):
        self.image = image
        self.is_in_home = is_in_home


class Player:
    """One player."""
    pawns = []
    board = []
    number_of_pawns = 0
    idx_pawn_in_game = 0
    position = 0
    last_position = 0
    finished = False

    def take_another_pawn(self):
        """Take next pawn if previous is in home."""
        for i in range(len(self.pawns)):
            pawn = self.pawns[i]
            if pawn.is_in_home is False:
                self.idx_pawn_in_game = i
                return False
        return True


def check_input(x):
    """Checks input if it is not even."""
    if x % 2 == 0:
        raise ValueError('Input must not be even.')
    elif x <= 5:
        raise ValueError('Input must be greater than 5.')


def gensachovnicu(n):
    """Generates our game board of size n * n.

    n is board_size_input that user inputs.

    Returning our board in 2D list.
    """
    for row in range(n + 1):
        if row == 0:
            for col in range(n + 1):
                if col == 0:
                    sachovnica[0][0] = ' '
                else:
                    if col > 10:
                        sachovnica[0][col] = col - 11
                    else:
                        sachovnica[0][col] = col - 1

        elif row == 1 or row == n:
            for col in range(n+1):
                if col == 0:
                    if row > 10:
                        sachovnica[row][0] = row - 11
                    else:
                        sachovnica[row][0] = row - 1
                elif col == (n + 1) / 2 or col == ((n + 1) / 2) - 1 or col == ((n + 1) / 2) + 1:
                    sachovnica[row][col] = '*'
                else:
                    sachovnica[row][col] = ' '

        elif row < ((n + 1) / 2) - 1 or row > ((n + 1) / 2) + 1:
            for col in range(n + 1):
                if col == 0:
                    if row > 10:
                        sachovnica[row][0] = row - 11
                    else:
                        sachovnica[row][0] = row - 1
                elif col == (n + 1) / 2:
                    sachovnica[row][col] = 'D'
                elif col == ((n + 1) / 2) - 1 or col == ((n + 1) / 2) + 1:
                    sachovnica[row][col] = '*'
                else:
                    sachovnica[row][col] = ' '
        elif row == ((n + 1) / 2) - 1 or row == ((n + 1) / 2) + 1:
            for col in range(n + 1):
                if col == 0:
                    if row > 10:
                        sachovnica[row][0] = row - 11
                    else:
                        sachovnica[row][0] = row - 1
                elif col == (n + 1) / 2:
                    sachovnica[row][col] = 'D'
                else:
                    sachovnica[row][col] = '*'
        else:
            for col in range(n + 1):
                if col == 0:
                    if row > 10:
                        sachovnica[row][0] = row - 11
                    else:
                        sachovnica[row][0] = row - 1
                elif col == (n + 1) / 2:
                    sachovnica[row][col] = 'X'      # Center of our board.
                elif col == 1 or col == n:
                    sachovnica[row][col] = '*'
                else:
                    sachovnica[row][col] = 'D'
    return sachovnica


def load_pawns(idx_player, n):
    """Loads pawns for one player."""
    num_of_pawns = int((n - 3) / 2)
    for i in range(num_of_pawns):
        image = 'A' + str(i)
        player_list[idx_player].pawns.append(Pawn(image, False))


# Loading quadrants of player paths.
def load_quadrant_1(row_beg, row_end, col_beg, col_end, idx_player):
    for row in range(row_beg, row_end):
        for col in range(col_beg, col_end):
            if sachovnica[row][col] == '*':
                point = Point()
                point.x = row
                point.y = col
                point.image = sachovnica[row][col]
                player_list[0].board.append(point)


def load_quadrant_2(row_beg, row_end, col_beg, col_end, idx_player):
    for row in range(row_beg, row_end):
        for col in range(col_beg, col_end, -1):
            if sachovnica[row][col] == '*':
                point = Point()
                point.x = row
                point.y = col
                point.image = sachovnica[row][col]
                player_list[idx_player].board.append(point)
    player_list[idx_player].last_position = len(player_list[idx_player].board) + 1


def load_quadrant_3(row_beg, row_end, col_beg, col_end, idx_player):
    for row in range(row_beg, row_end, -1):
        for col in range(col_beg, col_end, -1):
            if sachovnica[row][col] == '*':
                point = Point()
                point.x = row
                point.y = col
                point.image = sachovnica[row][col]
                player_list[idx_player].board.append(point)


def load_quadrant_4(row_beg, row_end, col_beg, col_end, idx_player):
    for row in range(row_beg, row_end, -1):
        for col in range(col_beg, col_end):
            if sachovnica[row][col] == '*':
                point = Point()
                point.x = row
                point.y = col
                point.image = sachovnica[row][col]
                player_list[idx_player].board.append(point)
    player_list[idx_player].last_position = len(player_list[idx_player].board) + 1


# Loading homes for players pawns.
def load_homes(row_beg, row_end, col_beg, col_end, idx_player):
    if idx_player == 0:
        for row in range(row_beg, row_end):
            for col in range(col_beg, col_end):
                if sachovnica[row][col] == 'D':
                    point = Point()
                    point.x = row
                    point.y = col
                    point.image = sachovnica[row][col]
                    player_list[idx_player].board.append(point)
    elif idx_player == 1:
        for row in range(row_beg, row_end):
            for col in range(col_beg, col_end):
                if sachovnica[row][col] == 'D':
                    point = Point()
                    point.x = row
                    point.y = col
                    point.image = sachovnica[row][col]
                    player_list[idx_player].board.append(point)


# Generating playing fields for each player.
def gen_playing_field(board_size, idx_player):
    """Counting right margins for board size.
    Loading quadrants for player 1."""
    r_start = int(((board_size + 1) / 2) + 1)  # 6
    r_end = int(((board_size + 1) / 2) - 1)  # 4
    r_max = int(board_size + 1)  # 10
    c_start = int(board_size)  # 9
    c_end = int((board_size + 1) / 2)  # 5
    if idx_player == 0:
        load_quadrant_1(0, r_start, r_start, r_max, idx_player)
        load_quadrant_2(r_start, r_max, c_start, r_end, idx_player)
        load_quadrant_3(c_start, r_end, r_end, 0, idx_player)
        load_quadrant_4(r_end, 0, 1, r_start, idx_player)
        load_homes(0, c_end, r_end, r_start, idx_player)
        set_default_position(0)
    elif idx_player == 1:
        load_quadrant_3(c_start, r_end, r_end, 0, idx_player)
        load_quadrant_4(r_end, 0, 1, r_start, idx_player)
        load_quadrant_1(0, r_start, r_start, r_max, idx_player)
        load_quadrant_2(r_start, r_max, c_start, r_end, idx_player)
        load_homes(r_max, r_end, r_end, r_start, idx_player)
        set_default_position(0)



def set_default_position(position):
    """Set starting position for every pawn."""
    player_list[0].position = position
    x = player_list[0].board[player_list[0].position].x
    y = player_list[0].board[player_list[0].position].y
    pawn_id = player_list[0].idx_pawn_in_game
    pawn = player_list[0].pawns[pawn_id]
    sachovnica[x][y] = pawn.image


def set_position(roll_dice):
    """Set new position by adding rolled number to current position."""
    current_position = player_list[0].position
    current_position += roll_dice
    if current_position < len(player_list[0].board):

        # Set previous image on field from which is pawn moving.
        x = player_list[0].board[player_list[0].position].x
        y = player_list[0].board[player_list[0].position].y
        sachovnica[x][y] = player_list[0].board[player_list[0].position].image

        # Place pawn on new position.
        player_list[0].position = current_position
        x = player_list[0].board[player_list[0].position].x
        y = player_list[0].board[player_list[0].position].y
        pawn_id = player_list[0].idx_pawn_in_game
        pawn = player_list[0].pawns[pawn_id]
        sachovnica[x][y] = pawn.image

        # Checks if pawn is in home.
        # Incrementing current_position to match length of board
        if (current_position + 1) == len(player_list[0].board):
            pawn = player_list[0].pawns[pawn_id]
            pawn.is_in_home = True
            player_list[0].finished = player_list[0].take_another_pawn()        # Taking out another pawn
            player_list[0].board.pop()      # Removing last element from board because it's occupied by our pawn
            return True
        return False
    else:
        return False


def tlacsachovnicu(sachovnica):
    """Prints out our board and state of game."""
    for row in sachovnica:
        print(' ' .join([str(elem) for elem in row]))


def roll_dice():
    """Generates random integer from 1 to 6 as our rolled number."""
    rolled_number = random.randint(1, 6)
    return rolled_number


def run_game(counter=0):
    """Starts our game loop."""
    while True:
        counter += 1        # Counting number of moves.
        print('\nMove no.:', counter)
        num = roll_dice()
        print('Rolled number:', num)
        is_in_home = set_position(num)
        if player_list[0].finished is True:
            tlacsachovnicu(sachovnica)
            print('Player finished.')
            break
        if is_in_home is True:
            set_default_position(0)
        tlacsachovnicu(sachovnica)


check_input(board_size_input)
gensachovnicu(board_size_input)
# Adding players
player_list.append(Player())
player_list.append(Player())
load_pawns(0, board_size_input)     # For Player(0) - A.
gen_playing_field(board_size_input, 0)      # For Player(0)
tlacsachovnicu(sachovnica)      # Printing our board with initial positions
run_game()
