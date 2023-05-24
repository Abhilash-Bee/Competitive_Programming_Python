def pattern_m(size):
    for i in range(size):
        for j in range(size):
            if j == 0 \
                    or j == size - 1 \
                    or (i == j and i <= size // 2) \
                    or (i + j) == size - 1 and i <= size // 2:
                print('* ', end='')
            else:
                print('  ', end='')
        print()


def main():
    size = int(input())
    pattern_m(size)


if __name__ == '__main__':
    main()
