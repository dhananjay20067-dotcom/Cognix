# Day 2: October 6, 2025
# Topic: Strings and Operators

# Example 1
text = "Python Programming"
print(text[0:6])
print(text[7:18])
print(text[-11:])

#Example 2- Negative Indexing
name = "Rajesh"
print(name[-1])
print(name[-3:])

#Example # - Step in Slicing 
word = "Mechanical"
print(word[::2])
print(word[::-1])

#Example 4 : String Method - uppercase and lowercase
college = "pes modern college"
print(college.upper())
print(college.title())
print(college.capitalize())
print(college.lower())

#Example 5 : Strip Whitespaces
messy = "  Hello, World  "
print(messy.strip())
print(len(messy))
print(len(messy.strip()))

#Example 6 : Split and Join
sentence = "I love Python programming"
words = sentence.split()
print(words)
print("-".join(words))

#Example 7: Find and Replace
text = "Python is easy. Python is powerful."
print(text.find("easy"))
print(text.replace("Python", "Coding"))

#Example 8: Check if substring exists
email = "student@pes.in"
print("@" in email)
print("gmail" in email)

#Example 9: String Concatentation
first = "Mechancial"
second = 'Engineering'
print(first + " " + second)

#Example 10: Format strings
marks = 85
attendance = 78
print(f"Marks {marks}, Attendance: {attendance}%")

print(17 / 5) # Division
print(17 // 5) # Floor Division
print(17 % 5) # Modulus
print(2 ** 3) # Exponentiation
print(5 ** 2)
print(5 + 3 * 2) # Operator Precedence

x = 10 
y = 20

print (x == y) # Equal
print (x != y) # Not Equal
print (x > y) # Greater than
print (x < y) # Less than
print (x >= y) # Greater than or Equal to
print (x <= 10) # Less than or Equal to

marks - 75
attendance = 84
if marks >= 75 and attendance >= 75:
    print ("Pass")
else:
    print ("Fail")

marks = 85
if marks >= 90 and marks >= 40:
    print("Eligible")

print("Hello DHANANJAY")

is_raining = False
if not is_raining:
    print("GO outside")

num1 = "12"
num2 = "24"
print(num1 + num2) # String Concatenation
print(int(num1) + int(num2)) # Integer Addition

#Questions for Practice
print(15 - 5 * 2)
print(20 / 4 * 2)   
print(3 ** 2 ** 2)
print(10 > 5 and 8 < 12)
print(not (5 > 3))

