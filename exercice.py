#!/usr/bin/env python
# -*- coding: utf-8 -*-
def capitaliser_pays(nom):
    for i in range(0, len(nom)):
        if nom[i] <= 'Z' and nom[i] >= 'A':
            nom = nom[0:i] + chr(ord(nom[i]) + 32) + nom[i+1:]
        if i == 0
                nom = nom[0:i] + chr(ord(nom[i]) - 32) + nom[i+1:]
        if nom[i-1] == ' ' and nom.find(' and ') + 1 != i:
                nom = nom[0:i] + chr(ord(nom[i]) - 32) + nom[i+1:]

    return nom


if __name__ == '__main__':
    pays = [
        'AfghanIstan',
        'albania',
        'algeria',
        'AndorRa',
        'angolA',
        'antigua ANd barbuda',
        'argEntina',
        'Armenia',
        'austrAlia',
        'ausTria',
        'azerBaijaN'
    ]
    for i in range(len(pays)):
        pays[i] = capitaliser_pays(pays[i])

    print(pays)
