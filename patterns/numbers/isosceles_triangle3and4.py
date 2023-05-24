def pattern3(size):
    for i in range(size):
        for k in range(size - 1 - i):
            print('  ', end='')

        for j in range(size - 1 - i, size + i):
            if j <= size - 1:
                print(j - (size - 1 - i), end=' ')
            else:
                print((size - 1 + i) - j, end=' ')

        print()


def pattern4(size):
    for i in range(size):
        for k in range(i):
            print('  ', end='')

        for j in range(i, (size - 1) * 2 - i + 1):
            if j <= size - 1:
                print(j - i, end=' ')
            else:
                print((size - 1) * 2 - i - j, end=' ')

        print()


def main():
    size = int(input())
    pattern3(size)
    print(end='\n\n')
    pattern4(size)


if __name__ == '__main__':
    main()
