def fib(n):
    def fib_iter(a, b, count):
        if count == 0:
            return b

        return fib_iter(a + b, a, count - 1)

    return fib_iter(1, 0, n)


if __name__ == '__main__':
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(3) == 2
    assert fib(4) == 3
    assert fib(5) == 5
    assert fib(6) == 8
    assert fib(7) == 13
    assert fib(8) == 21
