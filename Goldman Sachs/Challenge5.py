# Ugly numbers are numbers whose only prime factors are 2, 3 or 5. 
# The sequence 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, … shows the first
#  11 ugly numbers. By convention, 1 is included. Write a program to
#  find Nth Ugly Number.


class Solution:
    def getNthUglyNo(self,n):
        num_2 = 0
        num_3 = 0
        num_5 = 0
        arr = [0]
        arr[0] = 1
        
        for i in range(2,n+1):
            j = arr[num_2] * 2
            k = arr[num_3] * 3
            l = arr[num_5] * 5
            if min(j,k,l) == j:
                num_2 += 1
            if min(j,k,l) == k:
                num_3 += 1
            if min(j,k,l) == l:
                num_5 += 1
            arr.append(min(j,k,l))
        return arr[-1]


if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        ob = Solution()
        ans = ob.getNthUglyNo(n);
        print(ans)
        tc -= 1