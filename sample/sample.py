class ArgException(ArithmeticError):
    pass


def multiplier(*args):
    if any([type(n) != int for n in args]):
        raise ArgException('multiplier() only accepts integer arguments')
    x = 1
    for n in args:
        x = x * n
    return x


def adder(*args):
    if any([type(n) != int for n in args]):
        raise ArgException('adder() only accepts interger arguments')
    x = 0
    for n in args:
        x = x + n
    return x


def concatenator(*args):
    x = ''
    for e in args:
        x += '{}'.format(e)

    return x
