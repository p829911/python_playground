import numpy as np


def rot(n, x, y, rx, ry):
    if ry == 0:

        # reflect
        if rx == 1:
            x = n - 1 - x
            y = n - 1 - y

        # flip
        x, y = y, x

    return x, y


def hilbert_map(m):
    n = 2 ** m

    tmp_array = np.zeros((n, n))

    for t in range(n * n):
        idx = t
        x = 0
        y = 0
        s = 1

        while s < n:

            rx = (t // 2) % 2

            if rx == 0:
                ry = t % 2

            else:
                ry = (t ^ rx) % 2

            x, y = rot(s, x, y, rx, ry)
            x = x + s * rx
            y = y + s * ry
            t = t // 4

            s = s * 2

        tmp_array[x, y] = idx

    return tmp_array.astype(int)


tmp_array = hilbert_map(2)
print(tmp_array)
