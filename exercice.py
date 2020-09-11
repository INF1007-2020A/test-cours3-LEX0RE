#!/usr/bin/env python
# -*- coding: utf-8 -*-
def capitaliser_pays(nom):
    newname = ''
    for i in range(len(nom)):
        if nom[i] <= 'Z':
            value = ord(nom[i])
            value = value + 32
            newchar = chr(value)
            nom[i] = newchar

    nom = 
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
