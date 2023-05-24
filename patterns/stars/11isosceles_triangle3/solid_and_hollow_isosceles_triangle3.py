def solid_triangle(size):
    for i in range(size):
        for j in range(i + 1):
            print('*', end='')
        print()

    for i in range(1, size):
        for j in range(size - i):
            print('*', end='')
        print()


def hollow_triangle(size):
    for i in range(size):
        for j in range(i + 1):
            if j == 0 or j == i:
                print('*', end='')
            else:
                print(' ', end='')
        print()

    for i in range(1, size):
        for j in range(size - i):
            if j == 0 or j == size - 1 - i:
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
