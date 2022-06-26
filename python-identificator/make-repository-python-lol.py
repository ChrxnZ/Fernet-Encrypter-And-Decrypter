import math
# by Pulsed#1874
# the most random calculator i made

print("+ For Addition || +f For Float")
print("- For Subtraction || -f For Float")
print("* For Multiplication || *f For Float")
print("/ For Division || /f For Float")
print("Pow For Power || Powf For Float")
choice = str(input("Choose Type Of Calculator (Float Not Supported) : "))




if choice == "+":
    add = int(input("Enter Your Number: "))
    add2 = int(input("Enter The Number You Want To Add To " +str(add) + ": "))
    addansw = add + add2
    print(type(addansw))
    print("Answer Is: " +str(addansw) + "!")
elif choice == "+f":
    add = float(input("Enter Your Number: "))
    add2 = float(input("Enter The Number You Want To Add To " + str(add) + ": "))
    addansw = add + add2
    print(type(addansw))
    print("Answer Is: " + str(addansw) + "!")

elif choice == "-":
    minus = int(input("Enter Your Number: "))
    minus2 = int(input("Enter The Number You Want To Subtract " +str(minus) + " By: "))
    minusansw = minus - minus2
    print(type(minusansw))
    print("Answer Is: " +str(minusansw) + "!")
elif choice == "-f":
    minus = float(input("Enter Your Number: "))
    minus2 = float(input("Enter The Number You Want To Subtract " + str(minus) + " By: "))
    minusansw = minus - minus2
    print(type(minusansw))
    print("Answer Is: " + str(minusansw) + "!")

elif choice == "*":
    multiply = int(input("Enter Your Number: "))
    multiply2 = int(input("Enter The Number You Want To Multiply " +str(multiply) + " By: "))
    multiplyansw = multiply * multiply2
    print(type(multiplyansw))
    print("Answer Is: " +str(multiplyansw) + "!")
elif choice == "*f":
    multiply = float(input("Enter Your Number: "))
    multiply2 = float(input("Enter The Number You Want To Multiply " + str(multiply) + " By: "))
    multiplyansw = multiply * multiply2
    print(type(multiplyansw))
    print("Answer Is: " + str(multiplyansw) + "!")

elif choice == "/":
    divide = int(input("Enter Your Number: "))
    divide2 = int(input("Enter The Number You Want To Divide " +str(divide) + " By: "))
    divideansw = divide / divide2
    print(type(divideansw))
    print("Answer Is: " +str(divideansw) + "!")
elif choice == "/f":
    divide = float(input("Enter Your Number: "))
    divide2 = float(input("Enter The Number You Want To Divide " + str(divide) + " By: "))
    divideansw = divide / divide2
    print(type(divideansw))
    print("Answer Is: " + str(divideansw) + "!")

elif choice == "Pow" or choice == "pow":
    pow1 = int(input("Enter Your Number: "))
    pow2 = int(input("Enter How Many Times You Want To Multiply " +str(pow1) + " By Itself: "))
    print(type(pow1))
    print("Answer Is: ")
    print(pow(pow1,pow2))
elif choice == "Powf" or choice == "PowF" or choice == "powF" or choice == "powf":
    pow1 = float(input("Enter Your Number: "))
    pow2 = float(input("Enter How Many Times You Want To Multiply " + str(pow1) + " By Itself: "))
    print(type(pow1))
    print("Answer Is: ")
    print(pow(pow1, pow2))
    
else:
    print("Unexpected Response.")
    print("Note That Only Int And Float Values Can Be Entered")



