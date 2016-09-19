#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import csv
import calcoohija

if __name__ == "__main__":

    calculadora = calcoohija.CalculadoraHija()
    operadorDict = {'suma': calculadora.plus, 'resta': calculadora.minus,
             'multiplica': calculadora.mult, 'divide': calculadora.div}
    
    with open(sys.argv[1], newline='') as f:
        lineas = csv.reader(f)        
        for elemento in lineas:
        
            operando1 = int(elemento[1])
            operando2 = int(elemento[2])
            result = operadorDict[elemento[0]](operando1, operando2)
            
            for numero in elemento[3:]:
                result = operadorDict[elemento[0]](result, int(numero))

            print (result)
