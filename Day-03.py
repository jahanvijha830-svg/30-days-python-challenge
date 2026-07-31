def safe_divide(a,b):
    try:
        result = a / b

    except ZeroDivisionError:
        print("Can not Divide by zero!")
        return "Can not Divide by zero!"

    else:
        print("Division successful")
        return result

    finally:
        print("Operation complete")


print(safe_divide(10,0))
print(safe_divide(10,1))
print(safe_divide(10,2))



