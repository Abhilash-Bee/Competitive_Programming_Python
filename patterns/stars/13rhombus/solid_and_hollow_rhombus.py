def solid_rhombus(size):
    for i in range(size):
        for k in range(size - 1 - i):
            print(' ', end='')

        for j in range(size - 1 - i, size + i):
            print('*', end='')
        print()

    for i in range(1, size):
        for k in range(i):
            print(' ', end='')

        for j in range(i, (size - 1) * 2 - i + 1):
            print('*', end='')
        print()


def hollow_rhombus(size):
    for i in range(size):
        for k in range(size - 1 - i):
            print(' ', end='')

        for j in range(size - 1 - i, size + i):
            if j == size - 1 - i or j == size - 1 + i:
                print('*', end='')
            else:
                print(' ', end='')
        print()

    for i in range(1, size):
        for k in range(i):
            print(' ', end='')

        for j in range(i, (size - 1) * 2 - i + 1):
            if j == i or j == (size - 1) * 2 - i:
                print('*', end='')
            else:
                print(' ', end='')
        print()


def main():
    size = int(input())
    solid_rhombus(size)
    print(end='\n\n')
    hollow_rhombus(size)


if __name__ == '__main__':
    main()
