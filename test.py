#!/usr/bin/env python3

from datetime import datetime

print(datetime.now())

name = input("Write your name: ")
age = input("Write your age: ")

print("{} is {} years old.".format(name, age))
