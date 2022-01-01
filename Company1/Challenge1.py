# Given an array of strings, return all groups of strings that are anagrams.

given_array = ["listen", "silent","angel","bored","dusty","cloudy","night",
"sadder","mouse","arc","cat","elbow","below","glean","dreads","thing",
"study","robed","car","act","peach","cheap","cider","brag","grab",
"vase","state","drop","players","care","rac"]

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
    
get_anagrams(given_array)