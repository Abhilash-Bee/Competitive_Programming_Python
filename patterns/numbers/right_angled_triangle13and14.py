def pattern13(size):
    for i in range(size):
        for k in range(i):
            print('  ', end='')

        for j in range(i, size):
            print(size - 1 - j, end=' ')
        print()


def pattern14(size):
    for i in range(size):
        for k in range(i):
            print('  ', end='')

        for j in range(i, size):
            print(j - i, end=' ')
        print()


def main():
    size = int(input())
    pattern13(size)
    print(end='\n\n')
    pattern14(size)


if __name__ == '__main__':
    main()
