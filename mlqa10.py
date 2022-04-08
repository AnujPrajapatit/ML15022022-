l=[]
l2=[]
x=int(input("Enter the list1:"))
y=int(input("Enter the list2:"))
for i in range(0,x):
    e = int(input())

    l.append(e) ## adding the element

for i in range(0,y):
    f = int(input())

    l2.append(f) ## adding the element

print(l)

print(l2)

################output##############
##Enter the list1:3
##Enter the list2:3
##23
##54
##12

##98
##3
##17
##[23, 54, 12]
##[98, 3, 17]
