def gcd(x, y):
    def euclids_algo(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)

    a, b = max(x, y), min(x, y)
    return euclids_algo(a, b)


if __name__ == '__main__':
    assert gcd(206, 40) == 2
    assert gcd(40, 206) == 2
