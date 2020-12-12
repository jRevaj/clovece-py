import random


# Classes
class Point:
    """Constructing one point in game board."""
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image


class Pawn:
    """Constructing pawns for each player."""
    def __init__(self, image, is_in_home):
        self.image = image
        self.is_in_home = is_in_home


class Player:
    """Constructing one player."""
    def __init__(self):
        self.pawns = []
        self.board = []
        self.number_of_pawns = 0
        self.idx_pawn_in_game = 0
        self.position = 0
        self.last_position = 0
        self.finished = False

    def take_another_pawn(self):
        """Take next pawn if previous is in home."""
        for i in range(len(self.pawns)):
            pawn = self.pawns[i]
            if pawn.is_in_home is False:
                self.idx_pawn_in_game = i
                return False
        return True

    def add_point_to_board(self, row, col, image):
        """Add point to players gaming board."""
        if sachovnica[row][col] == image:
            self.board.append(Point(row, col, sachovnica[row][col]))

    def place_pawn(self):
        """Place pawn on new position."""
        x = self.board[self.position].x
        y = self.board[self.position].y
        pawn_id = self.idx_pawn_in_game
        pawn = self.pawns[pawn_id]
        sachovnica[x][y] = pawn.image


def check_input():
    """Checks input if it is not even and greater than 5."""
    err_mes = 'Invalid input! Input must not be even and must be greater than 5.'
    while True:
        board_size = int(input('Enter board size: '))
        if not input:
            print(err_mes)
        elif board_size % 2 == 0 or board_size <= 5:
            print(err_mes)
        else:
            break
    return board_size


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


def initialize_players():
    """Initialize pawns for each player and """
    for idx_player in range(len(player_list)):
        load_pawns(board_size_input, idx_player)
        gen_playing_field(board_size_input, idx_player)


def load_pawns(n, idx_player):
    """Loads pawns for one player."""
    num_of_pawns = int((n - 3) / 2)
    if idx_player == 0:
        for i in range(num_of_pawns):
            image = 'A'
            player_list[idx_player].pawns.append(Pawn(image, False))
    elif idx_player == 1:
        for i in range(num_of_pawns):
            image = 'B'
            player_list[idx_player].pawns.append(Pawn(image, False))


# Loading quadrants of player paths.
def load_quadrant_1(row_beg, row_end, col_beg, col_end, idx_player):
    for row in range(row_beg, row_end):
        for col in range(col_beg, col_end):
            player_list[idx_player].add_point_to_board(row, col, '*')


def load_quadrant_2(row_beg, row_end, col_beg, col_end, idx_player):
    for row in range(row_beg, row_end):
        for col in range(col_beg, col_end, -1):
            player_list[idx_player].add_point_to_board(row, col, '*')
    player_list[idx_player].last_position = len(player_list[idx_player].board) + 1


def load_quadrant_3(row_beg, row_end, col_beg, col_end, idx_player):
    for row in range(row_beg, row_end, -1):
        for col in range(col_beg, col_end, -1):
            player_list[idx_player].add_point_to_board(row, col, '*')


def load_quadrant_4(row_beg, row_end, col_beg, col_end, idx_player):
    for row in range(row_beg, row_end, -1):
        for col in range(col_beg, col_end):
            player_list[idx_player].add_point_to_board(row, col, '*')
    player_list[idx_player].last_position = len(player_list[idx_player].board) + 1


# Loading homes for players pawns.
def load_homes(row_beg, row_end, col_beg, col_end, idx_player):
    if idx_player == 0:
        for row in range(row_beg, row_end):
            for col in range(col_beg, col_end):
                player_list[idx_player].add_point_to_board(row, col, 'D')
    elif idx_player == 1:
        for row in range(row_beg, row_end, -1):
            for col in range(col_beg, col_end):
                player_list[idx_player].add_point_to_board(row, col, 'D')


# Generating playing fields for each player.
def gen_playing_field(board_size, idx_player):
    """Counting right margins for board size.
    Loading quadrants for each player.
    Commented ref values are for board_size 9."""
    r_start = int(((board_size + 1) / 2) + 1)  # 6
    r_end = int(((board_size + 1) / 2) - 1)  # 4
    max = int(board_size + 1)  # 10
    c_start = int(board_size)  # 9
    c_end = int((board_size + 1) / 2)  # 5
    if idx_player == 0:
        load_quadrant_1(0, r_start, r_start, max, idx_player)
        load_quadrant_2(r_start, max, c_start, r_end, idx_player)
        load_quadrant_3(c_start, r_end, r_end, 0, idx_player)
        load_quadrant_4(r_end, 0, 1, r_start, idx_player)
        load_homes(0, c_end, r_end, r_start, idx_player)
        set_default_position(0, idx_player)
    elif idx_player == 1:
        load_quadrant_3(c_start, r_end, r_end, 0, idx_player)
        load_quadrant_4(r_end, 0, 1, r_start, idx_player)
        load_quadrant_1(0, r_start, r_start, max, idx_player)
        load_quadrant_2(r_start, max, c_start, r_end, idx_player)
        load_homes(c_start, c_end, r_end, r_start, idx_player)
        set_default_position(0, idx_player)


def set_default_position(position, idx_player):
    """Set starting position for every pawn."""
    player_list[idx_player].position = position
    player_list[idx_player].place_pawn()


def set_position(roll_dice, idx_player):
    """Set new position by adding rolled number to current position.
    Return if pawn is in home or not."""
    current_position = player_list[idx_player].position
    current_position += roll_dice
    if current_position < len(player_list[idx_player].board):

        # Set previous image on field from which is pawn moving.
        x = player_list[idx_player].board[player_list[idx_player].position].x
        y = player_list[idx_player].board[player_list[idx_player].position].y
        sachovnica[x][y] = player_list[idx_player].board[player_list[idx_player].position].image

        # Place pawn on new position.
        player_list[idx_player].position = current_position
        player_list[idx_player].place_pawn()

        # Checks if pawn is in home.
        # Incrementing current_position to match length of board
        if (current_position + 1) == len(player_list[idx_player].board):
            pawn = player_list[idx_player].pawns[player_list[idx_player].idx_pawn_in_game]
            pawn.is_in_home = True
            player_list[idx_player].finished = player_list[idx_player].take_another_pawn()  # Taking out another pawn
            player_list[idx_player].board.pop()     # Removing last element from board because it's occupied by our pawn
            return True
        return False
    else:
        return False


def tlacsachovnicu(sachovnica):
    """Prints out our board and state of game."""
    for row in sachovnica:
        print(' ' .join([str(elem) for elem in row]))


def run_game(counter=0, idx_player=random.randint(0, 1)):
    """Starts our game loop.
    Switch between two players.
    """
    gensachovnicu(board_size_input)
    initialize_players()
    tlacsachovnicu(sachovnica)  # Printing our board with initial positions.
    while True:
        counter += 1        # Counting number of moves.
        print('\nPlayer', idx_player + 1, 'turn.')
        print('Move no.:', counter)
        num = random.randint(1, 6)
        print('Rolled number:', num)
        is_in_home = set_position(num, idx_player)
        if player_list[idx_player].finished is True:
            tlacsachovnicu(sachovnica)
            print('Player', idx_player + 1, 'won.')
            break
        if is_in_home is True:
            set_default_position(0, idx_player)
            set_default_position(0, idx_player)
        tlacsachovnicu(sachovnica)
        if num == 6:
            continue
        elif idx_player < 1:
            idx_player += 1
        else:
            idx_player = 0


# Initialization of main elements.
board_size_input = check_input()
sachovnica = [[''] * (board_size_input + 1) for i in range(board_size_input + 1)]
player_list = [Player() for player_number in range(2)]
run_game()
