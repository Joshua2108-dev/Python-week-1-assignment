# Create a python function.
def habari():
    print("Hello, World!")
habari()

# Parameters
def bycircle(make):
    print("the make of my " + make)
bycircle("black member")

def bicycle(make, cost):
    print("the make of the bike is " + make)
bicycle("1000", "sugai")

    # return statement
def grade(score):
    if score >= 70:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 50:
        return "C"
    else:
        return "Failed"
print(grade(64))



