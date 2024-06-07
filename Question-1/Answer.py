tcand = 10
ncand = int(input("Entert the sold Candles:"))

if ncand in range(1,6):
    print("NCAND sold:",ncand)
    print("NCAND left:",tcand-ncand)
else:
    print("INVALID INPUT")
    print("NCAND left:",tcand)