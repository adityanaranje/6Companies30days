# Given an array of strings, return all groups of strings that are anagrams.

'''
sample_array = ["listen", "silent","angel","bored","dusty","cloudy","night",
"sadder","mouse","arc","cat","elbow","below","glean","dreads","thing",
"study","robed","car","act","peach","cheap","cider","brag","grab",
"vase","state","drop","players","care","rac"]
'''


def get_anagrams(arr):
    print("The all groups of strings that are anagrams are:- ")
    x = 1
    lst = arr.copy()
    for i in arr:
        list1 = []
        list1.append(i)
        arr.remove(i)
        for j in arr:
            if (sorted(i))==(sorted(j)):
                list1.append(j)
                arr.remove(j)
        if len(list1)>1:
            for val in list1:
                lst.remove(val)
            print(f"Group {x} = {list1}")
            x = x+1

    print(f"Non anagram strings {lst}")

given_array = []

n = int(input("Enter no of string in array:- "))
for _ in range(n):
    ele = input()
    given_array.append(ele)

get_anagrams(given_array)


# Input
'''
Enter no of string in array:- 7
listen 
silent
angel
brag
grab
rac
state
'''

#Output
'''
The all groups of strings that are anagrams are:- 
Group 1 = ['listen', 'silent']
Group 2 = ['brag', 'grab']
Non anagram strings ['angel', 'rac', 'state']
'''