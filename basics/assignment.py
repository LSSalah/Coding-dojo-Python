def firstnlast(l):
    if len(l) < 2:
        return false
    return l[0], l[-1]

print (firstnlast([4,5,6,7,8]))

////////////////////////////////////////////

def sum (l):
    sum = 0 
    for i in l:
        sum += i
    return sum 

print (sum([4,5,6,7,8]))

/////////////////////////////////////////////

def reverse(l):
    return l[::-1]

print (reverse([4,5,6,7,8]))

/////////////////////////////////////////////

def max_min_avg (l):
    sum = 0
    min = l[0]
    max = l[0]
    for i in l:
        sum += i
        if i < min:
            min = i
        if i > max:
            max = i
    return {"sum":sum , "avg":sum/len(l), "min":min , "max":max}

print (max_min_avg([4,5,6,7,8]))

/////////////////////////////////////////////////////////////

def bubble(l, n):
    
    if n == 0:
        return l

    
    for i in range(1, n + 1):
        if l[i] < l[i - 1]:
            l[i], l[i-1] = l[i - 1], l[i]

    
    return bubble(l, n - 1)
        
salah = [4,6,8,5,1]
print(bubble(salah, len(salah)-1))   