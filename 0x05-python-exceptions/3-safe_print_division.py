#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        var = a / b
    except ZeroDivisionError:
        var = None
    finally:
        print("Inside result: {}".format(var))
    return var
