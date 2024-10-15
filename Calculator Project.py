# Initialize Answer globally
Answer = 0

# Addition Function
def Addition():
    Math = int(input("How many Variables would you like to add together? "))
    numberList = []
    i = 1
    VarNumber = Math
    while Math > 0:
        Number = float(input("Input the value of variable number '" + str(i) + "': "))
        numberList.append(Number)
        i += 1
        Math -= 1

    Answer = 0  # Initialize Answer for Addition

    # Summing the variables in reverse order (last added first)
    while VarNumber > 0:
        VarNumber -= 1
        Answer += numberList[VarNumber]
        
    return Answer  # Return the computed Answer

# Subtraction Function
def Sub():
    Math = int(input("How many Variables would you like to subtract together? \nREMINDER: ORDER MATTERS! "))
    numberList = []
    i = 1
    VarNumber = Math
    while Math > 0:
        Number = float(input("Input the value of variable number '" + str(i) + "': "))
        numberList.append(Number)
        i += 1
        Math -= 1
    
    Answer = numberList[0]  # Start with the first number (subtraction depends on order)
    j = VarNumber

    # Subtract each subsequent number from the first
    for i in range(1, j):
        Answer -= numberList[i]

    return Answer  # Return the computed Answer

# Multiplication Function
def mult():
    Math = int(input("How many Variables would you like to multiply together? "))
    numberList = []
    i = 1
    VarNumber = Math

    while Math > 0:
        Number = float(input("Input the value of variable number '" + str(i) + "': "))
        numberList.append(Number)
        i += 1
        Math -= 1

    Answer = 1  # Initialize Answer for Multiplication

    # Multiply all values in the list
    for num in numberList:
        Answer *= num
        
    return Answer  # Return the computed Answer

# Division Function
def div():
    Math = int(input("How many Variables would you like to divide together? \nREMINDER: ORDER MATTERS! "))
    numberList = []
    i = 1
    VarNumber = Math

    while Math > 0:
        Number = float(input("Input the value of variable number '" + str(i) + "': "))
        if Number != 0:  # Check for zero division
            numberList.append(Number)
            i += 1
            Math -= 1
        else:
            print("Can't divide by zero dummy")

    Answer = numberList[0]  # Start with the first number

    # Perform division, making sure to avoid zero division errors
    for j in range(1, VarNumber):
        if numberList[j] == 0:
            print("Error: Division by zero!")
            return None
        Answer /= numberList[j]
        
    return Answer  # Return the computed Answer


# Main program logic to choose the math operation
MathVar = str(input("Enter the Math you'd like to do \nOption 1: Addition (+) \nOption 2: Subtraction (-) \nOption 3: Multiplication (x) \nOption 4: Division (/) \n")).lower()

# Set Answer based on the selected operation
if MathVar == "+" or MathVar == "1" or MathVar == "addition":
    Answer = Addition()  # Store the result in the global Answer variable
elif MathVar == "-" or MathVar == "2" or MathVar == "subtraction":
    Answer = Sub()
elif MathVar == "x" or MathVar == "3" or MathVar == "multiplication":
    Answer = mult()
elif MathVar == "/" or MathVar == "4" or MathVar == "division":
    Answer = div()

# Check if Answer is valid (not None) before proceeding to rounding
if Answer is not None:
    Round = str(input("Would you like to round? (y/n): ")).lower()
    if Round == "y":
        Value = int(input("How many digits after the decimal?: "))  # No need for .lower() on an int
        NewMathVar = round(Answer, Value)  # Round the Answer to specified decimals
        print(f"Rounded Result: {NewMathVar}")
    else:
        print(f"Result: {Answer}")  # Print the raw Answer if rounding is not requested
