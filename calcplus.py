#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoohija

fich = open(sys.argv[1], 'r')

lineas = fich.readlines()

if __name__ == "__main__":

    calculadora = calcoohija.CalculadoraHija()
    
    for line in lineas:
        elementos = line[:-1].split(',') #LISTA: TROCEA POR EL CARACTER QUE LE INDICAMOS
        
        operador = elementos[0]
        operadorDict = {'suma': calculadora.plus, 'resta': calculadora.minus,
         'multiplica': calculadora.mult, 'divide': calculadora.div}
     
        operando1 = int(elementos[1])
        operando2 = int(elementos[2])
        result = operadorDict[operador](operando1, operando2)
        
        for numero in elementos [3:]:
            result = operadorDict[operador](result, int(numero))

        print (result)
