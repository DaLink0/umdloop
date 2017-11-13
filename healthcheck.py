import tkinter as tk
from tkinter import *
from tkinter import ttk
import random
import socket
import sys

    
def gui():
    root = Tk()

    root.configure(background="#D6C2C2", relief=SUNKEN)
    w,h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (w, h))
    root.title("Health Check")

    root.rowconfigure(0,weight=1)
    root.columnconfigure(0,weight=1)
    main = tk.Frame(root, height = h, width = w, bg="#D6C2C2")

    hold = tk.Label(main)
    hold.grid(row=1,column=8, padx=12,pady=10,columnspan=1)
    hold = tk.Label(main)
    hold.grid(row=1,column=1, padx=9,pady=5,columnspan=1)
    hold = tk.Label(main)
    hold.grid(row=1,column=13, padx=9,pady=10,columnspan=1)
    hold = tk.Label(main)
    hold.grid(row=1,column=19, padx=9,pady=5,columnspan=1)
    hold = tk.Label(main)
    hold.grid(row=40,column=1, padx=12,pady=150,columnspan=1)


    bgimage = PhotoImage(file = "/home/dlinko/Downloads/image6.png")
    # bgimage = bgimage.subsample(2)    
    bglabel = Label(main, image= bgimage,)
    bglabel.place(x=0,y=0, relwidth=1, relheight=1)    
   
    title2= tk.Label(main, text="Min", fg="black", font=("Courier", 22),bg = "#D6C2C2")
    title2.grid(row = 2, column = 3, padx=4, pady=10, columnspan = 1, sticky=N+S+E+W)
    title3= tk.Label(main, text="Actual",fg="black", font=("Courier", 22),bg = "#D6C2C2")
    title3.grid(row = 2, column = 5, padx=4, pady=10, columnspan = 1, sticky=N+S+E+W)
    title4= tk.Label(main, text="Max",fg="black", font=("Courier", 22),bg = "#D6C2C2")
    title4.grid(row = 2, column = 7, padx=4, pady=10, columnspan = 1, sticky=N+S+E+W)
    
    title12= tk.Label(main, text="Min", fg="black", font=("Courier", 22),bg = "#D6C2C2")
    title12.grid(row = 2, column = 10, padx=4, pady=10, columnspan = 1, sticky=N+S+E+W)
    title13= tk.Label(main, text="Actual",fg="black", font=("Courier", 22),bg = "#D6C2C2")
    title13.grid(row = 2, column = 11, padx=4, pady=10, columnspan = 1, sticky=N+S+E+W)
    title14= tk.Label(main, text="Max",fg="black", font=("Courier", 22),bg = "#D6C2C2")
    title14.grid(row = 2, column = 12, padx=4, pady=10, columnspan = 1, sticky=N+S+E+W)

    title12= tk.Label(main, text="Min", fg="black", font=("Courier", 22),bg = "#D6C2C2")
    title12.grid(row = 2, column = 15, padx=4, pady=10, columnspan = 1, sticky=N+S+E+W)
    title13= tk.Label(main, text="Actual",fg="black", font=("Courier", 22),bg = "#D6C2C2")
    title13.grid(row = 2, column = 16, padx=4, pady=10, columnspan = 1, sticky=N+S+E+W)
    title14= tk.Label(main, text="Max",fg="black", font=("Courier", 22),bg = "#D6C2C2")
    title14.grid(row = 2, column = 17, padx=4, pady=10, columnspan = 1, sticky=N+S+E+W)

    title1= tk.Label(main, text="HEALTH CHECK", fg="black", font=("Courier", 22),bg = "#D6C2C2")
    title1.place(x=int(w/2),y=0, anchor="n")


    # batteries
    titleBat= tk.Label(main, text="BATTERIES", fg="black", font=("Courier", 18),bg = "#D6C2C2")
    titleBat.grid(row = 2, column = 2, padx=4, pady=10, columnspan = 1, sticky=N+S+E+W)

    # P Bat volt
    batVolt1= tk.Label(main, text="P Bat 1 Volt",fg="black", font=("Courier", 12), bg="#D6C2C2", relief=SUNKEN)
    batVolt1.grid(row = 3, column = 2, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)
    batVolt1Min= tk.Label(main, text=20.0,fg="black", font=("Courier", 12), bg="#D6C2C2", relief=SUNKEN)
    batVolt1Min.grid(row = 3, column = 3, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)
    batVolt1Max= tk.Label(main, text=28.0,fg="black", font=("Courier", 12), bg="#D6C2C2", relief=SUNKEN)
    batVolt1Max.grid(row = 3, column = 7, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)

    batVolt1Actual= tk.Label(main, text="TEST",fg="black", font=("Courier", 12, 'bold'), bg="red", relief=SUNKEN)
    batVolt1Actual.grid(row = 3, column = 5, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)   
    def updateBat1Volt(actual):
        bg="lightgreen"
        if actual <= 20.0 or actual >= 28.0:
            bg="red"

        batVolt1Actual.config(text=actual, bg = bg)

    batVolt2= tk.Label(main, text="P Bat 2 Volt",fg="black", font=("Courier", 12), bg="#D6C2C2", relief=SUNKEN)
    batVolt2.grid(row = 4, column = 2, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)
    batVolt2Min= tk.Label(main, text=20.0,fg="black", font=("Courier", 12), bg="#D6C2C2", relief=SUNKEN)
    batVolt2Min.grid(row = 4, column = 3, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)
    batVolt2Max= tk.Label(main, text=28.0,fg="black", font=("Courier", 12), bg="#D6C2C2", relief=SUNKEN)
    batVolt2Max.grid(row = 4, column = 7, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)

    batVolt2Actual= tk.Label(main, text="0.0",fg="black", font=("Courier", 12, 'bold'), bg="red", relief=SUNKEN)
    batVolt2Actual.grid(row = 4, column = 5, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)   
    def updateBat2Volt(actual):
        bg="lightgreen"
        if actual <= 20.0 or actual >= 28.0:
            bg="red"

        batVolt2Actual.config(text=actual, bg = bg)
    
    batVoltRes= tk.Label(main, text="R Bat Volt",fg="black", font=("Courier", 12), bg="#D6C2C2", relief=SUNKEN)
    batVoltRes.grid(row = 6, column = 2, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)
    batVoltResMin= tk.Label(main, text=20.0,fg="black", font=("Courier", 12), bg="#D6C2C2", relief=SUNKEN)
    batVoltResMin.grid(row = 6, column = 3, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)
    batVoltResMax= tk.Label(main, text=28.0,fg="black", font=("Courier", 12), bg="#D6C2C2", relief=SUNKEN)
    batVoltResMax.grid(row = 6, column = 7, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)
    batVoltResActual= tk.Label(main, text="0.0",fg="black", font=("Courier", 12, 'bold'), bg="red", relief=SUNKEN)
    batVoltResActual.grid(row = 6, column = 5, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)   

    def updateBatResVolt(actual):
        bg="lightgreen"
        if actual <= 20.0 or actual >= 28.0:
            bg="red"

        batVoltResActual.config(text=actual, bg = bg)


    batCur1= tk.Label(main, text="P Bat 1 Current",fg="black", font=("Courier", 12), bg="#D6C2C2", relief=SUNKEN)
    batCur1.grid(row = 8, column = 2, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)
    batCur1Min= tk.Label(main, text=2518.73,fg="black", font=("Courier", 12), bg="#D6C2C2", relief=SUNKEN)
    batCur1Min.grid(row = 8, column = 3, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)
    batCur1Max= tk.Label(main, text=5302.46,fg="black", font=("Courier", 12), bg="#D6C2C2", relief=SUNKEN)
    batCur1Max.grid(row = 8, column = 7, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)
    batCur1Actual= tk.Label(main, text="0.0",fg="black", font=("Courier", 12, 'bold'), bg="red", relief=SUNKEN)
    batCur1Actual.grid(row = 8, column = 5, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)   
    
    def updateBatCur1(actual):
        bg="lightgreen"
        if actual <= 2518.46 or actual >= 5302.46:
            bg="red"

        batCur1Actual.config(text=actual, bg = bg)


    batCur2= tk.Label(main, text="P Bat 2 Current",fg="black", font=("Courier", 12), bg="#D6C2C2", relief=SUNKEN)
    batCur2.grid(row = 10, column = 2, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)
    batCur2Min= tk.Label(main, text=2518.73,fg="black", font=("Courier", 12), bg="#D6C2C2", relief=SUNKEN)
    batCur2Min.grid(row = 10, column = 3, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)
    batCur2Max= tk.Label(main, text=5302.46,fg="black", font=("Courier", 12), bg="#D6C2C2", relief=SUNKEN)
    batCur2Max.grid(row = 10, column = 7, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)
    batCur2Actual= tk.Label(main, text="0.0",fg="black", font=("Courier", 12, 'bold'), bg="red", relief=SUNKEN)
    batCur2Actual.grid(row = 10, column = 5, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)   

    def updateBatCur2(actual):
        bg="lightgreen"
        if actual <= 2518.46 or actual >= 5302.46:
            bg="red"

        batCur2Actual.config(text=actual, bg = bg)


    batCurRes= tk.Label(main, text="R Bat Current",fg="black", font=("Courier", 12), bg="#D6C2C2", relief=SUNKEN)
    batCurRes.grid(row = 12, column = 2, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)
    batCurResMin= tk.Label(main, text=0.0,fg="black", font=("Courier", 12), bg="#D6C2C2", relief=SUNKEN)
    batCurResMin.grid(row = 12, column = 3, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)   
    batCurResMax= tk.Label(main, text=5302.46,fg="black", font=("Courier", 12), bg="#D6C2C2", relief=SUNKEN)
    batCurResMax.grid(row = 12, column = 7, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)
    batCurResActual= tk.Label(main, text="0.0",fg="black", font=("Courier", 12, 'bold'), bg="red", relief=SUNKEN)
    batCurResActual.grid(row = 12, column = 5, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)

    def updateBatCurRes(actual):
        bg="lightgreen"
        if actual <= 0.0 or actual >= 5302.46:
            bg="red"

        batCurResActual.config(text=actual, bg = bg)

    batTemp1= tk.Label(main, text="P Bat 1 Temp ",fg="black", font=("Courier", 12), bg="#D6C2C2", relief=SUNKEN)
    batTemp1.grid(row = 14, column = 2, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)
    batTemp1Min= tk.Label(main, text=77,fg="black", font=("Courier", 12), bg="#D6C2C2", relief=SUNKEN)
    batTemp1Min.grid(row = 14, column = 3, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)   
    batTemp1Max= tk.Label(main, text=140,fg="black", font=("Courier", 12), bg="#D6C2C2", relief=SUNKEN)
    batTemp1Max.grid(row = 14, column = 7, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)
    batTemp1Actual= tk.Label(main, text="0.0",fg="black", font=("Courier", 12, 'bold'), bg="red", relief=SUNKEN)
    batTemp1Actual.grid(row = 14, column = 5, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)

    def updateBatTemp1(actual):
        bg="lightgreen"
        if actual <= 77 or actual >= 140:
            bg="red"

        batTemp1Actual.config(text=actual, bg = bg)

    batTemp2= tk.Label(main, text="P Bat 2 Temp ",fg="black", font=("Courier", 12), bg="#D6C2C2", relief=SUNKEN)
    batTemp2.grid(row = 16, column = 2, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)
    batTemp2Min= tk.Label(main, text=77,fg="black", font=("Courier", 12), bg="#D6C2C2", relief=SUNKEN)
    batTemp2Min.grid(row = 16, column = 3, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)   
    batTemp2Max= tk.Label(main, text=140,fg="black", font=("Courier", 12), bg="#D6C2C2", relief=SUNKEN)
    batTemp2Max.grid(row = 16, column = 7, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)
    batTemp2Actual= tk.Label(main, text="0.0",fg="black", font=("Courier", 12, 'bold'), bg="red", relief=SUNKEN)
    batTemp2Actual.grid(row = 16, column = 5, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)

    def updateBatTemp2(actual):
        bg="lightgreen"
        if actual <= 77 or actual >= 140:
            bg="red"

        batTemp2Actual.config(text=actual, bg = bg)

    batTempRes= tk.Label(main, text="R Bat Temp ",fg="black", font=("Courier", 12), bg="#D6C2C2", relief=SUNKEN)
    batTempRes.grid(row = 18, column = 2, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)
    batTempResMin= tk.Label(main, text=77,fg="black", font=("Courier", 12), bg="#D6C2C2", relief=SUNKEN)
    batTempResMin.grid(row = 18, column = 3, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)   
    batTempResMax= tk.Label(main, text=140,fg="black", font=("Courier", 12), bg="#D6C2C2", relief=SUNKEN)
    batTempResMax.grid(row = 18, column = 7, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)
    batTempResActual= tk.Label(main, text="0.0",fg="black", font=("Courier", 12, 'bold'), bg="red", relief=SUNKEN)
    batTempResActual.grid(row = 18, column = 5, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)

    def updateBatTempRes(actual):
        bg="lightgreen"
        if actual <= 77 or actual >= 140:
            bg="red"

        batTempResActual.config(text=actual, bg = bg)

    # sensors
    title2= tk.Label(main, text="SENSORS", fg="black", font=("Courier", 18),bg = "#D6C2C2")
    title2.grid(row = 2, column = 9, padx=4, pady=10, columnspan = 1, sticky=N+S+E+W)


    levFront= tk.Label(main, text="Leviation front",fg="black", font=("Courier", 12), bg="#D6C2C2", relief=SUNKEN)
    levFront.grid(row = 4, column = 9, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)
    levFrontMin= tk.Label(main, text=0.0,fg="black", font=("Courier", 12), bg="#D6C2C2", relief=SUNKEN)
    levFrontMin.grid(row = 4, column = 10, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)   
    levFrontMax= tk.Label(main, text=0.0,fg="black", font=("Courier", 12), bg="#D6C2C2", relief=SUNKEN)
    levFrontMax.grid(row = 4, column = 12, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)
    levFrontActual= tk.Label(main, text="0.0",fg="black", font=("Courier", 12, 'bold'), bg="red", relief=SUNKEN)
    levFrontActual.grid(row = 4, column = 11, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)

    def updateLevFront(actual):
        bg="lightgreen"
        if actual <= 0.0 or actual >= 1200:
            bg="red"

        levFrontActual.config(text=actual, bg = bg)


    levBack= tk.Label(main, text="Levation back",fg="black", font=("Courier", 12), bg="#D6C2C2", relief=SUNKEN)
    levBack.grid(row = 6, column = 9, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)
    levBackMin= tk.Label(main, text=0.0,fg="black", font=("Courier", 12), bg="#D6C2C2", relief=SUNKEN)
    levBackMin.grid(row = 6, column = 10, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)   
    levBackMax= tk.Label(main, text=0.0,fg="black", font=("Courier", 12), bg="#D6C2C2", relief=SUNKEN)
    levBackMax.grid(row = 6, column = 12, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)
    levBackActual= tk.Label(main, text="0.0",fg="black", font=("Courier", 12, 'bold'), bg="red", relief=SUNKEN)
    levBackActual.grid(row = 6, column = 11, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)

    def updateLevBack(actual):
        bg="lightgreen"
        if actual <= 0.0 or actual >= 1200:
            bg="red"

        levBackActual.config(text=actual, bg = bg)


    podTemp= tk.Label(main, text="Pod Temp",fg="black", font=("Courier", 12), bg="#D6C2C2", relief=SUNKEN)
    podTemp.grid(row = 8, column = 9, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)
    podTempMin= tk.Label(main, text=77,fg="black", font=("Courier", 12), bg="#D6C2C2", relief=SUNKEN)
    podTempMin.grid(row = 8, column = 10, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)   
    podTempMax= tk.Label(main, text=150,fg="black", font=("Courier", 12), bg="#D6C2C2", relief=SUNKEN)
    podTempMax.grid(row = 8, column = 12, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)
    podTempActual= tk.Label(main, text="0.0",fg="black", font=("Courier", 12, 'bold'), bg="red", relief=SUNKEN)
    podTempActual.grid(row = 8, column = 11, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)

    def updatePodTemp(actual):
        bg="lightgreen"
        if actual <= 77 or actual >= 150:
            bg="red"

        podTempActual.config(text=actual, bg = bg)


    accelX= tk.Label(main, text="accel X",fg="black", font=("Courier", 12), bg="#D6C2C2", relief=SUNKEN)
    accelX.grid(row = 10, column = 9, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)
    accelXMin= tk.Label(main, text=-3,fg="black", font=("Courier", 12), bg="#D6C2C2", relief=SUNKEN)
    accelXMin.grid(row = 10, column = 10, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)   
    accelXMax= tk.Label(main, text=3,fg="black", font=("Courier", 12), bg="#D6C2C2", relief=SUNKEN)
    accelXMax.grid(row = 10, column = 12, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)
    accelXActual= tk.Label(main, text="0.0",fg="black", font=("Courier", 12, 'bold'), bg="red", relief=SUNKEN)
    accelXActual.grid(row = 10, column = 11, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)

    def updateAccelX(actual):
        bg="lightgreen"
        if actual <= -3 or actual >= 3:
            bg="red"

        accelXActual.config(text=actual, bg = bg)

    accelY= tk.Label(main, text="accel Y",fg="black", font=("Courier", 12), bg="#D6C2C2", relief=SUNKEN)
    accelY.grid(row = 12, column = 9, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)
    accelYMin= tk.Label(main, text=-3,fg="black", font=("Courier", 12), bg="#D6C2C2", relief=SUNKEN)
    accelYMin.grid(row = 12, column = 10, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)   
    accelYMax= tk.Label(main, text=3,fg="black", font=("Courier", 12), bg="#D6C2C2", relief=SUNKEN)
    accelYMax.grid(row = 12, column = 12, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)
    accelYActual= tk.Label(main, text="0.0",fg="black", font=("Courier", 12, 'bold'), bg="red", relief=SUNKEN)
    accelYActual.grid(row = 12, column = 11, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)

    def updateAccelY(actual):
        bg="lightgreen"
        if actual <= -3 or actual >= 3:
            bg="red"

        accelYActual.config(text=actual, bg = bg)


    accelZ= tk.Label(main, text="accel Z",fg="black", font=("Courier", 12), bg="#D6C2C2", relief=SUNKEN)
    accelZ.grid(row = 14, column = 9, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)
    accelZMin= tk.Label(main, text=-3,fg="black", font=("Courier", 12), bg="#D6C2C2", relief=SUNKEN)
    accelZMin.grid(row = 14, column = 10, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)   
    accelZMax= tk.Label(main, text=3,fg="black", font=("Courier", 12), bg="#D6C2C2", relief=SUNKEN)
    accelZMax.grid(row = 14, column = 12, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)
    accelZActual= tk.Label(main, text="0.0",fg="black", font=("Courier", 12, 'bold'), bg="red", relief=SUNKEN)
    accelZActual.grid(row = 14, column = 11, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)

    def updateAccelZ(actual):
        bg="lightgreen"
        if actual <= -3 or actual >= 3:
            bg="red"

        accelZActual.config(text=actual, bg = bg)
    

    pressure= tk.Label(main, text="Pressure",fg="black", font=("Courier", 12), bg="#D6C2C2", relief=SUNKEN)
    pressure.grid(row = 3, column = 9, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)
    pressureMin= tk.Label(main, text=0.125,fg="black", font=("Courier", 12), bg="#D6C2C2", relief=SUNKEN)
    pressureMin.grid(row = 3, column = 10, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)   
    pressureMax= tk.Label(main, text=14.7,fg="black", font=("Courier", 12), bg="#D6C2C2", relief=SUNKEN)
    pressureMax.grid(row = 3, column = 12, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)
    pressureActual= tk.Label(main, text="0.0",fg="black", font=("Courier", 12, 'bold'), bg="red", relief=SUNKEN)
    pressureActual.grid(row = 3, column = 11, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)

    def updatePressure(actual):
        bg="lightgreen"
        if actual <= 0.125 or actual >= 14.7:
            bg="red"

        pressureActual.config(text=actual, bg = bg)

    # LIM Sensors
    titleLimSen= tk.Label(main, text="Lim Sen", fg="black", font=("Courier", 18),bg = "#D6C2C2")
    titleLimSen.grid(row = 2, column = 14, padx=4, pady=10, columnspan = 1, sticky=N+S+E+W)

    # Motor 1 temp
    mot1Temp= tk.Label(main, text="Motor 1 Temp",fg="black", font=("Courier", 12), bg="#D6C2C2", relief=SUNKEN)
    mot1Temp.grid(row = 3, column = 14, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)
    mot1TempMin= tk.Label(main, text=77,fg="black", font=("Courier", 12), bg="#D6C2C2", relief=SUNKEN)
    mot1TempMin.grid(row = 3, column = 15, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)
    mot1TempMax= tk.Label(main, text=28.0,fg="black", font=("Courier", 12), bg="#D6C2C2", relief=SUNKEN)
    mot1TempMax.grid(row = 3, column = 17, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)
    mot1TempActual= tk.Label(main, text="0.0",fg="black", font=("Courier", 12, 'bold'), bg="red", relief=SUNKEN)
    mot1TempActual.grid(row = 3, column = 16, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)   

    def updateMot1Temp(actual):
        bg="lightgreen"
        if actual <= 77 or actual >= 28.0:
            bg="red"

        mot1TempActual.config(text=actual, bg = bg)

    # Motor 2 temp
    mot2Temp= tk.Label(main, text="Motor 2 Temp",fg="black", font=("Courier", 12), bg="#D6C2C2", relief=SUNKEN)
    mot2Temp.grid(row = 4, column = 14, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)
    mot2TempMin= tk.Label(main, text=77,fg="black", font=("Courier", 12), bg="#D6C2C2", relief=SUNKEN)
    mot2TempMin.grid(row = 4, column = 15, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)
    mot2TempMax= tk.Label(main, text=302,fg="black", font=("Courier", 12), bg="#D6C2C2", relief=SUNKEN)
    mot2TempMax.grid(row = 4, column = 17, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)
    mot2TempActual= tk.Label(main, text="0.0",fg="black", font=("Courier", 12, 'bold'), bg="red", relief=SUNKEN)
    mot2TempActual.grid(row = 4, column = 16, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)   

    def updateMot2Temp(actual):
        bg="lightgreen"
        if actual <= 77 or actual >= 302:
            bg="red"

        mot2TempActual.config(text=actual, bg = bg)

    # Motor 3 temp
    mot3Temp= tk.Label(main, text="Motor 3 Temp",fg="black", font=("Courier", 12), bg="#D6C2C2", relief=SUNKEN)
    mot3Temp.grid(row = 6, column = 14, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)
    mot3TempMin= tk.Label(main, text=77,fg="black", font=("Courier", 12), bg="#D6C2C2", relief=SUNKEN)
    mot3TempMin.grid(row = 6, column = 15, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)
    mot3TempMax= tk.Label(main, text=302,fg="black", font=("Courier", 12), bg="#D6C2C2", relief=SUNKEN)
    mot3TempMax.grid(row = 6, column = 17, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)
    mot3TempActual= tk.Label(main, text="0.0",fg="black", font=("Courier", 12, 'bold'), bg="red", relief=SUNKEN)
    mot3TempActual.grid(row = 6, column = 16, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)   

    def updateMot3Temp(actual):
        bg="lightgreen"
        if actual <= 77 or actual >= 302:
            bg="red"

        mot3TempActual.config(text=actual, bg = bg)

    # Motor 4 temp
    mot4Temp= tk.Label(main, text="Motor 4 Temp",fg="black", font=("Courier", 12), bg="#D6C2C2", relief=SUNKEN)
    mot4Temp.grid(row = 8, column = 14, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)
    mot4TempMin= tk.Label(main, text=77,fg="black", font=("Courier", 12), bg="#D6C2C2", relief=SUNKEN)
    mot4TempMin.grid(row = 8, column = 15, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)
    mot4TempMax= tk.Label(main, text=302,fg="black", font=("Courier", 12), bg="#D6C2C2", relief=SUNKEN)
    mot4TempMax.grid(row = 8, column = 17, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)
    mot4TempActual= tk.Label(main, text="0.0",fg="black", font=("Courier", 12, 'bold'), bg="red", relief=SUNKEN)
    mot4TempActual.grid(row = 8, column = 16, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)   

    def updateMot4Temp(actual):
        bg="lightgreen"
        if actual <= 77 or actual >= 302:
            bg="red"

        mot4TempActual.config(text=actual, bg = bg)

    # IPM 1 tmep
    ipm1Temp= tk.Label(main, text="IPM 1 Temp",fg="black", font=("Courier", 12), bg="#D6C2C2", relief=SUNKEN)
    ipm1Temp.grid(row = 10, column = 14, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)
    ipm1TempMin= tk.Label(main, text=77,fg="black", font=("Courier", 12), bg="#D6C2C2", relief=SUNKEN)
    ipm1TempMin.grid(row = 10, column = 15, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)
    ipm1TempMax= tk.Label(main, text=257,fg="black", font=("Courier", 12), bg="#D6C2C2", relief=SUNKEN)
    ipm1TempMax.grid(row = 10, column = 17, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)
    ipm1TempActual= tk.Label(main, text="0.0",fg="black", font=("Courier", 12, 'bold'), bg="red", relief=SUNKEN)
    ipm1TempActual.grid(row = 10, column = 16, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)   

    def updateIpm1Temp(actual):
        bg="lightgreen"
        if actual <= 77 or actual >= 257:
            bg="red"

        ipm1TempActual.config(text=actual, bg = bg)


    # IPM 2 Temp
    ipm2Temp= tk.Label(main, text="IPM 2 Temp",fg="black", font=("Courier", 12), bg="#D6C2C2", relief=SUNKEN)
    ipm2Temp.grid(row = 12, column = 14, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)
    ipm2TempMin= tk.Label(main, text=77,fg="black", font=("Courier", 12), bg="#D6C2C2", relief=SUNKEN)
    ipm2TempMin.grid(row = 12, column = 15, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)
    ipm2TempMax= tk.Label(main, text=257,fg="black", font=("Courier", 12), bg="#D6C2C2", relief=SUNKEN)
    ipm2TempMax.grid(row = 12, column = 17, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)
    ipm2TempActual= tk.Label(main, text="0.0",fg="black", font=("Courier", 12, 'bold'), bg="red", relief=SUNKEN)
    ipm2TempActual.grid(row = 12, column = 16, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)   

    def updateIpm2Temp(actual):
        bg="lightgreen"
        if actual <= 77 or actual >= 257:
            bg="red"

        ipm2TempActual.config(text=actual, bg = bg)

    # IPM 3 Temp
    ipm3Temp= tk.Label(main, text="IPM 3 Temp",fg="black", font=("Courier", 12), bg="#D6C2C2", relief=SUNKEN)
    ipm3Temp.grid(row = 14, column = 14, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)
    ipm3TempMin= tk.Label(main, text=77,fg="black", font=("Courier", 12), bg="#D6C2C2", relief=SUNKEN)
    ipm3TempMin.grid(row = 14, column = 15, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)
    ipm3TempMax= tk.Label(main, text=257,fg="black", font=("Courier", 12), bg="#D6C2C2", relief=SUNKEN)
    ipm3TempMax.grid(row = 14, column = 17, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)
    ipm3TempActual= tk.Label(main, text="0.0",fg="black", font=("Courier", 12, 'bold'), bg="red", relief=SUNKEN)
    ipm3TempActual.grid(row = 14, column = 16, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)   

    def updateIpm3Temp(actual):
        bg="lightgreen"
        if actual <= 77 or actual >= 257:
            bg="red"

        ipm3TempActual.config(text=actual, bg = bg)

    # IPM 4 Temp
    ipm4Temp= tk.Label(main, text="IPM 4 Temp",fg="black", font=("Courier", 12), bg="#D6C2C2", relief=SUNKEN)
    ipm4Temp.grid(row = 16, column = 14, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)
    ipm4TempMin= tk.Label(main, text=77,fg="black", font=("Courier", 12), bg="#D6C2C2", relief=SUNKEN)
    ipm4TempMin.grid(row = 16, column = 15, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)
    ipm4TempMax= tk.Label(main, text=257,fg="black", font=("Courier", 12), bg="#D6C2C2", relief=SUNKEN)
    ipm4TempMax.grid(row = 16, column = 17, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)
    ipm4TempActual= tk.Label(main, text="0.0",fg="black", font=("Courier", 12, 'bold'), bg="red", relief=SUNKEN)
    ipm4TempActual.grid(row = 16, column = 16, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)   

    def updateIpm4Temp(actual):
        bg="lightgreen"
        if actual <= 77 or actual >= 257:
            bg="red"

        ipm4TempActual.config(text=actual, bg = bg)

    # Motor 1 Freq
    motor1Freq= tk.Label(main, text="Motor 1 Freq",fg="black", font=("Courier", 12), bg="#D6C2C2", relief=SUNKEN)
    motor1Freq.grid(row = 18, column = 14, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)
    motor1FreqMin= tk.Label(main, text=20.0,fg="black", font=("Courier", 12), bg="#D6C2C2", relief=SUNKEN)
    motor1FreqMin.grid(row = 18, column = 15, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)
    motor1FreqMax= tk.Label(main, text=28.0,fg="black", font=("Courier", 12), bg="#D6C2C2", relief=SUNKEN)
    motor1FreqMax.grid(row = 18, column = 17, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)
    motor1FreqActual= tk.Label(main, text="0.0",fg="black", font=("Courier", 12, 'bold'), bg="red", relief=SUNKEN)
    motor1FreqActual.grid(row = 18, column = 16, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)   

    def updateMotor1Freq(actual):
        bg="lightgreen"
        if actual <= 20.0 or actual >= 28.0:
            bg="red"

        motor1FreqActual.config(text=actual, bg = bg)

    # Motor 2 Freq
    motor2Freq= tk.Label(main, text="Motor 2 Freq",fg="black", font=("Courier", 12), bg="#D6C2C2", relief=SUNKEN)
    motor2Freq.grid(row = 20, column = 14, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)
    motor2FreqMin= tk.Label(main, text=20.0,fg="black", font=("Courier", 12), bg="#D6C2C2", relief=SUNKEN)
    motor2FreqMin.grid(row = 20, column = 15, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)
    motor2FreqMax= tk.Label(main, text=28.0,fg="black", font=("Courier", 12), bg="#D6C2C2", relief=SUNKEN)
    motor2FreqMax.grid(row = 20, column = 17, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)
    motor2FreqActual= tk.Label(main, text="0.0",fg="black", font=("Courier", 12, 'bold'), bg="red", relief=SUNKEN)
    motor2FreqActual.grid(row = 20, column = 16, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)   

    def updateMotor2Freq(actual):
        bg="lightgreen"
        if actual <= 20.0 or actual >= 28.0:
            bg="red"

        motor1FreqActual.config(text=actual, bg = bg)

    # Motor 3 Freq
    motor3Freq= tk.Label(main, text="Motor 3 Freq",fg="black", font=("Courier", 12), bg="#D6C2C2", relief=SUNKEN)
    motor3Freq.grid(row = 22, column = 14, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)
    motor3FreqMin= tk.Label(main, text=20.0,fg="black", font=("Courier", 12), bg="#D6C2C2", relief=SUNKEN)
    motor3FreqMin.grid(row = 22, column = 15, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)
    motor3FreqMax= tk.Label(main, text=28.0,fg="black", font=("Courier", 12), bg="#D6C2C2", relief=SUNKEN)
    motor3FreqMax.grid(row = 22, column = 17, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)
    motor3FreqActual= tk.Label(main, text="0.0",fg="black", font=("Courier", 12, 'bold'), bg="red", relief=SUNKEN)
    motor3FreqActual.grid(row = 22, column = 16, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)   

    def updateMotor3Freq(actual):
        bg="lightgreen"
        if actual <= 20.0 or actual >= 28.0:
            bg="red"

        motor3FreqActual.config(text=actual, bg = bg)


    # Motor 4 Freq
    motor4Freq= tk.Label(main, text="Motor 4 Freq",fg="black", font=("Courier", 12), bg="#D6C2C2", relief=SUNKEN)
    motor4Freq.grid(row = 24, column = 14, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)
    motor4FreqMin= tk.Label(main, text=20.0,fg="black", font=("Courier", 12), bg="#D6C2C2", relief=SUNKEN)
    motor4FreqMin.grid(row = 24, column = 15, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)
    motor4FreqMax= tk.Label(main, text=28.0,fg="black", font=("Courier", 12), bg="#D6C2C2", relief=SUNKEN)
    motor4FreqMax.grid(row = 24, column = 17, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)
    motor4FreqActual= tk.Label(main, text="0.0",fg="black", font=("Courier", 12, 'bold'), bg="red", relief=SUNKEN)
    motor4FreqActual.grid(row = 24, column = 16, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)   

    def updateMotor4Freq(actual):
        bg="lightgreen"
        if actual <= 20.0 or actual >= 28.0:
            bg="red"

        motor4FreqActual.config(text=actual, bg = bg)


    # Pack Temp
    packTemp= tk.Label(main, text="Pack Temp",fg="black", font=("Courier", 12), bg="#D6C2C2", relief=SUNKEN)
    packTemp.grid(row = 26, column = 14, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)
    packTempMin= tk.Label(main, text=77,fg="black", font=("Courier", 12), bg="#D6C2C2", relief=SUNKEN)
    packTempMin.grid(row = 26, column = 15, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)
    packTempMax= tk.Label(main, text=257,fg="black", font=("Courier", 12), bg="#D6C2C2", relief=SUNKEN)
    packTempMax.grid(row = 26, column = 17, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)
    packTempActual= tk.Label(main, text="0.0",fg="black", font=("Courier", 12, 'bold'), bg="red", relief=SUNKEN)
    packTempActual.grid(row = 26, column = 16, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)   

    def updatePackTemp(actual):
        bg="lightgreen"
        if actual <= 77 or actual >= 257:
            bg="red"

        packTempActual.config(text=actual, bg = bg)


    # Pack voltage
    packVolt= tk.Label(main, text="Pack Volt",fg="black", font=("Courier", 12), bg="#D6C2C2", relief=SUNKEN)
    packVolt.grid(row = 28, column = 14, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)
    packVoltMin= tk.Label(main, text=20.0,fg="black", font=("Courier", 12), bg="#D6C2C2", relief=SUNKEN)
    packVoltMin.grid(row = 28, column = 15, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)
    packVoltMax= tk.Label(main, text=592,fg="black", font=("Courier", 12), bg="#D6C2C2", relief=SUNKEN)
    packVoltMax.grid(row = 28, column = 17, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)
    packVoltActual= tk.Label(main, text="0.0",fg="black", font=("Courier", 12, 'bold'), bg="red", relief=SUNKEN)
    packVoltActual.grid(row = 28, column = 16, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)   

    def updatePackVolt(actual):
        bg="lightgreen"
        if actual <= 20.0 or actual >= 592:
            bg="red"

        packVoltActual.config(text=actual, bg = bg)
    

    # Pack Current
    packCurr= tk.Label(main, text="Pack Curr",fg="black", font=("Courier", 12), bg="#D6C2C2", relief=SUNKEN)
    packCurr.grid(row = 30, column = 14, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)
    packCurrMin= tk.Label(main, text=0,fg="black", font=("Courier", 12), bg="#D6C2C2", relief=SUNKEN)
    packCurrMin.grid(row = 30, column = 15, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)
    packCurrMax= tk.Label(main, text=28.0,fg="black", font=("Courier", 12), bg="#D6C2C2", relief=SUNKEN)
    packCurrMax.grid(row = 30, column = 17, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)
    packCurrActual= tk.Label(main, text="0.0",fg="black", font=("Courier", 12, 'bold'), bg="red", relief=SUNKEN)
    packCurrActual.grid(row = 30, column = 16, padx=4, pady=2, columnspan = 1, sticky=N+S+E+W)   

    def updatePackCurr(actual):
        bg="lightgreen"
        if actual <= 0 or actual >= 250:
            bg="red"

        packCurrActual.config(text=actual, bg = bg)

    tkimage = PhotoImage(file="hold.png")
    tkimage = tkimage.subsample(2,2)
    logo = tk.Label(main,image=tkimage)
    logo.place(x=int(w/2),y=int(h/2), anchor="n")
    logo.image = tkimage

    # hold= tk.Button(main, text="ABORT", fg="black", font=("Courier", 12), bg = "RED", command=quit, cursor="shuttle")
    # hold.grid(row = 0, column = 9, padx=2, pady=2, columnspan = 1, sticky=N+S+E+W)    

    # IPM 1 Fault
    ipm1Fault= tk.Label(main, text="IPM 1 Fault",fg="black", font=("Courier", 12, 'bold'), bg="red", relief=SUNKEN)
    ipm1Fault.place(x=int(w/2)-150, y=int(h/2), anchor="n")
    def updateIpm1Fault(actual):
        bg="lightgreen"
        if actual <= 20.0 or actual >= 28.0:
            bg="red"

        ipm1Fault.config(bg=bg)    

    # IPM 2 Fault
    ipm2Fault= tk.Label(main, text="IPM 2 Fault",fg="black", font=("Courier", 12, 'bold'), bg="red", relief=SUNKEN)
    ipm2Fault.place(x=int(w/2)+150, y=int(h/2), anchor="n")
    def updateIpm2Fault(actual):
        bg="lightgreen"
        if actual <= 20.0 or actual >= 28.0:
            bg="red"

        ipm2Fault.config(bg=bg)


    # IPM 3 Fault
    ipm3Fault= tk.Label(main, text="IPM 3 Fault",fg="black", font=("Courier", 12, 'bold'), bg="red", relief=SUNKEN)
    ipm3Fault.place(x=int(w/2)-150, y=int(h/2)+150, anchor="n")
    def updateIpm3Fault(actual):
        bg="lightgreen"
        if actual <= 20.0 or actual >= 28.0:
            bg="red"

        ipm3Fault.config(bg=bg)

    # IPM 4 Fault
    ipm4Fault= tk.Label(main, text="IPM 4 Fault",fg="black", font=("Courier", 12, 'bold'), bg="red", relief=SUNKEN)
    ipm4Fault.place(x=int(w/2)+150, y=int(h/2)+150, anchor="n")
    def updateIpm4Fault(actual):
        bg="lightgreen"
        if actual <= 20.0 or actual >= 28.0:
            bg="red"

        ipm4Fault.config(bg=bg)


    def updateAll():
        # open udp stream 
        # receive input 
        # proccess update

        # Create a UDP socket
        # sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # server_address = ('localhost', 10000)
        # message = 'This is the message.  It will be repeated.'

        # try:

        #     # Send data
        #     sent = sock.sendto(message.encode('utf-8'), server_address)

        #     # Receive response
        #     msg, server = sock.recvfrom(4096)

        #     msg = str(int.from_bytes(msg, byteorder='little'))
            


        # finally:
        #     sock.close()
        dev = random.randint(0,34)
        if dev < 10:
            dev = "0"+str(dev)
        else:
            dev = str(dev)
           
        msg = dev + str("{0:.2f}".format(random.random()*1000))

        funcs = {"00":updateBat1Volt, "01":updateBat2Volt, "02":updateBatResVolt, "03":updateBatCur1, "04":updateBatCur2, "05":updateBatCurRes, "06":updateBatTemp1, "07":updateBatTemp2, "08":updateBatTempRes, "09":updateLevFront, "10":updateLevBack, "11":updatePodTemp, "12":updateAccelX, "13":updateAccelY, "14":updateAccelZ, "15":updatePressure, "16":updateMot1Temp, "17":updateMot2Temp, "18":updateMot3Temp, "19":updateMot4Temp, "20":updateMotor1Freq, "21":updateMotor2Freq, "22":updateMotor3Freq, "23":updateMotor4Freq, "24":updatePackTemp, "25":updatePackVolt, "26":updatePackCurr, "27":updateIpm1Temp, "28":updateIpm2Temp, "29":updateIpm3Temp, "30":updateIpm4Temp, "31":updateIpm1Fault, "32":updateIpm2Fault, "33":updateIpm3Fault, "34":updateIpm4Fault}    
        funcs[msg[0:2]](float(msg[2:]))

        root.after(100, updateAll)

    updateAll()    
    main.pack()
    root.mainloop()



def main():
    gui()

    

if __name__ == '__main__':
	main()
