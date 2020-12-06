import random

# GLOBALNE PREMENNE
# zadanie vstupu
board_size_input = int(input('Zadajte rozmer hracej plochy: '))
# vytvorenie listu s n vnorenymi listami = Pocet riadkov a stlpcov
sachovnica = [[''] * (board_size_input + 1) for i in range(board_size_input + 1)]
player_list = []


# triedy
class Point:
    x = 0
    y = 0
    image = ''


class Pawn:
    image = ''
    is_in_home = False

    def __init__(self, image, is_in_home):
        self.image = image
        self.is_in_home = is_in_home


class Player:
    pawns = []
    board = []
    number_of_pawns = 0
    idx_pawn_in_game = 0
    position = 0
    last_position = 0
    finished = False

    def take_another_pawn(self):
        for i in range(len(self.pawns)):
            pawn = self.pawns[i]
            if pawn.is_in_home is False:
                self.idx_pawn_in_game = i
                return False
        return True


def gensachovnicu(n):
    # generovanie sachovnice s rozmermi n * n
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
                    sachovnica[row][col] = 'X'
                elif col == 1 or col == n:
                    sachovnica[row][col] = '*'
                else:
                    sachovnica[row][col] = 'D'
    return sachovnica


def load_pawns(idx_player):
    for i in range(3):
        image = 'A' + str(i)
        player_list[idx_player].pawns.append(Pawn(image, False))


def set_default_position(position):
    player_list[0].position = position
    x = player_list[0].board[player_list[0].position].x
    y = player_list[0].board[player_list[0].position].y
    pawn_id = player_list[0].idx_pawn_in_game
    pawn = player_list[0].pawns[pawn_id]
    sachovnica[x][y] = pawn.image


def set_position(roll_dice):
    current_position = player_list[0].position
    current_position += roll_dice
    if current_position < len(player_list[0].board):
        # na povodnu poziciu dame *
        x = player_list[0].board[player_list[0].position].x
        y = player_list[0].board[player_list[0].position].y
        sachovnica[x][y] = player_list[0].board[player_list[0].position].image

        # na novu dame figurku
        player_list[0].position = current_position
        x = player_list[0].board[player_list[0].position].x
        y = player_list[0].board[player_list[0].position].y
        pawn_id = player_list[0].idx_pawn_in_game
        pawn = player_list[0].pawns[pawn_id]
        sachovnica[x][y] = pawn.image

        # kontrola ci je v domceku
        if (current_position + 1) == len(player_list[0].board):
            pawn = player_list[0].pawns[pawn_id]
            pawn.is_in_home = True
            player_list[0].finished = player_list[0].take_another_pawn()
            player_list[0].board.pop()
            return True
        return False
    else:
        return False


def check_input(x):
    # overenie ci je rozmery neparne cislo
    if x % 2 == 0:
        raise ValueError('Cislo musi byt neparne')


def gen_playing_field_a():
    load_quadrant_1_a(0, 6, 6, 10)
    load_quadrant_2_a(6, 10, 9, 4)
    load_quadrant_3_a(9, 4, 4, 0)
    load_quadrant_4_a(4, 0, 1, 6)
    load_homes_a(0, 5, 4, 6)
    set_default_position(0)


def load_quadrant_1_a(row_beg, row_end, col_beg, col_end):
    for row in range(row_beg, row_end):
        for col in range(col_beg, col_end):
            if sachovnica[row][col] == '*':
                point = Point()
                point.x = row
                point.y = col
                point.image = sachovnica[row][col]
                player_list[0].board.append(point)


def load_quadrant_2_a(row_beg, row_end, col_beg, col_end):
    for row in range(row_beg, row_end):
        for col in range(col_beg, col_end, -1):
            if sachovnica[row][col] == '*':
                point = Point()
                point.x = row
                point.y = col
                point.image = sachovnica[row][col]
                player_list[0].board.append(point)


def load_quadrant_3_a(row_beg, row_end, col_beg, col_end):
    for row in range(row_beg, row_end, -1):
        for col in range(col_beg, col_end, -1):
            if sachovnica[row][col] == '*':
                point = Point()
                point.x = row
                point.y = col
                point.image = sachovnica[row][col]
                player_list[0].board.append(point)


def load_quadrant_4_a(row_beg, row_end, col_beg, col_end):
    for row in range(row_beg, row_end, -1):
        for col in range(col_beg, col_end):
            if sachovnica[row][col] == '*':
                point = Point()
                point.x = row
                point.y = col
                point.image = sachovnica[row][col]
                player_list[0].board.append(point)
    player_list[0].last_position = len(player_list[0].board) + 1


def load_homes_a(row_beg, row_end, col_beg, col_end):
    for row in range(row_beg, row_end):
        for col in range(col_beg, col_end):
            if sachovnica[row][col] == 'D':
                point = Point()
                point.x = row
                point.y = col
                point.image = sachovnica[row][col]
                player_list[0].board.append(point)


def tlacsachovnicu(sachovnica):
    # vypisanie sachovnice
    for row in sachovnica:
        print(' ' .join([str(elem) for elem in row]))


def roll_dice():
    rolled_number = random.randint(1, 6)
    return rolled_number


def run_game(counter=0):
    while True:
        counter += 1
        print('\nŤah:', counter)
        num = roll_dice()
        print('Hodené číslo:', num)
        is_in_home = set_position(num)
        if player_list[0].finished is True:
            tlacsachovnicu(sachovnica)
            print('Skoncil hru')
            break
        if is_in_home is True:
            # list_hracov[0].zoberDalsiuFigurku()
            set_default_position(0)
        tlacsachovnicu(sachovnica)


check_input(board_size_input)
gensachovnicu(board_size_input)
player_list.append(Player())
player_list.append(Player())
load_pawns(0)  # pre hraca A
gen_playing_field_a()
tlacsachovnicu(sachovnica)
run_game()
