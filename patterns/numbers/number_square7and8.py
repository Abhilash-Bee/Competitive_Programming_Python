def pattern7(size):
    for i in range(size):
        for j in range(size):
            if (i + j) % 2 == 0:
                print(0, end=' ')
            else:
                print(1, end=' ')
        print()


def pattern8(size):
    for i in range(size):
        for j in range(size):
            if (i + j) % 2 == 0:
                print(1, end=' ')
            else:
                print(0, end=' ')
        print()


def main():
    size = int(input())
    pattern7(size)
    print(end='\n\n')
    pattern8(size)


if __name__ == '__main__':
    main()
