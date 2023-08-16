#!/usr/bin/python3

if __name__ == "__main__":
    """Print the sum, difference, product, quotient of 10 and 5."""
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5

    result-add = add(a, b)
    result-sub = sub(a, b)
    result-mul = mul(a, b)
    result-div = div(a, b)

    print("{} + {} = {}".format(a, b, result-add))
    print("{} - {} = {}".format(a, b, result-sub))
    print("{} * {} = {}".format(a, b, result-mul))
    print("{} / {} = {}".format(a, b, result-div))
