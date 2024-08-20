# main.py

def greet_user(name):
    # TODO: return a greeting string "Hello, <name>!"
    return "Hello, "+ name

if __name__ == "__main__":
    name = input("Enter your name: ")
    print(greet_user(name))
