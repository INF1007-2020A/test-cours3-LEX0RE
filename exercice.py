#!/usr/bin/env python
# -*- coding: utf-8 -*-
def capitaliser_pays(nom):
    print(len(nom))
    for i in range(11):
        if nom[i] <= 'Z':
            nom = nom[i-1:i+1] + chr(ord(nom[i]) + 32) + nom[i+1:]
            #nom[i:i+1] =  + chr(ord(nom[i]) + 32)

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
