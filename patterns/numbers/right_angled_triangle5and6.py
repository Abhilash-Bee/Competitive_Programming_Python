def pattern5(size):
    for i in range(1, size + 1):
        count = i * (i + 1) // 2
        for j in range(i):
            print(count - j, end=' ')
        print()


def pattern6(size):
    count = 0
    for i in range(1, size + 1):
        if i % 2 == 0:
            count = i * (i + 1) // 2
            for j in range(i):
                print(count - j, end=' ')

        if i % 2 == 1:
            for j in range(i):
                print(count + j + 1, end=' ')
        print()


def main():
    size = int(input())
    pattern5(size)
    print(end='\n\n')
    pattern6(size)


if __name__ == '__main__':
    main()
