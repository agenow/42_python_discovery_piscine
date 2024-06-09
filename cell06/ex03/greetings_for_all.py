#!/usr/bin/env python3

def greetings(s="noble stranger"):
    print("Hello", s if type(s) == str else "Error! This was not a name.")

greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)
