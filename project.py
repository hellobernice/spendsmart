import tkinter
from tkinter import *
import tkinter.messagebox

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
        calcTopLvl.geometry("1200x600")
        calcTopLvl.title("Calculator")

        headingFrame = tkinter.Frame(calcTopLvl)
        headingFrame.pack(side = "top")

        headingCanvas = Canvas(headingFrame, highlightthickness = 0,
                               width = 1000)
        headingCanvas.config(bg = "#b5e1c1")
        headingCanvas.pack(side = "top")
        instructions = PhotoImage(file = "instructions.png")
        headingCanvas.create_image(50,10, anchor = NW, image = instructions)
        incomeHeading = PhotoImage(file = "heading.png")
        headingCanvas.create_image(100,220, anchor = SW, image = incomeHeading)

        frame1 = tkinter.Frame(calcTopLvl)
        frame1.config(bg = "#b5e1c1")
        frame1.pack(side = "left")
        frame2 = tkinter.Frame(calcTopLvl)
        frame2.config(bg = "#b5e1c1")
        frame2.pack(side = "left")
        frame3 = tkinter.Frame(calcTopLvl)
        frame3.config(bg = "#b5e1c1")
        frame3.pack(side = "left")
        frame4 = tkinter.Frame(calcTopLvl)
        frame4.config(bg = "#b5e1c1")
        frame4.pack(side = "left")
        frame5 = tkinter.Frame(calcTopLvl)
        frame5.config(bg = "#b5e1c1")
        frame5.pack(side = "left")
        
        incomeLabel = tkinter.Label(frame1, font = 20,
                                    text = "Monthly Salary:", bg = "#b5e1c1",
                                    fg = "#233027")
        incomeLabel.pack(side = "top", pady = 10, padx = 35)
        otherLabel = tkinter.Label(frame1, font = 20, text = "Others:",
                                   bg = "#b5e1c1", fg = "#233027")
        otherLabel.pack(side = "top", pady = 10, padx = 35)

        incomeEntry = tkinter.Entry(frame2, font = 20)
        incomeEntry.pack(side = "top", pady = 10, padx = 35)
        otherEntry = tkinter.Entry(frame2, font = 20)
        otherEntry.pack(side = "top", pady = 10, padx = 35)

        rentLabel = tkinter.Label(frame3, font = 20, text = "Rent/Mortgage:",
                                   bg = "#b5e1c1", fg = "#233027")
        rentLabel.pack(side = "top", pady = 10, padx = 35)
        utilityLabel = tkinter.Label(frame3, font = 20, text = "Utilities:",
                                   bg = "#b5e1c1", fg = "#233027")
        utilityLabel.pack(side = "top", pady = 10, padx = 35)
        transportLabel = tkinter.Label(frame3, font = 20,
                                       text = "Transportation:", bg = "#b5e1c1",
                                       fg = "#233027")
        transportLabel.pack(side = "top", pady = 10, padx = 35)
        foodLabel = tkinter.Label(frame3, font = 20, text = "Food:",
                                   bg = "#b5e1c1", fg = "#233027")
        foodLabel.pack(side = "top", pady = 10, padx = 35)
        entLabel = tkinter.Label(frame3, font = 20, text = "Entertainment:",
                                   bg = "#b5e1c1", fg = "#233027")
        entLabel.pack(side = "top", pady = 10, padx = 35)
        miscLabel = tkinter.Label(frame3, font = 20, text = "Miscellaneous:",
                                   bg = "#b5e1c1", fg = "#233027")
        miscLabel.pack(side = "top", pady = 10, padx = 35)

        rentEntry = tkinter.Entry(frame4, font = 20)
        rentEntry.pack(side = "top", pady = 10, padx = 35)
        utilityEntry = tkinter.Entry(frame4, font = 20)
        utilityEntry.pack(side = "top", pady = 10, padx = 35)
        transportEntry = tkinter.Entry(frame4, font = 20)
        transportEntry.pack(side = "top", pady = 10, padx = 35)
        foodEntry = tkinter.Entry(frame4, font = 20)
        foodEntry.pack(side = "top", pady = 10, padx = 35)
        entEntry = tkinter.Entry(frame4, font = 20)
        entEntry.pack(side = "top", pady = 10, padx = 35)
        miscEntry = tkinter.Entry(frame4, font = 20)
        miscEntry.pack(side = "top", pady = 10, padx = 35)

        def total_earnings():
            income1 = float(incomeEntry.get())
            income2 = float(otherEntry.get())
            total_income = income1 + income2

            expense1 = float(rentEntry.get())
            expense2 = float(utilityEntry.get())
            expense3 = float(transportEntry.get())
            expense4 = float(foodEntry.get())
            expense5 = float(entEntry.get())
            expense6 = float(miscEntry.get())
            total_expenses = expense1 + expense2 + expense3 + expense4 + expense5 + expense6
            total = total_income - total_expenses
            if total >= 0:
                tkinter.messagebox.showinfo("Total Earnings", "You have $" +
                                            str(format(total, '.2f')))
            else:
                tkinter.messagebox.showinfo("Total Earnings", "You have $" +
                                            str(format(total, '.2f'))\
                                            + "\nYou're in debt.")

        calcButton = tkinter.Button(frame5, text = "CALCULATE", font = 20,
                                    bg = "White", fg = "#233027",
                                    command = total_earnings)
        calcButton.pack(side = "top")
        
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
    
    

    
