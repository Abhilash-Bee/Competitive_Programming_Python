def pattern_d1(size):
    for i in range(size):
        for j in range(size):
            if i == 0 \
                    or i == size - 1 \
                    or j == 0 \
                    or j == size - 1:
                print('* ', end='')
            else:
                print('  ', end='')
        print()


def pattern_d2(size):
    for i in range(size):
        for j in range(size):
            if (i == 0 and j != size - 1) \
                    or (i == size - 1 and j != size - 1) \
                    or j == 0 \
                    or (j == size - 1 and i != 0 and i != size - 1):
                print('* ', end='')
            else:
                print('  ', end='')
        print()


def main():
    size = int(input())
    pattern_d1(size)
    print(end='\n\n')
    pattern_d2(size)


if __name__ == '__main__':
    main()
