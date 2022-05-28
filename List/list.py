our_fav_number= 10
user_guess = input("Enter your guess: ")
print(type(user_guess))
user_guess = int(user_guess)
print(type(user_guess))
if user_guess == our_fav_number:
    print("success, you guessed the number: OUr favourite number is: "+ str(our_fav_number))