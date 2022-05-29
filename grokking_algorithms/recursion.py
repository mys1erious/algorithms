def factorial(x: int) -> int:
    if not isinstance(x, int):
        raise TypeError("x has to be an integer value")
    if x < 0:
        raise ValueError("You cant calculate a factorial of the negative value")
    if x in (0, 1):
        return 1

    return x * factorial(x-1)


print(factorial(5))
