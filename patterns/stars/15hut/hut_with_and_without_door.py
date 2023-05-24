def hut_without_door(size):
    for i in range(size):
        for k in range(size - 1 - i):
            print(' ', end='')

        for j in range(size - 1 - i, size + i):
            print('*', end='')
        print()

    for i in range(size):
        for j in range((size - 1) * 2 + 1):
            print('*', end='')
        print()


def hut_with_door(size):
    for i in range(size):
        for k in range(size - 1 - i):
            print(' ', end='')

        for j in range(size - 1 - i, size + i):
            print('*', end='')
        print()

    for i in range(size):
        for j in range((size - 1) * 2 + 1):
            if i >= size / 4 and j >= (size - 1) * 2 / 4 and \
                    j <= ((size - 1) * 2) - (size - 1) * 2 / 4:
                print(' ', end='')
            else:
                print('*', end='')
        print()


def main():
    size = int(input())
    hut_without_door(size)
    print(end='\n\n')
    hut_with_door(size)


if __name__ == '__main__':
    main()
