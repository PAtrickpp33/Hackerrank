if __name__ == '__main__':
    n = int(input())
    a = map(int, input().split())
    largest = secondlargest = -100
    for x in a:
        if x > largest:
            tmp = largest
            largest = x
            secondlargest = tmp
        elif x > secondlargest and x != largest:
            secondlargest = x
    print(secondlargest)