name = "Arnab"
friend = "Vrinda"
print("Hello",name,"and",friend)
apple = """He said
Hi Arnab
I am good.
How are you doing ?
I am also fine
Everything is so interesting
"""
print(apple)

# string indexing
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
# print(name[5]) # This throws an error

"""
for var in sequence:
    # statements
"""
print("Let's use a for loop with strings")
for char in name:
    print(char)

print("Let's use a for loop\n")
for i in apple:
    print(i)