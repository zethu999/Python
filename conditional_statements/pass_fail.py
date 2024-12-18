"""Check if a student has passed or failed by taking marks in 3 subjects"""

subject_1 = int(input("Enter marks in subject 1: "))
subject_2 = int(input("Enter marks in subject 2: "))
subject_3 = int(input("Enter marks in subject 3: "))

if(subject_1 >= 50 and subject_2 >= 50 and subject_3 >= 50):
    print("Pass")
else:
    print("Fail")
