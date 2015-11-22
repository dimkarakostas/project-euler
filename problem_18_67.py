DYNAMIC_TABLE = []
TRIANGLE = []

with open('input_67', 'r') as f:
    for l in f.readlines():
        DYNAMIC_TABLE.append([])
        TRIANGLE.append([])
        for num in l.strip().split(' '):
            DYNAMIC_TABLE[-1].append(0)
            TRIANGLE[-1].append(int(num))


def dynamic(line):
    for i, val in enumerate(TRIANGLE[line]):
        if line == len(TRIANGLE) - 1:
            DYNAMIC_TABLE[line][i] = (val)
        else:
            DYNAMIC_TABLE[line][i] = val + max(DYNAMIC_TABLE[line+1][i], DYNAMIC_TABLE[line+1][i+1])


def main():
    for i in range(len(TRIANGLE)-1, -1, -1):
        dynamic(i)
    print DYNAMIC_TABLE[0][0]


if __name__ == '__main__':
    main()
