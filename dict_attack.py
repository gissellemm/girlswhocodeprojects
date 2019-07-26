f = open("dictionary.txt","r")

print("Can your password survive a dictionary attack?")
dict_word = ""
#NOTE - You will have to use .strip() to strip whitespace and newlines from the file and passwords
test_password = input("Type in a trial password: ")
for word in f:
    if word.strip() == test_password.strip():
        print("Your password is too weak.")
    else:
        print("Your password is okay.")
