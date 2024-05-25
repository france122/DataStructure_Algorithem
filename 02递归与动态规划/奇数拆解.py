def partition_odd_numbers(n, odd_numbers=[]):
    if n == 0:
        for x in odd_numbers:
            if x!=odd_numbers[-1]:
                print(x,end=" ")
            else:
                print(x)
        return 1
    elif n < 0:
        return 0

    count = 0
    start = 1 if not odd_numbers else odd_numbers[-1] + 2
    for i in range(start, n + 1, 2):
        count += partition_odd_numbers(n - i, odd_numbers + [i])

    return count

if __name__ == "__main__":
    N = int(input())
    count = partition_odd_numbers(N)
    print(count)
