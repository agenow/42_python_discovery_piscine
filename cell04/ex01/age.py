#!/usr/bin/env python3
age = int(input("Please tell me your age: "))
print ("You are currently", age, "years old.")
for i in range(10, 31, 10):
    print ("In", i, "years, you'll be", age+i, "years old.")
