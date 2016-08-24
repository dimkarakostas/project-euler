from time import time


def triangle(n):
    return (n*(n + 1)) / 2


def pentagonal(n):
    return (n*(3*n - 1)) / 2


def hexagonal(n):
    return n*(2*n - 1)


def main():
    pentagonals = set()
    hexagonals = set()
    correct_triangles = []
    index = 2

    while len(correct_triangles) < 2:
        current_triangle = triangle(index)

        pentagonals.add(pentagonal(index))
        hexagonals.add(hexagonal(index))

        if (current_triangle in pentagonals) and (current_triangle in hexagonals):
            correct_triangles.append(current_triangle)

        index += 1

    print correct_triangles[1]


if __name__ == '__main__':
    t = time()
    main()
    print 'Time:', time() - t
