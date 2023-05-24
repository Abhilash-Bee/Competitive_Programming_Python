def solid_hourglass(size):
    for i in range(size):
        for k in range(i):
            print(' ', end='')

        for j in range(i, (size - 1) * 2 - i + 1):
            print('*', end='')
        print()

    for i in range(size):
        for k in range(size - 1 - i):
            print(' ', end='')

        for j in range(size - 1 - i, size + i):
            print('*', end='')
        print()


def hollow_hourglass(size):
    for i in range(size):
        for k in range(i):
            print(' ', end='')

        for j in range(i, (size - 1) * 2 - i + 1):
            if i == 0 or j == i or j == (size - 1) * 2 - i:
                print('*', end='')
            else:
                print(' ', end='')
        print()

    for i in range(size):
        for k in range(size - 1 - i):
            print(' ', end='')

        for j in range(size - 1 - i, size + i):
            if i == size - 1 or j == size - 1 - i or j == size - 1 + i:
                print('*', end='')
            else:
                print(' ', end='')
        print()


def main():
    size = int(input())
    solid_hourglass(size)
    print(end='\n\n')
    hollow_hourglass(size)


if __name__ == '__main__':
    main()
