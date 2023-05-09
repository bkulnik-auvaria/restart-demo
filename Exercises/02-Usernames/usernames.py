import random

filename_nouns = "english-nouns.txt"
filename_adjectives = "english-adjectives.txt"


def read_word_list(filename):
    f = open(filename, "r")
    content = f.read()
    f.close()
    words = content.split("\n")
    return words


def random_username(noun_list, adjective_list):
    x = random.randint(0, len(adjective_list)-1)
    y = random.randint(0, len(noun_list)-1)
    return adjectives[x] + "-" + nouns[y]


nouns = read_word_list(filename_nouns)
adjectives = read_word_list(filename_adjectives)

random_username(nouns, adjectives)


# Generate a random password:
#  For a given length of 'n' select 'n' random characters from some list (the alphabet)

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n = 10

password = ""
for i in range(0, n):
    # i = 0,1,2,.....n-1
    index = random.randint(0, len(alphabet)-1)
    randomCharacter = alphabet[index]  # pick random character
    password = password + randomCharacter  # append it to the password string
    print(f"Password at step i={i}; password={password}")





# Interactive Menu:
#   Do you want a username? [yes/no]: yes
#       This is your username: ....
#   Do you want another username? [yes/no]: no
#       program terminates!

userWantsToQuit = False

while userWantsToQuit == False: # loop as long as the user does not wish to quit

    # ask what the user wants to do
    response = input("Do you want a username? [yes/no]: ")
    
    if response == "yes":
        # if "yes", give the user a username
        user_name = random_username(nouns, adjectives)
        print("This is you username: ", user_name)
    
    elif response == "no":
        # if no, modify the condition so that the loop exits
        print("Goodbye!")
        userWantsToQuit = True

    else:
        # in case we get input that we do understand
        print("I do not understand, please write 'yes' or 'no'")
