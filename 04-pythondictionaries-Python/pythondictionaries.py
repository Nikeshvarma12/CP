"""Time to play with Python dictionaries!
You're going to work on a dictionary that
stores cities by country and continent.
One is done for you - the city of Mountain 
View is in the USA, which is in North America.

You need to add the cities listed below by
modifying the structure.
Then, you should print out the values specified
by looking them up in the structure.

Cities to add:
Bangalore (India, Asia)
Atlanta (USA, North America)
Cairo (Egypt, Africa)
Shanghai (China, Asia)"""


"""Print the following (using "print").
1. A list of all cities in the USA in
alphabetic order. Make it function with name as sortUSA(), return list of cities
2. All cities in Asia, in alphabetic
order, next to the name of the country.
In your output, label each answer with a number
so it looks like this: (Make it function with name as alphaAsia(), return list of cities)
1
American City
American City
2
Asian City - Country
Asian City - Country"""

locations = {'North America': {'USA': ['Atlanta','Mountain View']},'Asia':{'India':['Banglore'],'China':['Shangai']},'Africa':{'Egypt':['Cairo']}}
def sortUSA():
    '''Return all the cities in the USA in alphabetical order'''
    for i in locations:
        if(i=='North America'):
            k=dict(locations['North America'])
            for j in k:
                if(j=='USA'):
                    res1=k['USA']
                    res1.sort
    return res1

def alphaAsia():
    '''Return all the cities in Asia continent in alphabetical order'''
    res2=[]
    for i in locations:
        if(i=='Asia'):
            k=dict(locations['Asia'])
            for j in k:
                result=k[j][0]+ " - "+j
                res2.append(result)
                res2.sort()
    return res2

# Note: Check for test cases to understand the output format.
