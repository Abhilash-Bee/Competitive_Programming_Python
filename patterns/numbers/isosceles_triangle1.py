def pattern1(size):
    for i in range(size):
        for k in range(size - 1 - i):
            print('  ', end='')

        for j in range(size - 1 - i, size + i):
            if j <= size - 1:
                print((size - 1) - j, end=' ')
            else:
                print(j - (size - 1), end=' ')

        print()


def main():
    size = int(input())
    pattern1(size)


if __name__ == '__main__':
    main()
