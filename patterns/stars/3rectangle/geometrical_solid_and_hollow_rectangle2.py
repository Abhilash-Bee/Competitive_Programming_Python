def solid_rectangle(size1, size2):
    for i in range(size1):
        print('*' * size2)


def hollow_rectangle(size1, size2):
    for i in range(size1):
        for j in range(size2):
            if i == 0 or i == size1 - 1 or \
                    j == 0 or j == size2 - 1:
                print('*', end='')
            else:
                print(' ', end='')
        print()


def main():
    size = list(map(int, input().split()))
    size1, size2 = size
    solid_rectangle(size1, size2)
    print(end='\n\n')
    hollow_rectangle(size1, size2)


if __name__ == '__main__':
    main()
