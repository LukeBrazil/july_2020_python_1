Celsius = int(input("Enter temperature in Celcuis: "))

def tempConverter(Cel):
    Fahrenheit = Cel * 1.8 + 32
    print("The conversion from Celsius to Fahrenheit = " + str(Fahrenheit))

tempConverter(Celsius)