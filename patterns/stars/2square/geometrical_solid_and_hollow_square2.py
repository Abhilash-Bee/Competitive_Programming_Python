def solid_square(size):
    for i in range(size):
        print('*' * size)


def hollow_square(size):
    for i in range(size):
        for j in range(size):
            if i == 0 or i == size - 1 or \
                    j == 0 or j == size - 1:
                print('*', end='')
            else:
                print(' ', end='')
        print()


def main():
    size = int(input())
    solid_square(size)
    print(end='\n\n')
    hollow_square(size)


if __name__ == '__main__':
    main()
