def rhombus(size):
    for i in range(size):
        for k in range(size - 1 - i):
            print('  ', end='')

        for j in range(size - 1 - i, size + i):
            if j <= size - 1:
                print((size - 1) - j, end=' ')
            else:
                print(j - (size - 1), end=' ')

        print()

    for i in range(1, size):
        for k in range(i):
            print('  ', end='')

        for j in range(i, (size - 1) * 2 - i + 1):
            if j <= size - 1:
                print((size - 1) - j, end=' ')
            else:
                print(j - (size - 1), end=' ')

        print()


def main():
    size = int(input())
    rhombus(size)


if __name__ == '__main__':
    main()
