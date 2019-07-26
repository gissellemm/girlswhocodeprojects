from random import *

def intro():
    print("Hello, my name is Chatbot!")

def say_greeting():
    print("Hi, i'm Chatbot!")

def default():
    print("That's cool!")

def poem():
    print("Roses are red, Violets are blue, You make the world better, By just being you!")

def process_input(answer_1):
    if answer_1 == "hi":
        say_greeting()
    elif "poem" in answer_1:
        poem()
    else:
        default()

def main():
    intro()
    while True:
        answer = input("(What will you say?)")
        process_input(answer) #use parameters to pass info between functions instead of global variables

if __name__ == "__main__":
    main()
