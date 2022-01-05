fruits = ["apple", "banana", "pineapple", "orange"]

for x in fruits:
    if x == "pineapple":
        fruits.append("grapes")
print(fruits)
for x in fruits:
    if x == "banana":
        fruits.remove("pineapple")
print(fruits)

x = "orang"
if x == "orange":
    print('hi ram-ya')
elif x == "banana":
    print("hello ram-ya")
else:
    print("hey")


