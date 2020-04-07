'''
def fahrenheit_to_celsius(f):
    return round(((f - 32) * 5 / 9), 3)


f = float(input())
print(fahrenheit_to_celsius(f))
'''

name = "John"


def change_name(new_name):
    global name
    name = new_name


change_name("Mary")
print(name)
