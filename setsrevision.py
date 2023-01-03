#sets are used to storre multiple items in a single variable

#a set is a collection which is unordered unchangeable and unindexed
#set are represented in {} 

set = {"name = rishi","id = 9999","country = india","pincode = 231001"}

print(set)


#type
print(type(set))

#acces items
for x in set:
    print(set)

#####
print("name = rishi" in set)


#add items
set.add("class = computer")
print(set)

#add sets
data = {"staff = phd","id= 0001","qualification = high"}

set.update(data)

print(set)


#remove items
#we can use different methods to remove items like 
#remove()
#.discard()
#pop()
#del set()

#we use here discard method here
set.discard("country = india")
print(set)


#looping in set
for x in set:
    print(x)
        
#joining set

set1 = {1,3,5,66}
set2 = {"rishi","krish","pratham","shrey"}

set3 = set1.union(set2)
print(set3)

#can also use .update() method
