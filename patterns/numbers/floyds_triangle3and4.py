def pattern3(size):
    count = 1
    for i in range(size):
        for j in range(i + 1):
            print(count, end=' ')
            count += 1
        print()


def pattern4(size):
    count = (size * (size + 1)) // 2
    for i in range(size):
        for j in range(i + 1):
            print(count, end=' ')
            count -= 1
        print()


def main():
    size = int(input())
    pattern3(size)
    print(end='\n\n')
    pattern4(size)


if __name__ == '__main__':
    main()
