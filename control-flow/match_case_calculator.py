num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter operation (+/-/*// ): )

match operations:
    case "+":
    result = num1 + num2
        print("The result is [result].")
         case "-":
         result = num1 - num2
         print("The result is [result].")
             case "*":
             result = num1 * num2
             print("The resul is [result].")
                 case "/"
                 result = num1 / num2
                 print("The result is [result].)
                     case _:
                     print("Invalid day entered.")
