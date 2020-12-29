#Biggie Size
def biggie(l):
    for i in range(len(l)):
        if l[i] > 0:
            print("big")
        else:
            print(l[i])
    
print (biggie([-1,5,5,-3]))

#Count Positives
def countpos(l):
    sum = 0
    for i in range(len(l)):
        if l[i] > 0:
            sum += 1
    
    l[-1] = sum
    return l
        
print (countpos([-1,5,5,-3]))

#Sum Total
def sum(l):
    sum = 0
    for i in range(len(l)):
        sum += l[i]
    return sum

print (sum([2,3,5,1]))

#Average
def avg(l):
    sum= 0
    for i in l:
        sum += i
        avg = sum/len(l)
    return avg
print (avg([1,2,3,4]))

#Length
def length(l):
    x = len(l)
    return x
print (length([1,2,3,4]))

#Minimum
def min(l):
    min = l[0]
    for i in range(len(l)):
        if l[i] < min:
            min = l[i]
    return min
print (min([6,1,3,4]))

#Maximum
def max(l):
    max = l[0]
    for i in range(len(l)):
        if l[i] > max:
            max = l[i]
    return max
print (max([6,1,3,4]))

#Ultimate Analysis
def max_min_avg_length (l):
    sum = 0
    min = l[0]
    max = l[0]
    x = len(l)
    for i in l:
        sum += i
        if i < min:
            min = i
        if i > max:
            max = i
    return {"sum":sum , "avg":sum/len(l), "min":min , "max":max , "length": x}

print (max_min_avg_length([4,5,6,7,8]))

#Reverse List
def reverse(l):
    return l[::-1]

print (reverse([4,5,6,7,8]))
