#coding: utf-8
import tkinter as tk
import random as R


#set the first centre location randomly
#x=100
#y=100
#dx=R.randint(1,3)
#dy=R.randint(1,3)

#Dictatory ={}
#ball={"x":100, "y":100, "dx":R.randint(1,3), "dy":R.randint(1,3)}
#Value of ball["x"] is 100

ball=[
    {"x":100, "y":100, "dx":R.randint(1,3), "dy":R.randint(1,3), "color":"violet"},
    {"x":200, "y":400, "dx":-R.randint(1,3), "dy":R.randint(1,3), "color":"red"},
    {"x":600, "y":300, "dx":R.randint(1,3), "dy":-R.randint(1,3), "color":"navy"},
    {"x":600, "y":300, "dx":R.randint(1,3), "dy":-R.randint(1,3), "color":"orange"},
    {"x":600, "y":300, "dx":R.randint(1,3), "dy":-R.randint(1,3), "color":"green"}]
#Value of ball[0]["x"] is 100


#Move Function
def move():
    global ball
    for b in ball:
        canvas.create_oval(b["x"]-31, b["y"]-31, b["x"]+31, b["y"]+31, fill="light blue", width=0) #same color as the canvas bg to cancel

        b["x"]+=b["dx"]  #b["x"]=b["x"]+b["dy"]
        b["y"]+=b["dy"]
        
        canvas.create_oval(b["x"]-30, b["y"]-30, b["x"]+30, b["y"]+30, fill=b["color"], width=0)

        if b["x"]+30 >= canvas.winfo_width():
            b["dx"]=-R.randint(1,3)
        if b["x"]-30 <= 0:
            b["dx"]=+R.randint(1,3)
        if b["y"]+30 >= canvas.winfo_height():
            b["dy"]=-R.randint(1,3)
        if b["y"]-30 <= 0:
            b["dy"]=+R.randint(1,3)
    
    frame.after(30, move) #to loop the move function
    


frame = tk.Tk()
frame.geometry("800x800")
frame.title("🔴🟠🟢🔵 Moving Balls 🔵🔴🟠🟢")

canvas=tk.Canvas(frame, width=700, height=700, bg="light blue")
canvas.place(x=50, y=50)

#Trigger the move function
frame.after(30, move)

frame.mainloop()
