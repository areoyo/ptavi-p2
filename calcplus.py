#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoohija

fich = open('/tmp/git/datos', 'r')

lineas = fich.readlines()

if __name__ == "__main__":

    calculadora = calcoohija.CalculadoraHija()
    
    for line in lineas[:-1]:
        elementos = line[:-1].split(',') #LISTA: TROCEA POR EL CARACTER QUE LE INDICAMOS
        print (elementos[0])
        
        operando1 = int(elementos[1])
        operando2 = int(elementos[2])
        if elementos[0] == "suma":               
            resultado = calculadora.plus(operando1, operando2)
            for numero in elementos [3:]:
                resultado = calculadora.plus(resultado, int(numero))
        elif elementos[0] == "resta":               
            resultado = calculadora.minus(operando1, operando2)
            for numero in elementos [3:]:
                resultado = calculadora.minus(resultado, int(numero))

        elif elementos[0] == "multiplica":               
            resultado = calculadora.mult(operando1, operando2)
            for numero in elementos [3:]:
                resultado = calculadora.mult(resultado, int(numero))

        elif elementos[0] == "divide":               
            resultado = calculadora.div(operando1, operando2)
            for numero in elementos [3:]:
                resultado = calculadora.div(resultado, int(numero))
        else:
            sys.exit('Operación sólo puede ser sumar, restar, multiplicar  o dividir.')

        print (resultado)
