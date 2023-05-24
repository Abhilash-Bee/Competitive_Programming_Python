def pattern(size):
    for i in range(size):
        for k in range(size - 1 - i):
            print('  ', end='')

        for j in range(size - 1 - i, size + i):
            if j <= size - 1:
                print(chr(65 + ((size - 1) - j)), end=' ')
            else:
                print(chr(65 + (j - (size - 1))), end=' ')

        print()


def main():
    size = int(input())
    pattern(size)


if __name__ == '__main__':
    main()
