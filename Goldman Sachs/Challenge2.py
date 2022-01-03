# Given two rectangles, find if the given two rectangles overlap or not. 

class Sovle():

    def overlap(self, l1, r1, l2, r2):
        if (l1[0] == r1[0] or l1[1] == r1[1]or l2[0] == r2[0] or l2[1] == r2[1]):
            return False

        if(l1[0] >= r2[0] or l2[0] >= r1[0]):
            return False
    
        if(r1[1] >= l2[1] or r2[1] >= l1[1]):
            return False
    
        return True
 


obj = Sovle()

x, y = [int(a) for a in input("Enter co-ordinates for top left of rectangle 1 :- ").split()]
l1 = (x, y) 
x, y = [int(a) for a in input("Enter co-ordinates for bottom right of rectangle 1 :- ").split()]
r1 = (x, y)
x, y = [int(a) for a in input("Enter co-ordinates for top left of rectangle 2 :- ").split()]
l2 = (x, y)
x, y = [int(a) for a in input("Enter co-ordinates for bottom right of rectangle 2 :- ").split()]
r2 = (x, y)

ans = obj.overlap(l1, r1, l2, r2)

if ans:
    print("Rectangles are overlapping")
else:
    print("Rectangles are not overlapping")



# Output
'''
Enter co-ordinates for top left of rectangle 1 :- 2 2
Enter co-ordinates for bottom right of rectangle 1 :- 4 0 
Enter co-ordinates for top left of rectangle 2 :- 3 4
Enter co-ordinates for bottom right of rectangle 2 :- 5 1
Rectangles are overlapping
'''