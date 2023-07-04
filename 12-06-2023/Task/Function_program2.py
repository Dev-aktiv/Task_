def average_of_num():
    try:
        num1 = int(input("Enter num1"))
        num2 = int(input("Enter num2"))
        num3 = 10
        avg = 0
    except Exception as e:
        print("Here is some exception", e)

    def calculate_sum():
        try:
            avg = num1 + num2 + num3
            print("sum is:",avg)
        except Exception as e:
            print("Exception Accure", e)

        def calculate_average():
            nonlocal avg
            try:
                avg=avg/3
                print("Average is",avg)
            except Exception as e:
                print("Exception Accure",e)
        calculate_average()
    calculate_sum()



average_of_num()
