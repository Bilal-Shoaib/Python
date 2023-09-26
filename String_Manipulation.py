def string_manipulation():
    index, count, character, first_name, roll_number = 0, 0, '', '', ''
    email = input("Enter the E-mail Address: ")
    #email = "bilal:202236@gmail.com"
    while character != ":":
        character = email[index:index+1]
        index += 1
    while character != "@":
        character = email[count:count+1]
        count += 1
    first_name = email[0:index - 1].capitalize()
    roll_number = email[index:count - 1]
    print("First Name is: "+first_name, "\nRoll Number is: "+roll_number)
