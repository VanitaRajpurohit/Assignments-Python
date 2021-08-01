i = 1
while i:
  tempC = input("Enter the temperature in celsius:")
  try: 
    tempC = float(tempC)
    i = 0
  except:
    print("Please enter the temperature in numerical format")

tempF = tempC * 9 / 5 + 32

print("Output is: ", tempF)
