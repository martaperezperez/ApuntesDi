#!/usr/bin/env python

""" Un programa sinxelo, para calcular cadrados
de números """


def potencia():
    print("Calcularanse potencia de dous números")
    n1 =  input("Ingrese un número enteiro: ")
    n2 =  input("Ingrese un número enteiro: ")

    for x in range(int(n1), int(n2)):
        print(x * x)

    print("É todo por agora")


potencia()


