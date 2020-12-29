def checkbraces(myStr): 
    opened = ["[","{","("] 
    closed = ["]","}",")"] 
    arr = [] 
    for i in myStr: 
        if i in opened: 
            arr.append(i) 
        elif i in closed: 
            pos = closed.index(i) 
            if ((len(arr) > 0) and
                (opened[pos] == arr[len(arr)-1])): 
                arr.pop() 
            else: 
                return False
    if len(arr) == 0: 
        return True
    else: 
        return False

string = "{w[t]a{va(n)}}"
string2 = ")P()}na[g("
print(string,"-", checkbraces(string)) 
print(string2,"-", checkbraces(string2)) 