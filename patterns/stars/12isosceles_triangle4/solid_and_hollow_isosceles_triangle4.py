def solid_triangle(size):
    for i in range(size):
        for k in range(size - 1 - i):
            print(' ', end='')

        for j in range(size - 1 - i, size):
            print('*', end='')
        print()

    for i in range(1, size):
        for k in range(i):
            print(' ', end='')

        for j in range(i, size):
            print('*', end='')
        print()


def hollow_triangle(size):
    for i in range(size):
        for k in range(size - 1 - i):
            print(' ', end='')

        for j in range(size - 1 - i, size):
            if j == size - 1 - i or j == size - 1:
                print('*', end='')
            else:
                print(' ', end='')
        print()

    for i in range(1, size):
        for k in range(i):
            print(' ', end='')

        for j in range(i, size):
            if j == i or j == size - 1:
                print('*', end='')
            else:
                print(' ', end='')
        print()


def main():
    size = int(input())
    solid_triangle(size)
    print(end='\n\n')
    hollow_triangle(size)


if __name__ == '__main__':
    main()
