def pattern7(size):
    for i in range(size):
        for j in range(i + 1):
            print(j, end=' ')
        print()


def pattern8(size):
    for i in range(size):
        for j in range(i + 1):
            print(i - j, end=' ')
        print()


def main():
    size = int(input())
    pattern7(size)
    print(end='\n\n')
    pattern8(size)


if __name__ == '__main__':
    main()
