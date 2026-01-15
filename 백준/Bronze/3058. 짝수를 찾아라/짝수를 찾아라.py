for _ in range(int(input())):
    nums = list(map(int, input().split()))
    evens = [n for n in nums if n % 2 == 0]
    print(sum(evens), min(evens))