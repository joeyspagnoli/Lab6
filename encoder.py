menu = "Menu\n-------------\n1. Encode\n2. Decode\n3. Quit"
print(menu)
user = input("Please enter an option: ")

def encode(password):
    temp = ''
    for x in password:
        temp += str(int(x) + 3)
    return temp


while(user != 3):
    if(user == '1'):
        password = input("Please enter your password to encode: ")
        password = encode(password)
        print("Your password has been encoded and stored!")


