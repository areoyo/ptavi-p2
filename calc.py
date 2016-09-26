#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys


def plus(op1, op2):
    """ Function to sum the operands """
    return op1 + op2


def minus(op1, op2):
    """ Function to substract the operands """
    return op1 - op2


def div(op1, op2):
    try:
        return op1 / op2
    except ZeroDivisionError:
        sys.exit("Error: Division by zero is not allowed")


def mult(op1, op2):
    return op1 * op2


if __name__ == "__main__":
    try:
        operando1 = int(sys.argv[1])
        operando2 = int(sys.argv[3])
    except ValueError:
        sys.exit("Error: Non numerical parameters")

    operador = sys.argv[2]
    operadorDict = {'suma': plus, 'resta': minus, 'multiplica': mult,   \
        'divide': div}

    result = operadorDict[operador](operando1, operando2)
    print(result)
