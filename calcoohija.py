#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoo
                
class CalculadoraHija (calcoo.Calculadora):
    def div (self, op1, op2):
        try:
            return op1 / op2
        except ZeroDivisionError:
            sys.exit("Error: Division by zero is not allowed")
    
    def mult (self, op1, op2):
        return op1 * op2

if __name__ == "__main__":

    calculadora = CalculadoraHija()
    operadorDict = {'suma': calculadora.plus, 'resta': calculadora.minus,
     'multiplica': calculadora.mult, 'divide': calculadora.div}
    
    try:
        operando1 = int(sys.argv[1])
        operando2 = int(sys.argv[3])
    except ValueError:
        sys.exit("Error: Non numerical parameters")
        
    operador = sys.argv[2]     
    result = operadorDict[operador](operando1, operando2)
    print(result)
