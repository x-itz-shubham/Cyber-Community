def check_password_strength(password):
    special_chars = list("@#$%&*")
    isdigit_there = any(char.isdigit() for char in password)
    isupper_there = any(char.isupper() for char in password)
    isspchar_there = any(char.isdigit() for char in password)
    check_lower = any(char.islower() for char in password)
    all_true = all([isdigit_there, isupper_there, isspchar_there, check_lower])
    if len(password) < 6:
        print("weak")
    elif len(password) >= 8 and all_true:
        print("strong")
    else:
        print("Average")
input_password= input("create password:")
strength=check_password_strength(input_password)
print("")
