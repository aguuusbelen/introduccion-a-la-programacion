from funcionesSeparador import *
import pygame
from pygame.locals import *
from configuracion import *
import random

def subcadena (cadena,inicio,fin):
  subcad=""
  for letra in range (inicio,fin-1):
    subcad+=cadena[letra]
  return subcad

def damePosicion (posiciones):
    posicionX = random.randint(0,741)
    posicionY = -15
    posicion = [posicionX,posicionY]
    while not posicionValida(posicion, posiciones):
        posicion = [random.randint(0,741), -15]
    return posicion

def posicionValida(posicion, posiciones):
    i=0
    while i<len(posiciones):
        if posiciones[i][1] <= 0 and (posiciones[i][0] - posicion[0] < 50 and posiciones[i][0] - posicion[0] > -50):
            return False
        i=i+1
    return True


def aparece (cadena,lista):
    for p in range (len(lista)):
        if lista[p]==cadena:
            return True
    return False

def estaEnPantalla (lista,SilabasPantalla):
    for s in lista:
        if aparece(s,SilabasPantalla)==False:
            return False
    return True

def quitarLemario(candidata, lemario):
    cont=0
    while cont<len (lemario):
        if lemario[cont] == candidata:
            lemario.pop(cont)
            return lemario

        cont=cont+1


listaColor = [(255,255,0),(0,255,0),(65,105,255),(255,99,71),(205,105,180),(127,255,212),(238,130,238)]

def cambiarColor():
    color = random.randint (0,len(listaColor)-1)
    return (listaColor[color])

