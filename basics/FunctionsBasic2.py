#CountDown
def countDown(l):
    for x in range(l,-1,-1):
            print (x)

print(countDown(5))

#Print and Return
def printReturn(l):
    print (l[0])
    return l[1]

x = printReturn([6,7])
print (printReturn([4,5]))
print (x)

#First Plus Length
def plus(l):
    x = l[0] + len(l)
    return x 

print (plus([1,2,3,4,5]))

#Values Greater than Second
def greater(l):
    if len(l) < 2:
        return false
    newl = []
    for i in range(len(l)):
        if l[1] < l[i]:
            newl.append(l[i])
    return newl
print (greater([5,2,3,2,1,4]))

#This Length, That Value
def lengthvalue(size , value):
    new_list= []
    for x in range(size):
        new_list.append(value)
    return new_list
print (lengthvalue(4,7))




