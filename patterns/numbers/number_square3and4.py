def pattern3(size):
    for i in range(size):
        for j in range(size):
            print(size - 1 - i, end=' ')
        print()


def pattern4(size):
    for i in range(size):
        for j in range(size):
            print(size - 1 - j, end=' ')
        print()


def main():
    size = int(input())
    pattern3(size)
    print(end='\n\n')
    pattern4(size)


if __name__ == '__main__':
    main()
