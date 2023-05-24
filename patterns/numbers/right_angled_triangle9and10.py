def pattern9(size):
    for i in range(size):
        for j in range(size - i):
            print(j, end=' ')
        print()


def pattern10(size):
    for i in range(size):
        for j in range(size - i):
            print(size - 1 - i - j, end=' ')
        print()


def main():
    size = int(input())
    pattern9(size)
    print(end='\n\n')
    pattern10(size)


if __name__ == '__main__':
    main()
