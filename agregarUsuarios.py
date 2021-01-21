#!/usr/bin/python

import sys
import os
from subprocess import call

print('Hola, vamos a agregar los usuarios de Jitsi mediante del archivo', sys.argv[1])
print('Agregando lista de usuarios ...')
archivo = open(sys.argv[1])
dominio = input('Ingresa el nombre de donminio:\n')
for linea in archivo:
    usr = linea.split()
    str = ("sudo prosodyctl register "+usr[0]+" "+dominio+" "+usr[1])
    os.system(str)
    print ("Usuario: ",usr[0],'agregado con exito')

exit(0)
