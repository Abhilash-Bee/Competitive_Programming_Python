def solid_parallelogram(size):
    for i in range(size):
        for k in range(size - 1 - i):
            print(' ', end='')

        for j in range(size):
            print('*', end='')
        print()


def hollow_parallelogram(size):
    for i in range(size):
        for k in range(size - 1 - i):
            print(' ', end='')

        for j in range(size):
            if i == 0 or i == size - 1 or \
                    j == 0 or j == size - 1:
                print('*', end='')
            else:
                print(' ', end='')
        print()


def main():
    size = int(input())
    solid_parallelogram(size)
    print(end='\n\n')
    hollow_parallelogram(size)


if __name__ == '__main__':
    main()
