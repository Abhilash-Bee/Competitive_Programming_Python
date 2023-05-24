def pattern_q1(size):
    for i in range(size):
        for j in range(size):
            if (i == 0 and j <= (3 * size) // 4) \
                    or (i == (3 * size) // 4 and j <= (3 * size) // 4) \
                    or (j == 0 and i <= (3 * size) // 4) \
                    or (j == (3 * size) // 4 and i <= (3 * size) // 4) \
                    or (i == j and i >= size // 2):
                print('* ', end='')
            else:
                print('  ', end='')
        print()


def pattern_q2(size):
    for i in range(size):
        for j in range(size):
            if (i == 0 and j != 0 and j < (3 * size) // 4) \
                        or (i == (3 * size) // 4 and j != 0 and j < (3 * size) // 4) \
                        or (j == 0 and i != 0 and i < (3 * size) // 4) \
                        or (j == (3 * size) // 4 and i != 0 and i < (3 * size) // 4) \
                        or (i == j and i >= size // 2):
                print('* ', end='')
            else:
                print('  ', end='')
        print()


def main():
    size = int(input())
    pattern_q1(size)
    print(end='\n\n')
    pattern_q2(size)


if __name__ == '__main__':
    main()
