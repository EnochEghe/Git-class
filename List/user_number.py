user_no= input("enter a numbr: ")

try: 
    user_no = float(user_no)
    print("yepee, you entered the correct number")

    if user_no >= 0:
        print("true")

    else:
        print("false")
except:
    print("This is not a number")
"ABC" == "abc"