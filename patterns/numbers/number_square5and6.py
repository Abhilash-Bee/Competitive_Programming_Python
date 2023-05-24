def pattern5(size):
    for i in range(size):
        for j in range(size):
            if i % 2 == 0:
                print(0, end=' ')
            else:
                print(1, end=' ')
        print()


def pattern6(size):
    for i in range(size):
        for j in range(size):
            if j % 2 == 0:
                print(0, end=' ')
            else:
                print(1, end=' ')
        print()


def main():
    size = int(input())
    pattern5(size)
    print(end='\n\n')
    pattern6(size)


if __name__ == '__main__':
    main()
