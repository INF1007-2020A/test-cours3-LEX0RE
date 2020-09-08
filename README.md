[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod-redirect-0.herokuapp.com/)

# Capitalisation de noms de pays

Avant de commencer. Consulter les instructions à suivre dans [instructions.md](instructions.md)

## Objectif

Modifier les casses de noms de pays afin que:
* Les mots de liaisons (ex.: and) soient en casses minuscules
* Les premières lettres de noms soient en casses majuscules

### Exemple
```python
print(capitaliser_pays('antigua ANd barbuda'))
```
Antigua and Barbuda

### À compléter
Vous devez compléter la fonction suivante du fichier [exercice.py](exercice.py).

```python
def capitaliser_pays(nom):
    #TODO completer la fonction
    return nom
```

## Connaissances utiles

### Changement de casse
```python
chaine = "Hello, World!"
print(chaine.upper())
print(chaine.lower())
print(chaine.capitalize())
print(chaine.swapcase())
```
HELLO, WORLD!<br>
hello, world!<br>
Hello, world!<br>
hELLO, wORLD!<br>

### Remplacement de sous-chaîne (substring)
```python
print(chaine.replace('Hello', 'Bonjour'))
```
Bonjour, World!<br>

### Trouver une sous-chaîne ou un charactère
```python
# retourne le premier indice trouvé
print(chaine.find('o'))
print(chaine.find('World'))
```
4<br>
7
