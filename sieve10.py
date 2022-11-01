def sieve():
    n = 0
    while (n <= 2):
        n = int(input('Find primes up to: '))

    nums = []
    for i in range(2, n+1):
        nums.append(i)
    
    primes = []
    while(len(nums) >= 1):
        prime = nums.pop(0)
        primes.append(prime)
        for num in nums:
            if (num % prime == 0):
                nums.remove(num)
    
    print('Here is the list of primes up to', n)
    print(primes)


sieve()