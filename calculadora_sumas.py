#!/usr/bin/env python3
"""Calculadora de sumas muy sencilla."""


def sumar(a, b):
    return a + b


def main():
    a = float(input("Introduce el primer número: "))
    b = float(input("Introduce el segundo número: "))
    print(f"El resultado es: {sumar(a, b)}")


if __name__ == "__main__":
    main()
