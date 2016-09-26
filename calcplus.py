#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoohija

fich = open(sys.argv[1], 'r')
lineas = fich.readlines()

if __name__ == "__main__":

    calculadora = calcoohija.CalculadoraHija()
    operadorDict = {'suma': calculadora.plus, 'resta': calculadora.minus,
    'multiplica': calculadora.mult, 'divide': calculadora.div}

    for line in lineas:
        elementos = line[:-1].split(',')

        operando1 = int(elementos[1])
        operando2 = int(elementos[2])
        result = operadorDict[elementos[0]](operando1, operando2)

        for numero in elementos[3:]:
            result = operadorDict[elementos[0]](result, int(numero))

        print(result)
