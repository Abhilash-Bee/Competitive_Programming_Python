def univ_ptrn(size):
    for i in range(size):
        for j in range(size):
            if i == 0 \
                    or i == size - 1 \
                    or j == 0 \
                    or j == size - 1 \
                    or (i + j) == size // 2 \
                    or (i - j) == size // 2 \
                    or (j - i) == size // 2 \
                    or (i + j) == size + (size // 2) - 1:
                print('* ', end='')
            else:
                print('  ', end='')
        print()


def main():
    size = int(input())
    univ_ptrn(size)


if __name__ == '__main__':
    main()
