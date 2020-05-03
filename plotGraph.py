import matplotlib.pyplot as plt
import csv
import os

print("Available files")

print()

k = 1

for i in os.listdir():
    if i.endswith(".csv"):
        print(str(k)+"."+" ",end="")
        k+=1
        print(i[:-4])

print()

a = input("input file name(Example: 2019-9-09_123456): ").strip()
i = 1

if os.path.exists(os.path.dirname(os.path.realpath(__file__))+"\\"+a+".csv"):

    ms = []
    vin = []
    temp_mos = []
    motorCurrent = []
    batteryCurrent = []
    kmph = []

    secStart = 0
    

    data = csv.DictReader(open(a+".csv"),delimiter=";")

    for row in data:
        ms.append(((int(row["ms_today"]))/1000)-secStart)

        if i:
            secStart = ms[0]
            ms[0] = 0
            i = 0
        
        vin.append(float(row["input_voltage"]))
        temp_mos.append(float(row["temp_mos_max"]))
        motorCurrent.append(float(row["current_motor"]))
        batteryCurrent.append(float(row["current_in"]))
        kmph.append(((int(row["erpm"])/7)/2.4)*0.0182845)
        

    plt.plot(ms,vin,label="V Battery")
    plt.plot(ms,temp_mos,label="Mosfet Temp")
    plt.plot(ms,motorCurrent,label="Motor Current")
    plt.plot(ms,batteryCurrent,label="Battery Current")
    plt.plot(ms,kmph,label="Km/H")

    plt.legend()
    plt.show()

else:
    print("File not found")

input("press enter to exit")
