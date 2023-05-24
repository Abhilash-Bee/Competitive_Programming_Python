def pattern11and7(size):
    for i in range(size):
        for k in range(size - 1 - i):
            print('  ', end='')

        for j in range(size - 1 - i, size):
            print((size - 1) - j, end=' ')

        for j in range(1, i + 1):
            print(j, end=' ')

        print()


def main():
    size = int(input())
    pattern11and7(size)


if __name__ == '__main__':
    main()
