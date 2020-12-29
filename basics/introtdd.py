def Reverse(l): 
    return [i for i in reversed(l)] 

arr = [10, 11, 12, 13, 14, 15] 
print(Reverse(arr)) 

print ("-" * 30)


def isPalindrome(l):
    for i in range(0, int(len(l)/2)): 
        if l[i] != l[len(l)-i-1]:
            return False
    return True

sal = "racecar"

print(isPalindrome(sal))

print ("-" * 30)

#def coins(l):

print ("-" * 30)

def Fibonacci(n): 
    if n<0: 
        print("Incorrect input") 
    elif n==0: 
        return 0
    
    elif n==1: 
        return 1
    else: 
        return Fibonacci(n-1)+Fibonacci(n-2) 

print(Fibonacci(10))

print ("-" * 30)

def factorial(n):
    res = 1
    for i in range(2, n+1): 
        res *= i 
    return res 

print("Factorial:", factorial(5))

print ("-" * 30)

