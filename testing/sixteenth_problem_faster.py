import random
def password_generator(user_input):
    weak_list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o", \
    "p","q","r","s","t","u","v","w","x","y","z"]

    average_list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o", \
    "p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H", \
    "I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

    strong_list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o", \
    "p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H", \
    "I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0", \
    "1","2","3","4","5","6","7","8","9"]

    exceptional_list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n", \
    "o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G", \
    "H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z", \
    "0","1","2","3","4","5","6","7","8","9","!","@","#","$","%","^","&","*","(", \
    ")","-","_","+","=","[","{","]","}",":",";","<",">",",",".","?","/","|"]

    password = []

    if user_input == 1:
        for _ in range(6):
            password.append(random.choice(weak_list))
        print("".join(password))
    elif user_input == 2:
        for _ in range(9):
            password.append(random.choice(average_list))
        print("".join(password))
    elif user_input == 3:
        for _ in range(12):
            password.append(random.choice(strong_list))
        print("".join(password))
    elif user_input == 4:
        for _ in range(15):
            password.append(random.choice(exceptional_list))
        print("".join(password))
    else:
        pass

if __name__ == "__main__":
    password_generator(4)
