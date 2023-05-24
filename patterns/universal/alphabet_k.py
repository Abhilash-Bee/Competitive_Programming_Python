def pattern_k(size):
    for i in range(size):
        for j in range(size):
            if j == 0 \
                    or (i + j) == size // 2 \
                    or (i - j) == size // 2:
                print('* ', end='')
            else:
                print('  ', end='')
        print()


def main():
    size = int(input())
    pattern_k(size)


if __name__ == '__main__':
    main()
