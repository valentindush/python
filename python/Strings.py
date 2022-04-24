from turtle import title


s = "Hello world"
a = "hello world"

#String methods casefold() capitalize()

print(s.casefold() == a.casefold())
print(s)

#Slicing strings

print(a[2:7]) #we don't get the last element || we use colon 
print(a[0:12:2]) #skipping by 2

#Using string.center()

print(s.center(20, "*"))

#.conut() function

print(s.count("l"))

#using * operator on strings

print(s*4)  #prints s 4 times

#IN and NOT IN operator

print('a' in s)
print('a' not in s)

#.title()
print("this is title with python".title())

#Swapcase() reverses the case of the string()

#endswith && startswith returns true/false on strings



