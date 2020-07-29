Cel = int(input("Enter temperature in Celcuis: "))

def tempConverter(Cel):
    Farenheit = Cel * 1.8 + 32
    print("The conversion from Celcius to Farenheit = " + str(Farenheit))

tempConverter(Cel)