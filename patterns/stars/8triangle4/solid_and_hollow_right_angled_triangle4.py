def solid_triangle(size):
    for i in range(size):
        for k in range(i):
            print(' ', end='')

        for j in range(i, size):
            print('*', end='')
        print()


def hollow_triangle(size):
    for i in range(size):
        for k in range(i):
            print(' ', end='')

        for j in range(i, size):
            if i == 0 or j == i or \
                    j == size - 1:
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
