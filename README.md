# GreetUser# Python I/O Assessment

## Assignment Overview

In this exercise, you will implement a function that generates a greeting message. Your task is to complete the `greet_user` function in the `main.py` file.

## Task Description

You need to implement the `greet_user` function to return a greeting message in the format: `Hello, <name>!`. The function should handle different cases, including when the `name` is an empty string.

### Instructions

1. **Open the Assignment in GitHub Codespaces**

   Open this repository in GitHub Codespaces by clicking the green "Code" button at the top right of this page and selecting "Open with Codespaces."

2. **Implement the Function**

   In Codespaces, open the `main.py` file and complete the `greet_user` function. Ensure that the function:
   - Takes a single argument, `name`, which is a string.
   - Returns a string in the format: `Hello, <name>!`

   For example:
   - `greet_user("John")` should return `"Hello, John!"`
   - `greet_user("")` should return `"Hello, !"`

   Here’s the skeleton code you need to complete:

   ```python
   # main.py

   def greet_user(name):
       # TODO: return a greeting string "Hello, <name>!"
       pass

   if __name__ == "__main__":
       name = input("Enter your name: ")
       print(greet_user(name))
