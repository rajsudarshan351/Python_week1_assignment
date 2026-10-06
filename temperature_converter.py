print("Temperature converter:\n 1. Celsius to Fahrenhiet \n 2. Fahrenheit to Celsius")
choice = input("Enter the choice: ")

def C_to_F(celsius):
    return (celsius * 9/5) + 32
def F_to_C(fahrenheit):
    return(fahrenheit - 32) * 5/9

if choice == "1":
    celsius = float(input("Enter Celsius value: "))
    fahrenheit = C_to_F(celsius)
    print("Temperature in Fahrenheit: ",fahrenheit)
elif choice == "2":
    fahrenheit = float(input("Enter Fahrenheit value: "))   
    celsius = F_to_C(fahrenheit) 
    print("Temperature in Celsius: ",celsius)
else:
    print("please select appropriate choice")
