import math
import turtle

bob = turtle.Turtle()


def arc(t, radius, angle):
    arc_length = 2 * math.pi * radius * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n
    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)


def list_kvetu(t, radius_listu, uhol_listu):
    for i in range(2):
        arc(t, radius_listu, uhol_listu)
        t.lt(180-uhol_listu)


def kvet(t, pocet_kvetov, radius_listu, uhol_listu):
    for i in range(pocet_kvetov):
        list_kvetu(t, radius_listu, uhol_listu)
        t.lt(360.0 / pocet_kvetov)


def presun(t, dlzka, smer):
    t.pu()
    t.home()
    t.setheading(smer)
    t.fd(dlzka)
    t.pd()
    t.setheading(0)


def stonka(t, dlzka_stonky, uhol_stonky):
    t.setheading(270 - uhol_stonky + 1)
    arc(t, dlzka_stonky / 2, uhol_stonky * 2)


def list_stonky(t, pocet_listov, uhol_od_zeme, dlzka_listu, hrubka):
    t.setheading(0)
    t.left(uhol_od_zeme)
    for i in range(pocet_listov):
        list_kvetu(t, dlzka_listu, hrubka)
        t.setheading(180 - (uhol_od_zeme + hrubka) + 1)


bob.speed(30)

presun(bob, 200, 180)

kvet(bob, 7, 60.0, 60.0)
stonka(bob, 250, 40)
list_stonky(bob, 2, 5, 80, 60)

presun(bob, 0, 0)

kvet(bob, 10, 40.0, 80.0)
stonka(bob, 600, 25)
list_stonky(bob, 2, 60, 300, 20)

presun(bob, 200, 0)

kvet(bob, 20, 140.0, 20.0)
stonka(bob, 650, 15)
list_stonky(bob, 2, 10, 100, 80)

turtle.mainloop()

