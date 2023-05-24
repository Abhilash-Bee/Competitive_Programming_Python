def solid_triangle(size):
    for i in range(size):
        for j in range(i + 1):
            print('*', end='')
        print()


def hollow_triangle(size):
    for i in range(size):
        for j in range(i + 1):
            if i == size - 1 or j == 0 or j == i:
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
