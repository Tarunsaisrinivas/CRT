n = int(input("Enter the number between 0 to 7000: "))
if n in range(0, 2000):
    print("25 Min")
elif n in range(2000, 4000):
    print("35 Min")
elif n in range(4000, 7000):  
    print("45 Min")
else:
    print("INVALID INPUT")
