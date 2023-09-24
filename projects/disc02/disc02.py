# Q5: Make Keeper (higher order function)
from operator import add, mul, mod


def make_keeper(n):
    """Returns a function that takes one parameter cond and prints
    out all integers 1..i..n where calling cond(i) returns True.

    >>> def is_even(x): # Even numbers have remainder 0 when divided by 2.
    ...     return x % 2 == 0
    >>> make_keeper(5)(is_even)
    2
    4
    >>> make_keeper(5)(lambda x: True)
    1
    2
    3
    4
    5
    >>> make_keeper(5)(lambda x: False)  # Nothing is printed
    """
    "*** YOUR CODE HERE ***"
    def keeper(cond):
        i = 0
        while i <= n:
            if cond(i):
                print(i)
            i = + 1
    return keeper


make_keeper(5)(lambda x: True)


# Q6: Currying


def curry(func):
    """
    Returns a Curried version of a two-argument function FUNC.
    >>> from operator import add, mul, mod
    >>> curried_add = curry(add)
    >>> add_three = curried_add(3)
    >>> add_three(5)
    8
    >>> curried_mul = curry(mul)
    >>> mul_5 = curried_mul(5)
    >>> mul_5(42)
    210
    >>> curry(mod)(123)(10)
    3
    """
    "*** YOUR CODE HERE ***"
    def func():
        def g(x):
            def h(y):
                return func(x, y)
        return g
    return func


curried_add = curry(add)
add_three = curried_add(3)
add_three(5)

# Q7: Make Your Own Lambdas(HOFs and Lambdas)


def f1():
    """
    >>> f1()
    3
    """
    "*** YOUR CODE HERE ***"
    return 3


def f2():
    """
    >>> f2()()
    3
    """
    "*** YOUR CODE HERE ***"
    return lambda: 3


def f3():
    """
    >>> f3()(3)
    3
    """
    "*** YOUR CODE HERE ***"
    return lambda: lambda x: x


def f4():
    """
    >>> f4()()(3)()
    3
    """
    "*** YOUR CODE HERE ***"
    return lambda: lambda x: lambda: x

# Q8: Match Maker


def match_k(k):
    """Returns a function that checks if digits k apart match.

    >>> match_k(2)(1010)
    True
    >>> match_k(2)(2010)
    False
    >>> match_k(1)(1010)
    False
    >>> match_k(1)(1)
    True
    >>> match_k(1)(2111111111111111)
    False
    >>> match_k(3)(123123)
    True
    >>> match_k(2)(123123)
    False
    """
    def match(x):
        p = k
        while x > 10 ** p:
            if x // (10 ** p) % 10 != x % 10:
                return False
            x = x // 10
        return True
    return match


match_k(2)(123123)
