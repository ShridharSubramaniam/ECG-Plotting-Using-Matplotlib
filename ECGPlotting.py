
import serial
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ser = serial.Serial('COM5', 9600)

fig.show()
x=[]
i=0
noOfInputs=10000
xLimit= 100
freq = 5

limitMax = 40
limitMin = 35

fig.canvas.draw()
for i in range(noOfInputs):

    for a in range(freq):
        numeric_data = int(ser.readline().strip())
        print(numeric_data)
        x.append(numeric_data)


    if(len(x)< xLimit):
        print(len(x))
        plot = x
    else:
        x = x[len(x)-xLimit: ]
        plot = x

    ax.clear()
    if plot[-1] in range(limitMin, limitMax):
        col = 'green'
        bgCol = 'white'
    else:
        col = 'red'
        bgCol = 'pink'
    ax.plot(plot, color=col)
    ax.set_facecolor(bgCol)
    ax.set_xlabel("Time")
    ax.set_ylabel("Electrical Signals of Heart (V)")
    plt.pause(0.000000001)
