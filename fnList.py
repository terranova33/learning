

# List function

list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, -2, 3+4j, 4, 5.55]
list3 = ["a", "b", 'c', "d"]
str1 = "Hello World!"

# accessing and updating

print(list1[0]) # prints the first value in list1
print(list1[1]) # prints the second value in list1
print(list2[2:4]) # prints the 3rd and 4th value in list 2
print(list2[1:]) # prints list 2 starting from the 2nd value
print(list2 * 3) # prints list 2 three times
print(list2 + list3) # concantonates list2 and list3

print("Old value of list 1: ", list1)
list1[2] = 1998 # changes the third value in list 1 to 1998
print("New value in list 1: ", list1)

del list1[2] # deletes the third value in list 1
print(list1)
list1.append('2001') # adds 2001 to the end of the list
print(list1)
list1.insert(2, '1997') # inserts original 1997 into list1 at the right spot
print(list1)
list1.remove('2001') # removes 2001 from the list1
print(list1)
list1.reverse() # reverses the order that the list appears
print(list1)

print(list1.count(2000)) # lists how many times 2000 appears in list1 *note that you don't search for a string with an integer

print(len(list1)) # prints how many items are in list1

print(list(list2)) # converts a sequence into a list where 'list2' is the sequence
print(list(str1))

#print(max(list1))
#print(min(list1))
