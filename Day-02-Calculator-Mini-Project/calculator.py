print("Welcome to calculator application...")
first = float(input("Enter the first number: "))


print("Select any one opeartor: ")
ope = input(" Enter the operator/symbol: ")

'''
#using match case
match(ope):
    case "+":
        second= float(input("Enter the second number: "))
        print(first+second)
    case "-":
         second= float(input("Enter the second number: "))
         print(first-second)
    case "*":
          second= float(input("Enter the second number: "))
          print(first * second)
    case "/":
           second= float(input("Enter the second number: "))
           print(first/second)
           
 '''                            
#using if elif 
if(ope== "+"):
           second= float(input("Enter the second number: "))
           print(first + second)
          
elif(ope== "-"):
           second= float(input("Enter the second number: "))
           print(first - second)        
            
elif(ope== "*"):
               second= float(input("Enter the second number: "))
               print(first * second)
          
elif(ope == "/"):
               second= float(input("Enter the second number: "))
               print(first / second)          
               Day 02 calculator mini project added