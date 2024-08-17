import tkinter
from tkinter import *

def main():
    #---------------------------MAIN WINDOW-------------------------------
    root = tkinter.Tk()
    root.title("SpendSmart")
    root.config(background = "#b5e1c1")
    root.geometry("1000x600")
    topFrame = tkinter.Frame(root)
    topFrame.pack()
    bottomFrame = tkinter.Frame(root)
    bottomFrame.config(bg = "#b5e1c1")
    bottomFrame.pack()
    
    canvas = Canvas(topFrame, highlightthickness = 0, width = 1000)
    canvas.config(bg = "#b5e1c1")
    canvas.pack(side = "top")
    title = PhotoImage(file = "title.png")
    canvas.create_image(50,60, anchor = NW, image = title)
    
    #-------------------------------MENUBAR----------------------------------
    menubar = tkinter.Menu(root)
    helpMenu = tkinter.Menu(menubar, tearoff = 0)
    helpMenu.add_command(label = "Help", command = guide)
    menubar.add_cascade(label = " ? ", menu = helpMenu)
    root.config(menu = menubar)

    #-----------------------------CALCULATOR------------------------------
    def calc():
        calcTopLvl = tkinter.Toplevel()
        calcTopLvl.config(bg = "#b5e1c1")
        calcTopLvl.geometry("1000x600")
        calcTopLvl.title("Calculator")

        headingFrame = tkinter.Frame(calcTopLvl)
        headingFrame.pack(side = "top")

        headingCanvas = Canvas(headingFrame, highlightthickness = 0,
                               width = 1000)
        headingCanvas.config(bg = "#b5e1c1")
        headingCanvas.pack(side = "top")
        instructions = PhotoImage(file = "instructions.png")
        headingCanvas.create_image(50,10, anchor = NW, image = instructions)

        heading = PhotoImage(file = "heading.png")
        headingCanvas.create_image(100,220, anchor = SW, image = heading)
        

        tkinter.mainloop()

    #--------------------------MAIN WINDOW BUTTONS-------------------------
    calculatorButton = tkinter.Button(bottomFrame, text = "CALCULATOR",
                                      font = ("Arial", 35), bg = "White",
                                      fg = "#233027", command = calc)
    calculatorButton.pack()
    quitButton = tkinter.Button(bottomFrame, text = "QUIT", font = ("Arial", 35),
                                fg = "#233027", bg = "White",
                                command = root.destroy)
    quitButton.pack(pady = 35)
    tkinter.mainloop()
#---------------------------MENUBAR CALLBACK FUNCTIONS--------------------------------
def guide():
    helpTopLvl = tkinter.Toplevel()
    helpTopLvl.config(bg = "#b5e1c1")
    helpTopLvl.geometry("1000x600")
    helpTopLvl.title("Help")
    canvasTopLvl = Canvas(helpTopLvl, highlightthickness = 0, width = 1000,
                          height = 500)
    canvasTopLvl.config(bg = "#b5e1c1")
    canvasTopLvl.pack(expand=True)
    helpPic = PhotoImage(file = "help.png")
    canvasTopLvl.create_image(50,5, anchor = NW, image = helpPic)


    tkinter.mainloop()
main()
    
    

    
