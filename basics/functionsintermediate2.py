#Update Values in Dictionaries and Lists
x = [ [5,2,3], [15,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]
#Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
x[1][0] = 15
print(x)

#Change the last_name of the first student from 'Jordan' to 'Bryant'
students[0]['last_name'] = 'Bryant'
print (students)

#In the sports_directory, change 'Messi' to 'Andres'
sports_directory['soccer'][0] = 'Andres'
print (sports_directory) 

#Change the value 20 in z to 30
z[0]['y'] = 30
print(z)

#Iterate Through a List of Dictionaries
def iterateDictionary(l): 
    for i in range(len(l)):
        for key in l[i]:
            print(key , '-' , l[i][key])

#Get Values From a List of Dictionaries
def iterateDictionary2(k, l):
    for i in range(len(l)):
        print(l[i][k])

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
iterateDictionary(students)
iterateDictionary2('first_name' , students)
iterateDictionary2('last_name',students)







#Iterate Through a Dictionary with List Values
def printInfo(d):
    for key in d:
        print(len(d[key]))
        for i in range(len(d[key])):
            print(d[key][i])

dojo = {
'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)



