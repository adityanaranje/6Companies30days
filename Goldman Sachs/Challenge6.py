# For two strings s and t, we say "t divides s" if and only if
#  s = t + ... + t (i.e., t is concatenated with itself one or more times).
# Given two strings str1 and str2, return the largest string x such that x
#  divides both str1 and str2.


def hcf(a,b):

    if b==0:
        return a
    else:
        return hcf(b,a%b)


class Solution(object):
    def gcdOfStrings(self, str1, str2):
        if str1+str2==str2+str1:
            return str1[:hcf(len(str1), len(str2))]
        else:
            return ""

ob = Solution()  
ans = ob.func("ABABAB","ABAB")
print(ans)