users = ["Hizkia", "Albert", "Arundaa"]

data = ["Hizkia", 20, True]

emptylist = []

print("Hizkia" in emptylist)

print(users[0])
print(users[-2])

print(users.index("Arundaa"))
print(users[0:2])
print(users[1:])
print(users[-3:-1])

print(len(data))

users.append("Elsa")
print(users)

users += ["Angel"]
print(users)

users.extend(["Sabatini", "Ethan"])
print(users)

# users.extend(data)
# print(users)

users.insert(0, "Tristan")
print(users)

users[2:2] = ["Natacia", "Chemistriana"]
print(users)

# slice
users[1:3] = ["Kay", "Arky"]
print(users)

users.remove("Tristan")
print(users)

print(users.pop())
print(users)

del users[0]
print(users)

# del data
data.clear()
print(data)

users[1:2] = ['hizkia']
users.sort()
print(users)

users.sort(key=str.lower)
print(users)

nums = [4, 20, 42, 1, 5]
nums.reverse()
print(nums)

# nums.sort(reverse=True)
# print(nums)

print(sorted(nums, reverse=True))
print(nums)

numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]
print(numscopy)
print(mynums)
mycopy.sort()
print(mycopy)
print(nums)

print(type(nums))

mylist = list([1, "Neil", True])
print(mylist)

# Tuples

myTuple = tuple(("Hizkia", 20, True))

anotherTuple = (1, 6, 4, 8, 4, 4)
print(myTuple)
print(type(myTuple))
print(type(anotherTuple))

newList = list(myTuple)
newList.append("Kay")
newTuple = tuple(newList)
print(newTuple)
(one, *two, hey) = anotherTuple
print(one)
print(two)
print(hey)

print(anotherTuple.count(2))
