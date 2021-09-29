import tkinter as tk
def draw(canvas):
    #canvas.create_rectangle(90,70,180,120,fill="#F6B794",width=0)
    #canvas.create_oval(30,80,150,200,fil="#FF69B4",width=4)
    #canvas.create_rectangle(40,40,80,140,fill="#D2B4A7",width=10)
    #canvas.create_line(10,20,10,120,fill="blue",width=3)
    canvas.create_text(200, 200, text="AAA",font="Times 30", anchor="w")
    canvas.create_text(200, 200, text="BBB",font="Times 30", anchor="center")
    canvas.create_text(200, 200, text="CCC",font="Times 30", anchor="ne")
def makeCanvas(w,h):
    root=tk.Tk()
    canvas=tk.Canvas(root, width=w, height=h)
    canvas.configure(bg="Pink")
    canvas.pack()
    #canvas.create_rectangle(10,50,110,100)
    draw(canvas)
    root.mainloop()
makeCanvas(400,400)