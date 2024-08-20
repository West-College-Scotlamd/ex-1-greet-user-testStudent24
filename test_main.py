# test_main.py
import main

def test_greet_user():
    assert main.greet_user("John") == "Hello, John!"
    assert main.greet_user("Jude") == "Hello, Jude!"
    assert main.greet_user("") == "Hello, !"
