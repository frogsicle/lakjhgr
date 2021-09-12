#!/usr/bin/env python3

"""
Baut die Funktion **snake_case** so, dass die Tests **True** ausgeben.
Macht es C-like in pure python ohne imports und ohne fancy string Methoden (Beispiel: kein lower, keine der Funktionen https://twitter.com/AbzAaron/status/1434556230014541826) (das join ist nur für die tests der Übersicht halber drin).
Da Python strings nicht by-ref übergeben kann und es mehr wie C sein soll wird mit Listen gearbeitet.
"""


# hand written C-like snake_case without fancy python methods
def is_upper(char):
    oc = ord(char)
    return 65 <= oc <= 90


def to_lower(char):
    out = chr(ord(char) + 32)
    return out


def snake_case(txt_ar):
    for i in range(len(txt_ar) - 1, -1, -1):
        char = txt_ar[i]
        if is_upper(char):
            txt_ar[i] = to_lower(char)
            # cleaning the room from floor to ceiling ;-)
            txt_ar[i:] = ['_'] + txt_ar[i:-1]


# tests
def helper_test(txt_ar, target):
    snake_case(txt_ar)
    res = ''.join(txt_ar)
    assert res == target, f'{res} != {target}'


def test_00():
    txt_ar = ['m', 'a', 'k', 'e', 'S', 'n', 'a', 'k', 'e', 'C', 'a', 's', 'e', ' ', ' ']
    target = "make_snake_case"
    helper_test(txt_ar, target)


def test_01():
    txt_ar = ['m', 'o', 'r', 'e', ' ', 'S', 'n', 'a', 'k', 'e', ' ']
    target = "more _snake"
    helper_test(txt_ar, target)


def test_02():
    txt_ar = ['B', 'l', 'e', 'r', 'g', 'h', ' ']
    target = "_blergh"
    helper_test(txt_ar, target)


def test_03():
    txt_ar = ['l', 'O', 'L', ' ', ' ']
    target = "l_o_l"
    helper_test(txt_ar, target)

