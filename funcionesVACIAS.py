from principal import *
from configuracion import *
from funcionesSeparador import *
from funcionesAuxiliares import *

import random
import math

def lectura (archivo,lista):
  lista1 = archivo.readlines ()
  for linea in lista1:
    cad = subcadena(linea,0,len(linea))
    if cad!="":
      lista.append(cad)
  archivo.close ()
  return (lista)

def nuevaSilaba(silabas):
    silaba = random.choice(silabas) #elige aleatoriamente de la lista de silabas una silaba
    return silaba

def actualizar(silabasEnPantalla,posiciones,listaDeSilabas):
    silabasEnPantalla.append(nuevaSilaba(listaDeSilabas))
    posiciones.append(damePosicion(posiciones))
    s=0
    while s<len(silabasEnPantalla):
        if posiciones[s][1]>=500:  #el valor del eje y
            silabasEnPantalla.pop(s)
            posiciones.pop(s)
        else:
            posiciones[s][1]+=8
        s=s+1

def quitar(candidata, silabasEnPantalla, posiciones):
    silabas = dameSilabas(candidata) #separando en silabas (arma una lista)
    for elem in silabas:
        cont=0
        while cont<len(silabasEnPantalla):
            if elem==silabasEnPantalla[cont]:
                silabasEnPantalla.pop(cont)
                posiciones.pop(cont)
                break
            else:
              cont=cont+1

def dameSilabas(candidata):
    palabra = separador(candidata) #devuelve una cadena con la palabra separada en silabas
    silabas=[]
    sil=""
    for l in palabra:
        if l!="-":
            sil=sil+l
        else:
            silabas.append(sil)
            sil=""
    silabas.append(sil)
    return silabas


def esValida(candidata,silabasEnPantalla, lemario):
    lista=dameSilabas(candidata) #funcion que separa en silabas las palabras
    if estaEnPantalla(lista,silabasEnPantalla)==True and aparece(candidata,lemario)==True:
            return True
    else:
        return False


def Puntos(candidata):
    suma=0
    for letra in candidata:
        if letra=="a" or letra=="e" or letra=="i" or letra=="o" or letra=="u":
            suma=suma+1
        else:
            if letra=="j" or letra=="k" or letra=="q" or letra=="w" or letra=="x" or letra=="y" or letra=="z":
                suma=suma+5
            else:
                suma=suma+2
    return suma


def procesar(candidata, silabasEnPantalla, posiciones, lemario):
    if esValida(candidata,silabasEnPantalla,lemario)==True:
        quitar(candidata,silabasEnPantalla,posiciones)
        quitarLemario (candidata,lemario)
        return Puntos(candidata)
    return 0

