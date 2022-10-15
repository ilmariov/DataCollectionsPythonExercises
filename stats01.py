from math import sqrt


def getNumbers():
    nums = []
    xStr = input('Enter a number (<Enter> to quit) >> ')
    while xStr != '':
        x = float(xStr)
        nums.append(x)
        xStr = input('Enter a number (<Enter> to quit) >> ')
    return nums

def mean(nums):
    total = 0.0
    for num in nums:
        total = total + num
    return total / len(nums)

def stdDev(nums):
    sumDevSq = 0.0
    for num in nums:
        dev = mean(nums) - num
        sumDevSq = sumDevSq + (dev*dev)
    return sqrt(sumDevSq/(len(nums)-1))

def meanStdDev(nums):
    return mean(nums), stdDev(nums)

def main():
    print('This program computes mean and standard deviation.')
    data = getNumbers()
    avg, std = meanStdDev(data)

    print('The mean is {0:0.4}'.format(avg))
    print('The standard deviation is {0:0.4}'.format(std))


if __name__=='__main__': main()