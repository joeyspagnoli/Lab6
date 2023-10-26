menu = "Menu\n-------------\n1. Encode\n2. Decode\n3. Quit"
print(menu)
user = 0

def encode(password):
    temp = ''
    for x in password:
        temp += str(int(x) + 3)
    return temp


"""decode section coded by Reynaldo Zeledon"""
def decoder(password):   # is the decoder
    temp = ''
    for num in password:
        temp += str(int(num) - 3)
    return temp

while(user != '3'):
    user = input("Please enter an option: ")
    if (user == '1'):
        password = input("Please enter your password to encode: ")
        password = encode(password)
        print("Your password has been encoded and stored!")

    elif (user == '2'):
        print(f'The encoded password is {password}, and the original password is {decoder(password)}')


