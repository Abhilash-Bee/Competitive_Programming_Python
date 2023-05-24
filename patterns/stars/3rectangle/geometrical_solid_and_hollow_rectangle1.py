def solid_rectangle(size1, size2):
    for i in range(size1):
        for j in range(size2):
            print('*', end='')
        print()


def hollow_rectangle(size1, size2):
    for i in range(size1):
        for j in range(size2):
            if i == 0 or i == size1 - 1 or j == 0 or j == size2 - 1:
                print('*', end='')
            else:
                print(' ', end='')
        print()


def main():
    size1 = int(input())
    size2 = int(input())
    solid_rectangle(size1, size2)
    print(end='\n\n')
    hollow_rectangle(size1, size2)


if __name__ == '__main__':
    main()
