word = "APPLE"

letter = input("Guess a letter in the secret word: ")

if letter in word:
    print(f"There is a {letter}")
else:
    print(f"{letter} was not found")

students = {"Jackson", "Aiden", "Noah", "Matt"}

student = input("Enter the name of a student: ")

if student in students:
    print(f"{student} is a student")
else:
    print(f"{student} was not found")

grades = {"Jackson": "A", "Aiden": "B", "Matt": "C", "Noah": "F"} 

student = input("Enter the name of a student: ")

if student in grades:
    print(f"{student}'s grade is {grades[student]}")
else:
    print(f"{student} was not found")

email = "JackFake@gmail.com"

if "@" in email and "." in email:
    print("Valid Email")
else:("Invaild Email")