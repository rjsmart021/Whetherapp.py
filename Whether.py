#Module 2 Lesson 7: Assignments | Python Exception Handling
#1. Exceptional Weather Forecast
#Task 1: Start Begin by asking the user to enter the temperature in Fahrenheit.
Fahrenheit = float(input("Temperature in Fahrenheit"))
#Task 2: Temperature Conversion Write a function that converts the Fahrenheit temperature to Celsius.
# Remember that the formula is (Fahrenheit - 32) * 5/9
def Fahrenheit_to_Celsius(Fahrenheit):
    Celsius = (Fahrenheit - 32)*5/9
    print(Celsius)
#Task 3: User Experience Implement an else block that prints the converted temperature in a user-friendly format. 
Fahrenheit = float(input("Temperature in Fahrenheit"))
Fahrenheit_to_Celsius(Fahrenheit)
#Task 4: Finally Add a finally block that thanks the user for using the weather forecast application
print("Thank you for using the Whether forecast application!")
#ensuring that this message is displayed regardless of whether an exception was caught or not.
