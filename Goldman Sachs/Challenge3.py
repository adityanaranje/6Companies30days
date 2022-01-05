#Given an array of positive numbers, the task is to find the 
# number of possible contiguous subarrays having product less 
# than a given number k.

class Solution:
    def countSubArrayProductLessThanK(self, a, n, k):

        ans = 0
        curr = 1
        start, end = 0,0
        while start <= end and end < len(a):
                while curr < k and end < len(a):
                    curr *= a[end]
                    end += 1
                    if curr < k:
                        ans += (end - start)
                while start <= end and curr >= k:
                    curr = curr // a[start]
                    start += 1
                    if curr < k:
                        ans += (end - start)
        return ans

def main():

    T = int(input())

    while(T > 0):
        n, k = [int(x) for x in input().strip().split()]
        arr = [int(x) for x in input().strip().split()]
        
        print(Solution().countSubArrayProductLessThanK(arr, n, k))

        T -= 1


if __name__ == "__main__":
    main()
