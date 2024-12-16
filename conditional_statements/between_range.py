"""Check if marks of a subject are within range 0-100"""

marks = int(input("Enter marks: "))

if(marks >= 0 and marks <= 100):
    print("In b/w 0-100")
else:
    print("Not in b/w 0-100")
