def pattern_g1(size):
    for i in range(size):
        for j in range(size):
            if i == 0 \
                    or i == size - 1 \
                    or j == 0 \
                    or (j == size - 1 and i >= size // 2) \
                    or (i == size // 2 and j >= size // 2):
                print('* ', end='')
            else:
                print('  ', end='')
        print()


def pattern_g2(size):
    for i in range(size):
        for j in range(size):
            if (i == 0 and j != 0) \
                    or (i == size - 1 and j != 0) \
                    or (j == 0 and i != 0 and i != size - 1) \
                    or (j == size - 1 and i >= size // 2) \
                    or (i == size // 2 and j >= size // 2):
                print('* ', end='')
            else:
                print('  ', end='')
        print()


def main():
    size = int(input())
    pattern_g1(size)
    print(end='\n\n')
    pattern_g2(size)


if __name__ == '__main__':
    main()
