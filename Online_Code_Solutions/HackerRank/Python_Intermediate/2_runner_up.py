if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    # Use set() to make a set list() to make set a list and sorted() to sort list
    lst = sorted(list(set(arr)))
    # grab secdon to last element in list
    print(lst[-2])
