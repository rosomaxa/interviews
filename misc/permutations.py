def permutations(s):
    if not s:
        return [[]]

    result = []
    for i in s:
        filtered = filter(lambda x: x != i, s)
        for p in permutations(filtered):
            j = [i]
            j.extend(p)
            result.append(j)

    return result


def flatmap(func, l):
    result = []
    for e in l:
        result.extend(func(e))
    return result


def permute(s):
    if not s:
        return [[]]

    return flatmap(
        (lambda x: map(lambda p: [x] + p,
                       permute(filter(lambda y: y != x, s)))),
        s)

if __name__ == '__main__':
    print permutations([1, 2, 3, 4])
    print permute([1, 2, 3, 4])

