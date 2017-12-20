import random


def is_prime(n):
    return n == get_smallest_divisor(n)


def get_smallest_divisor(x):
    return find_divisor(x, 2)


def find_divisor(x, test_divisor):
    if test_divisor * test_divisor > x:
        return x
    if x % test_divisor == 0:
        return test_divisor
    return find_divisor(x, test_divisor + 1)


def is_prime_fermat(n, times):
    if times == 0:
        return True

    if fermat_test(n):
        return is_prime_fermat(n, times - 1)

    return False


def fermat_test(n):
    def try_it(a):
        return a == a ** n % n

    return try_it(random.randint(1, n - 1))


if __name__ == '__main__':
    assert is_prime(2) is True
    assert is_prime_fermat(2, 3) is True

    assert is_prime(3) is True
    assert is_prime_fermat(3, 5) is True

    assert is_prime(4) is False
    assert is_prime_fermat(4, 6) is False

    assert is_prime(5) is True
    assert is_prime_fermat(5, 7) is True

    assert is_prime(6) is False
    assert is_prime_fermat(6, 8) is False

    assert is_prime(7) is True
    assert is_prime_fermat(7, 9) is True

    assert is_prime(17) is True
    assert is_prime_fermat(17, 22) is True

    assert is_prime(27) is False
    assert is_prime_fermat(27, 34) is False

    # Carmichael number that fools Fermat test
    assert is_prime(561) is False
    assert is_prime_fermat(561, 748) is True
