def pattern13and9(size):
    for i in range(size):
        for k in range(i):
            print('  ', end='')

        for j in range(i, size):
            print((size - 1) - j, end=' ')

        for j in range(1, size - i):
            print(j, end=' ')

        print()


def main():
    size = int(input())
    pattern13and9(size)


if __name__ == '__main__':
    main()
