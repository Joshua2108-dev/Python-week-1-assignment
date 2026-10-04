# conditions in phython
# if statement/condition

User_age = 23

if User_age >= 18:
    print("you are allowed to vote")

# if /Else
if User_age >= 18:
    print("Go ahead and ast your vote")
else:
    print("Goooo back to school")


# if/Elif/Else condition statement
score = int(input("Enter student marks"))
if score >= 90:
    grade = "A"
elif  score >= 80:
    grade = "B"
elif  score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "failed!"

print(f"(the grade is{grade})")