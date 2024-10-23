table = [
    [0, 1, 2],
    [1, 1, 3],
    [2, 3, 2],
    [3, 3, 3] 
]

print("Password must contain at least 1 special character, 1 number, and a minimum of 8 characters.")
newPass = input("Create password: ")

def specialChar(char) -> bool:
    return not char.isalnum() and not char.isspace()

def passwordValidator(password):
    state = 0
    if len(password) < 8:
        return False

    for c in password:
        if c.isalpha():
            state = table[state][0]
        elif c.isnumeric():
            state = table[state][1]
        elif specialChar(c):
            state = table[state][2]
        
        if state == 3:
            return True
    return False

if passwordValidator(newPass):
    print("Password is valid")
else:
    print("Password does not meet all conditions.")
