def pattern1(size):
    for i in range(size):
        for j in range(i + 1):
            print(i, end=' ')
        print()


def pattern2(size):
    for i in range(size):
        for j in range(i + 1):
            print(size - i - 1, end=' ')
        print()


def main():
    size = int(input())
    pattern1(size)
    print(end='\n\n')
    pattern2(size)


if __name__ == '__main__':
    main()
