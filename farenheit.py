Celsius = int(input("Enter temperature in Celcuis: "))

def tempConverter(Celsius):
    Fahrenheit = Celsius * 1.8 + 32
    print("The conversion from Celsius to Fahrenheit = " + str(float(Fahrenheit)))

tempConverter(Celsius)