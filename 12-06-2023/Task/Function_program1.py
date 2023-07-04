def digit_power():
    try:
        digit = int(input("Enter the Digit:"))
        power = int(input("Enter the Power:"))
        print("Value is:", digit ** power)
    except Exception as e:
        print("Here is some Exception", e)


digit_power()
