def pattern(size):
    for i in range(size):
        for k in range(i):
            print('  ', end='')

        for j in range(i, (size - 1) * 2 - i + 1):
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
