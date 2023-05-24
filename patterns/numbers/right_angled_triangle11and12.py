def pattern11(size):
    for i in range(size):
        for k in range(size - 1 - i):
            print('  ', end='')

        for j in range(size - 1 - i, size):
            print(size - 1 - j, end=' ')
        print()


def pattern12(size):
    for i in range(size):
        for k in range(size - 1 - i):
            print('  ', end='')

        for j in range(size - 1 - i, size):
            print(j - (size - 1 - i), end=' ')
        print()


def main():
    size = int(input())
    pattern11(size)
    print(end='\n\n')
    pattern12(size)


if __name__ == '__main__':
    main()
