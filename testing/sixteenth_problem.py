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
        password.append(random.choice(weak_list))
        password.append(random.choice(weak_list))
        password.append(random.choice(weak_list))
        password.append(random.choice(weak_list))
        password.append(random.choice(weak_list))
        password.append(random.choice(weak_list))
        return "".join(password)
    elif user_input == 2:
        password.append(random.choice(average_list))
        password.append(random.choice(average_list))
        password.append(random.choice(average_list))
        password.append(random.choice(average_list))
        password.append(random.choice(average_list))
        password.append(random.choice(average_list))
        password.append(random.choice(average_list))
        password.append(random.choice(average_list))
        password.append(random.choice(average_list))
        return "".join(password)
    elif user_input == 3:
        password.append(random.choice(strong_list))
        password.append(random.choice(strong_list))
        password.append(random.choice(strong_list))
        password.append(random.choice(strong_list))
        password.append(random.choice(strong_list))
        password.append(random.choice(strong_list))
        password.append(random.choice(strong_list))
        password.append(random.choice(strong_list))
        password.append(random.choice(strong_list))
        password.append(random.choice(strong_list))
        password.append(random.choice(strong_list))
        password.append(random.choice(strong_list))
        return "".join(password)
    elif user_input == 4:
        password.append(random.choice(exceptional_list))
        password.append(random.choice(exceptional_list))
        password.append(random.choice(exceptional_list))
        password.append(random.choice(exceptional_list))
        password.append(random.choice(exceptional_list))
        password.append(random.choice(exceptional_list))
        password.append(random.choice(exceptional_list))
        password.append(random.choice(exceptional_list))
        password.append(random.choice(exceptional_list))
        password.append(random.choice(exceptional_list))
        password.append(random.choice(exceptional_list))
        password.append(random.choice(exceptional_list))
        password.append(random.choice(exceptional_list))
        password.append(random.choice(exceptional_list))
        password.append(random.choice(exceptional_list))
        return "".join(password)
    else:
        pass
password_generator(4)
