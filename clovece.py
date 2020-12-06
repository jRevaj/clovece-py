import random

# GLOBALNE PREMENNE
# zadanie vstupu
vstup = int(input('Zadajte rozmer hracej plochy: '))
# vytvorenie listu s n vnorenymi listami = Pocet riadkov a stlpcov
sachovnica = [[''] * (vstup + 1) for i in range(vstup + 1)]
list_hracov = []


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
    figurky = []
    hracie_pole = []
    pocet_figuriek = 0
    idx_figurka_v_hre = 0
    pozicia = 0
    posledna_hracia_pozicia = 0
    skoncil_hru = False

    def zober_dalsiu_figurku(self):
        for i in range(len(self.figurky)):
            figurka = self.figurky[i]
            if figurka.is_in_home is False:
                self.idx_figurka_v_hre = i
                return False
        return True


def gensachovnicu(n):
    # generovanie sachovnice s rozmermi n * n
    for row in range(n+1):
        if row == 0:
            for col in range(n+1):
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
                    '''if (row > 1 or row < 4) and col == 6:
                        sachovnica[row][col] = 'A'
                    point = Bod()
                    point.x = row
                    point.y = col
                    point.image = '*'
                    list_hracov[0].hracie_pole.append(point)'''
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
                    '''if (row > 1 or row < 4) and col == 6:
                        sachovnica[row][col] = 'A'
                    point = Bod()
                    point.x = row
                    point.y = col
                    point.image = '*'
                    list_hracov[0].hracie_pole.append(point)'''
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
                    '''if (row > 1 or row < 4) and col == 6:
                        sachovnica[row][col] = 'A'
                    point = Bod()
                    point.x = row
                    point.y = col
                    point.image = '*'
                    list_hracov[0].hracie_pole.append(point)'''
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
                    '''point = Bod()
                    point.x = row
                    point.y = col
                    point.image = '*'
                    list_hracov[0].hracie_pole.append(point)'''
                else:
                    sachovnica[row][col] = 'D'
                    '''list_hracov[0].pocet_figuriek += 1
                    point = Bod()
                    point.x = row
                    point.y = col
                    point.image = 'D'
                    list_hracov[0].hracie_pole.append(point)'''
    return sachovnica


def loadFigurky(idxHrac):
    for i in range(3):
        image = 'A' + str(i)
        list_hracov[idxHrac].figurky.append(Pawn(image, False))


def nastavDefaultPoziciu(pozicia):
    list_hracov[0].pozicia = pozicia
    x = list_hracov[0].hracie_pole[list_hracov[0].pozicia].x
    y = list_hracov[0].hracie_pole[list_hracov[0].pozicia].y
    idFigurky = list_hracov[0].idx_figurka_v_hre
    figurka = list_hracov[0].figurky[idFigurky]
    sachovnica[x][y] = figurka.image


def nastavPoziciu(hodKockou):
    currentPosition = list_hracov[0].pozicia
    currentPosition += hodKockou
    if currentPosition < len(list_hracov[0].hracie_pole):

        # na povodnu poziciu dame *
        x = list_hracov[0].hracie_pole[list_hracov[0].pozicia].x
        y = list_hracov[0].hracie_pole[list_hracov[0].pozicia].y
        sachovnica[x][y] = list_hracov[0].hracie_pole[list_hracov[0].pozicia].image

        # na novu dame figurku
        list_hracov[0].pozicia = currentPosition
        x = list_hracov[0].hracie_pole[list_hracov[0].pozicia].x
        y = list_hracov[0].hracie_pole[list_hracov[0].pozicia].y
        idFigurky = list_hracov[0].idx_figurka_v_hre
        figurka = list_hracov[0].figurky[idFigurky]
        sachovnica[x][y] = figurka.image

        # kontrola ci je v domceku
        if (currentPosition + 1) == len(list_hracov[0].hracie_pole):
            figurka = list_hracov[0].figurky[idFigurky]
            figurka.is_in_home = True
            list_hracov[0].skoncil_hru = list_hracov[0].zober_dalsiu_figurku()
            list_hracov[0].hracie_pole.pop()
            return True

        return False
    else:
        return False


def f_vstup(x):
    # overenie ci je rozmery neparne cislo
    if x % 2 == 0:
        raise ValueError('Cislo musi byt neparne')


def genHraciePoleA():
    loadKvadrant1A(0, 6, 6, 10)
    loadKvadrant2A(6, 10, 9, 4)
    loadKvadrant3A(9, 4, 4, 0)
    loadKvadrant4A(4, 0, 1, 6)
    loadDomcekyA(0, 5, 4, 6)
    nastavDefaultPoziciu(0)


def loadKvadrant1A(rowBeg, rowEnd, colBeg, colEnd):
    for row in range(rowBeg, rowEnd):
        for col in range(colBeg, colEnd):
            if sachovnica[row][col] == '*':
                point = Point()
                point.x = row
                point.y = col
                point.image = sachovnica[row][col]
                list_hracov[0].hracie_pole.append(point)


def loadKvadrant2A(rowBeg, rowEnd, colBeg, colEnd):
    for row in range(rowBeg, rowEnd):
        for col in range(colBeg, colEnd, -1):
            if sachovnica[row][col] == '*':
                point = Point()
                point.x = row
                point.y = col
                point.image = sachovnica[row][col]
                list_hracov[0].hracie_pole.append(point)


def loadKvadrant3A(rowBeg, rowEnd, colBeg, colEnd):
    for row in range(rowBeg, rowEnd, -1):
        for col in range(colBeg, colEnd, -1):
            if sachovnica[row][col] == '*':
                point = Point()
                point.x = row
                point.y = col
                point.image = sachovnica[row][col]
                list_hracov[0].hracie_pole.append(point)


def loadKvadrant4A(rowBeg, rowEnd, colBeg, colEnd):
    for row in range(rowBeg, rowEnd, -1):
        for col in range(colBeg, colEnd):
            if sachovnica[row][col] == '*':
                point = Point()
                point.x = row
                point.y = col
                point.image = sachovnica[row][col]
                list_hracov[0].hracie_pole.append(point)
    list_hracov[0].posledna_hracia_pozicia = len(list_hracov[0].hracie_pole) + 1


def loadDomcekyA(rowBeg, rowEnd, colBeg, colEnd):
    for row in range(rowBeg, rowEnd):
        for col in range(colBeg, colEnd):
            if sachovnica[row][col] == 'D':
                point = Point()
                point.x = row
                point.y = col
                point.image = sachovnica[row][col]
                list_hracov[0].hracie_pole.append(point)


def tlacsachovnicu(sachovnica):
    # vypisanie sachovnice
    for row in sachovnica:
        print(' ' .join([str(elem) for elem in row]))


def hodKockou():
    hodeneCislo = random.randint(1, 6)
    return hodeneCislo


def spustHru():
    for s in range(100):
        cislo = hodKockou()
        print('\nHodené číslo: ', cislo, s)
        jeVdomceku = nastavPoziciu(cislo)
        if list_hracov[0].skoncil_hru is True:
            tlacsachovnicu(sachovnica)
            print('Skoncil hru')
            break
        if jeVdomceku is True:
            # list_hracov[0].zoberDalsiuFigurku()
            nastavDefaultPoziciu(0)
        tlacsachovnicu(sachovnica)


f_vstup(vstup)
gensachovnicu(vstup)
list_hracov.append(Player())
list_hracov.append(Player())
loadFigurky(0)  # pre hraca A
genHraciePoleA()
tlacsachovnicu(sachovnica)
spustHru()
