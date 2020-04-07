# put your python code here
year = int(input())

if 1900 <= year <= 3000:
    leap = ((year % 4) == 0) and (((year % 100) != 0) or ((year % 400) == 0))
    if leap:
        print("Leap")
    else:
        print("Ordinary")
