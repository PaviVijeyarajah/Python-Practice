#!/usr/bin/env python
# coding: utf-8

# In[16]:


from tkinter import *
window = Tk() # create a window
label = Label(window, text = "Hard work pays off!") # create the label
button = Button(window, text = "Roger!") # create teh button
label.pack() # place the label in the window
button.pack() # place the button in the window
window.mainloop() # create an event loop


# In[5]:


from tkinter import  *

class ProcessButtonEvent:
    
    def __init__(self):
        window = Tk()
        btOk = Button(window, text = "OK", fg = "red", command = self.processOK)
        btCancel = Button(window, text = "Cancel", bg = "pink", command = self.processCancel)
        btOk.pack()
        btCancel.pack()

        
        window.mainloop()
        
    def processOK(self):
        print("Ok button is clicked!")
    
    def processCancel(self):
        print("Cancel button clicked!")
    

ProcessButtonEvent()


# In[6]:


from tkinter import  *

def processOK():
    print("Ok button is clicked!")
    
def processCancel():
    print("Cancel button clicked!")
    
window = Tk()
btOk = Button(window, text = "OK", fg = "red", command = processOK)
btCancel = Button(window, text = "Cancel", bg = "pink", command = processCancel)

btOk.pack()
btCancel.pack()

window.mainloop()


# In[7]:


from tkinter import  *

window = Tk() # create a window 
label = Label(window, text = "Hard work pays off!") # create the label
button = Button(window, text = "Roger!") # create teh button

label.pack() # place the label in the window
button.pack() # place the button in the window

window.mainloop() # create an event loop


# In[7]:


from tkinter import *
class GridManagerDemo:
    window = Tk()
    window.title("Grid Manage Demo")
    message = Message(window, text = "This message widget occupies three rows and two columns")
    message.grid(row = 1, column = 1, rowspan = 3, columnspan = 2)
    # padx, pady: how many pixles to pad widget, horizontally and veritically
    Label(window, text = "First name:").grid(row = 1, column = 3)
    Entry(window).grid(row = 1, column = 4, padx = 5, pady = 5)

    Label(window, text = "Last name:").grid(row = 2, column = 3)
    Entry(window).grid(row = 2, column = 4)
    # E, S, N, W; NW, NE, SW, SE
    Button(window, text = "Get Name").grid(row = 3, column = 4, padx = 5, pady = 5, sticky = E)
    window.mainloop()
GridManagerDemo()


# In[8]:


from tkinter import *

class PackManagerDemo:
    def __init__(self):
        window = Tk()
        window.title("Pack Manager Demo")
        
        # Expand tells the pack manager to assign additional space to the widget
        # fill option uses X, Y, or BOTH to fill horizontally, vertically or both ways
        Label(window, text = "Blue", bg = "blue").pack()
        Label(window, text = "Red", bg = "red").pack(fill = BOTH, expand = 1)
        Label(window, text = "Green", bg = "green").pack(fill = BOTH)
        
        window.mainloop()

PackManagerDemo()


# In[32]:


from tkinter import *

class PackManagerDemo:
    def __init__(self):
        window = Tk()
        window.title("Pack Manager Demo")
        
        # Expand tells the pack manager to assign additional space to the widget
        # fill option uses X, Y, or BOTH to fill horizontally, vertically or both ways
        Label(window, text = "Blue", bg = "blue").pack(side = LEFT)
        Label(window, text = "Red", bg = "red").pack(side = LEFT, fill = BOTH, expand = 1)
        Label(window, text = "Green", bg = "green").pack(side = LEFT, fill = BOTH)
        
        window.mainloop()

PackManagerDemo()


# In[14]:


from tkinter import * 

class ImageDemo:
    def __init__(self):
        window = Tk() 
        window.title("Image Demo")   
        
        # create photoimage objects
        caImage = PhotoImage(file = "image/ca.gif")
        chinaImage = PhotoImage(file = "image/china.gif")
        leftImage = PhotoImage(file = "image/left.gif")
        rightImage = PhotoImage(file = "image/right.gif")
        usImage = PhotoImage(file = "image/usIcon.gif")
        ukImage = PhotoImage(file = "image/ukIcon.gif")
        crossImage = PhotoImage(file = "image/x.gif")
        circleImage = PhotoImage(file = "image/o.gif")


        # frame1 to contain lable and canvas
        frame1 = Frame(window)
        frame1.pack()
        Label(frame1, image = caImage).pack(side = LEFT)
        canvas = Canvas(frame1)
        canvas.create_image(90, 50, image = chinaImage)
        canvas["width"] = 200
        canvas["height"] = 100
        canvas.pack(side = LEFT)
        
        
        frame2 = Frame(window)
        frame2.pack()
        
        Button(frame2, image = leftImage).pack(side = LEFT)
        Button(frame2, image = rightImage).pack(side = LEFT)
        Checkbutton(frame2, image = usImage).pack(side = LEFT)
        Checkbutton(frame2, image = ukImage).pack(side = LEFT)
        Radiobutton(frame2, image = crossImage).pack(side = LEFT)
        Radiobutton(frame2, image = circleImage).pack(side = LEFT)

   
        
        window.mainloop()
ImageDemo()        
        
 


# In[17]:


from tkinter import *

class MenuDemo:
    def __init__(self):
        window = Tk()
        window.title("Menu Demo")
        
        menubar = Menu(window)
        window.config(menu = menubar) 
        
        operationMenu = Menu(menubar, tearoff = 0)
        menubar.add_cascade(label = "Operation", menu = operationMenu)
        operationMenu.add_command(label = "Add", command = self.add)
        operationMenu.add_command(label = "Subtract", command = self.subtract)
        operationMenu.add_separator()
        operationMenu.add_command(label = "Multiply", command = self.multiply)
        operationMenu.add_command(label = "Divide", command = self.divide)
        
        exitmenu = Menu(menubar, tearoff = 0)
        menubar.add_cascade(label = "Exit", menu = exitmenu)
        exitmenu.add_command(label = "Quit", command = window.quit)
        
        frame0 = Frame(window) 
        frame0.grid(row = 1, column = 1, sticky = W)
        
        plusImage = PhotoImage(file = "plus.gif")
        minusImage = PhotoImage(file = "minus.gif")
        timesImage = PhotoImage(file = "times.gif")
        divideImage = PhotoImage(file = "divide.gif")
        
        Button(frame0, image = plusImage, command = self.add).grid(row = 1, column = 1, sticky = W)
        Button(frame0, image = minusImage, command = self.subtract).grid(row = 1, column = 2)
        Button(frame0, image = timesImage, command = self.multiply).grid(row = 1, column = 3)
        Button(frame0, image = divideImage, command = self.divide).grid(row = 1, column = 4)
        
        frame1 = Frame(window)
        frame1.grid(row = 2, column = 1, pady = 10)
        Label(frame1, text = "Number 1:").pack(side = LEFT)
        self.v1 = StringVar()
        Entry(frame1, width = 5, textvariable = self.v1, justify = RIGHT).pack(side = LEFT)
        Label(frame1, text = "Number 2:").pack(side = LEFT)
        self.v2 = StringVar()
        Entry(frame1, width = 5, textvariable = self.v2, justify = RIGHT).pack(side = LEFT)
        Label(frame1, text = "Result:").pack(side = LEFT)
        self.v3 = StringVar()
        Entry(frame1, width = 5, textvariable = self.v3, justify = RIGHT).pack(side = LEFT)
        

        frame2 = Frame(window) 
        frame2.grid(row = 3, column = 1, pady = 10, sticky = E)
        Button(frame2, text = "Add", command = self.add).pack(side = LEFT)
        Button(frame2, text = "Subtract", command = self.subtract).pack(side = LEFT)
        Button(frame2, text = "Multiply", command = self.multiply).pack(side = LEFT)
        Button(frame2, text = "Divide", command = self.divide).pack(side = LEFT)
               
        mainloop()
        
    def add(self): 
        self.v3.set(eval(self.v1.get()) + eval(self.v2.get()))
    
    def subtract(self):
        self.v3.set(eval(self.v1.get()) - eval(self.v2.get()))
    
    def multiply(self):
        self.v3.set(eval(self.v1.get()) * eval(self.v2.get()))
    
    def divide(self):
        self.v3.set(eval(self.v1.get()) / eval(self.v2.get()))

MenuDemo() 


# In[22]:


class PopupMenuDemo:
    def __init__(self):
        window = Tk() 
        window.title("Popup Menu Demo") 

        self.menu = Menu(window, tearoff = 0)
        self.menu.add_command(label = "Draw a line", command = self.displayLine)
        self.menu.add_command(label = "Draw an oval", command = self.displayOval)
        self.menu.add_command(label = "Draw a rectangle", command = self.displayRect)
        self.menu.add_command(label = "Clear", command = self.clearCanvas)

        self.canvas = Canvas(window, width = 200, height = 100, bg = "white")
        self.canvas.pack()
        
        self.canvas.bind("<Button-1>", self.popup)
        
        window.mainloop() 

    def displayRect(self):
        self.canvas.create_rectangle(10, 10, 190, 90, tags = "rect")

    def displayOval(self):
        self.canvas.create_oval(10, 10, 190, 90, tags = "oval")

    def displayLine(self):
        self.canvas.create_line(10, 10, 190, 90, tags = "line")
        self.canvas.create_line(10, 90, 190, 10, tags = "line")

    def clearCanvas(self):
        self.canvas.delete("rect", "oval", "line")

    def popup(self, event):
        self.menu.post(event.x_root, event.y_root)
    
PopupMenuDemo() 


# In[23]:


from tkinter import * 

class MouseKeyEventDemo:
    def __init__(self):
        window = Tk() 
        window.title("Event Demo") 
        
        canvas = Canvas(window, bg = "white", width = 200, height = 100)
        canvas.pack()        

        canvas.bind("<Button-1>", self.processMouseEvent)        

        canvas.bind("<Key>", self.processKeyEvent)    
        canvas.focus_set()
        
        window.mainloop() 

    def processMouseEvent(self, event):       
        print("clicked at", event.x, event.y)
        print("Position in the screen", event.x_root, event.y_root)
        print("Which button is clicked? ", event.num)
    
    def processKeyEvent(self, event):        
        print("keysym? ", event.keysym)
        print("char? ", event.char)
        print("keycode? ", event.keycode)
    
MouseKeyEventDemo() 


# In[24]:


from tkinter import * 

class EnlargeShrinkCircle:
    def __init__(self):
        self.radius = 50
                
        window = Tk() 
        window.title("Control Circle Demo") 
        self.canvas = Canvas(window, bg = "white", width = 200, height = 200)
        self.canvas.pack()
        self.canvas.create_oval(100-self.radius, 100-self.radius, 100 + self.radius,100 + self.radius, tags = "oval")
        
        self.canvas.bind("<Button-1>", self.increaseCircle)
        self.canvas.bind("<Button-3>", self.decreaseCircle)
        
        window.mainloop() 
        
    def increaseCircle(self, event):
        self.canvas.delete("oval")
        if self.radius < 100:
            self.radius += 2
        self.canvas.create_oval(100-self.radius, 100-self.radius, 100 + self.radius,100 + self.radius, tags = "oval")
        
    def decreaseCircle(self, event):
        self.canvas.delete("oval")
        if self.radius > 2:
            self.radius -= 2
        self.canvas.create_oval(100-self.radius, 100-self.radius, 100 + self.radius,100 + self.radius, tags = "oval")

EnlargeShrinkCircle() 


# In[1]:


from tkinter import *

class AnimationDemo:
    def __init__(self):
        window = Tk()
        window.title("Animation Demo")
        width = 250
        
        canvas = Canvas(window, bg = "white", width = 250, height = 50)
        canvas.pack()
        
        x = 0 
        canvas.create_text(x, 30, text = "Message Moving?", tags = "text")
        
        dx = 3
        while True:
            canvas.delete # move text dx unit to the right
            canvas.after(10) #sleep for 100 milliseconds
            canvas.update() # update canvas - it re-displayes it
            
            if x < width:
                x += dx
            else:
                x = 0
                canvas.delete("text")
                canvas.create_text(x, 30, text = "Message Moving?", tags = "text")

        window.mainloop()

AnimationDemo()


# In[31]:


from tkinter import * 

class ControlAnimation:
    def __init__(self):
        window = Tk() 
        window.title("Control Animation Demo") 
        
        self.width = 250 
        self.canvas = Canvas(window, bg = "white", width = self.width, height = 50)
        self.canvas.pack()
        
        frame = Frame(window)
        frame.pack()
        btStop = Button(frame, text = "Stop", command = self.stop)
        btStop.pack(side = LEFT)
        btResume = Button(frame, text = "Resume", command = self.resume)
        btResume.pack(side = LEFT)
        btFaster = Button(frame, text = "Faster", command = self.faster)
        btFaster.pack(side = LEFT)
        btSlower = Button(frame, text = "Slower", command = self.slower)
        btSlower.pack(side = LEFT)
        
        self.x = 0 
        self.sleepTime = 100 
        self.canvas.create_text(self.x, 30, text = "Message moving?", tags = "text")
        
        self.dx = 3
        self.isStopped = False
        self.animate()
        
        window.mainloop() 
        
    def stop(self): 
        self.isStopped = True
    
    def resume(self): 
        self.isStopped = False   
        self.animate()
    
    def faster(self): 
        if self.sleepTime > 5:
            self.sleepTime -= 20
               
    def slower(self): 
        self.sleepTime += 20
                                
    def animate(self): 
        while not self.isStopped:
            self.canvas.move("text", self.dx, 0)  
            self.canvas.after(self.sleepTime) 
            self.canvas.update() 
            if self.x < self.width:
                self.x += self.dx  
            else:
                self.x = 0 
                self.canvas.delete("text") 
                self.canvas.create_text(self.x, 30, text = "Message moving?", tags = "text") 
ControlAnimation()


# In[32]:


from tkinter import * 
    
class ScrollText:
    def __init__(self):
        window = Tk() 
        window.title("Scroll Text Demo")
        
        frame1 = Frame(window)
        frame1.pack()
        scrollbar = Scrollbar(frame1)
        scrollbar.pack(side = RIGHT, fill = Y)
        text = Text(frame1, width = 40, height = 10, wrap = WORD, yscrollcommand = scrollbar.set)
        text.pack()
        scrollbar.config(command = text.yview)
        
        window.mainloop() 
ScrollText()


# In[34]:


import tkinter.messagebox
import tkinter.simpledialog
import tkinter.colorchooser

tkinter.messagebox.showinfo("showinfo", "This is an info message")
tkinter.messagebox.showwarning("showwarning", "This is a warning")
tkinter.messagebox.showerror("showerror", "This is an error")

# askokcancel
isYes = tkinter.messagebox.askyesno("askyesno", "Continue?")
print(isYes)


# In[18]:


from tkinter import *
def processOK():
    print("Ok button is clicked!")
def processCancel():
    print("Cancel button clicked!")
window = Tk()
btOk = Button(window, text = "OK", fg = "red", command = processOK)
btCancel = Button(window, text = "Cancel", bg = "pink", command = processCancel)
btOk.pack()
btCancel.pack()
window.mainloop()


# In[19]:


from tkinter import *
class ProcessButtonEvent:
    def __init__(self):
        window = Tk()
        btOk = Button(window, text = "OK", fg = "red", command = self.processOK)
        btCancel = Button(window, text = "Cancel", bg = "pink", command =
        self.processCancel)
        btOk.pack()
        btCancel.pack()
        window.mainloop()
    def processOK(self):
        print("Ok button is clicked!")
    def processCancel(self):
        print("Cancel button clicked!")
ProcessButtonEvent()


# In[22]:


# Slide 13 Demo
from tkinter import *
class WidgetDemo:
    def __init__(self):
        window = Tk()
        window.title("Widgets Demo")
        frame1 = Frame(window)
        frame1.pack()
        self.v1 = IntVar()
        cbtBold = Checkbutton(frame1, text = "Bold", variable = self.v1, command =self.processCheckbutton)
        self.v2 = IntVar()
        rbRed = Radiobutton(frame1, text = "Pink", bg = "pink", variable = self.v2,value = 1, command = self.processRadiobutton)
        rbYellow = Radiobutton(frame1, text = "Yellow", bg = "yellow", variable =self.v2,value = 2, command = self.processRadiobutton)
        cbtBold.grid(row = 1, column = 1)
        rbRed.grid(row = 1, column = 2)
        rbYellow.grid(row = 1, column = 3)
        # create another frame
        frame2 = Frame(window)
        frame2.pack()
        label = Label(frame2, text = "Enter your name: ")
        self.name = StringVar()
        entryName = Entry(frame2, textvariable = self.name)
        btGetName = Button(frame2, text = "Get Name", command = self.processButton)
        message = Message(frame2, text = "It is a widgets demo")
        label.grid(row = 1, column = 1)
        entryName.grid(row = 1, column = 2)
        btGetName.grid(row = 1, column = 3)
        message.grid(row = 1, column = 4)
        text = Text(window)
        text.pack()
        text.insert(END, "Success is simple\n")
        text.insert(END, "\nsuccess is simple\n")
        text.insert(END, "success is simple")
        window.mainloop()
    # Check button status
    def processCheckbutton(self):
        print("Check button is " + ("checked" if self.v1.get() == 1 else
        "unchecked"))
    def processRadiobutton(self):
        print("Pink" if self.v2.get() == 1 else "Yellow")
    def processButton(self):
        print("Your name is: " + self.name.get())
WidgetDemo()


# In[36]:


from tkinter import *
class ChangeLabelDemo:
    def __init__(self):
        window = Tk()
        window.title("Change Label Demo")
        frame1 = Frame(window)
        frame1.pack()
        self.lbl = Label(frame1, text = "Programming is fun")
        self.lbl.pack()
        frame2 = Frame(window)
        frame2.pack()
        label = Label(frame2, text = "Enter text: ")
        self.msg = StringVar()
        entry = Entry(frame2, textvariable = self.msg)
        btChangeText = Button(frame2, text = "Change Text",command = self.processButton)
        self.v1 = StringVar()
        rbRed = Radiobutton(frame2, text = "Pink", bg = "pink",variable = self.v1, value = 'P', command = self.processRadiobutton)
        rbYellow = Radiobutton(frame2, text = "Blue",bg = "blue", variable = self.v1, value = 'B', command =self.processRadiobutton)
        label.grid(row = 1, column = 1)
        entry.grid(row = 1, column = 2)
        btChangeText.grid(row = 1, column = 3)
        rbRed.grid(row = 1, column = 4)
        rbYellow.grid(row = 1, column = 5)
        window.mainloop()
    def processRadiobutton(self):
        if self.v1.get() == 'P':
            self.lbl["fg"] = "pink"
        elif self.v1.get() == 'B':
            self.lbl["fg"] = "blue"
    def processButton(self):
        self.lbl["text"] = self.msg.get()
ChangeLabelDemo()


# In[2]:


from tkinter import *
class ChangeLabelDemo:
    def __init__(self):
        window = Tk()
        window.title("Change Label Demo")
        frame1 = Frame(window)
        frame1.pack()
        label = Label(frame1, text = "Enter Text: ")
        self.sentence = StringVar()
        entry = Entry(frame1, textvariable= self.sentence)
        chB = Button(frame1, text= "Change Text", command= self.processChange)
        self.v1 = IntVar()
        rbPink = Radiobutton(frame1, text= "Pink", bg= "pink", variable= self.v1,
        value= 1, command= self.processColor)
        rbPurple = Radiobutton(frame1, text= "Purple", bg= "purple", variable=
        self.v1, value= 2, command= self.processColor)
        label.grid(row=2, column=1)
        entry.grid(row=2, column=2)
        chB.grid(row=2, column=2)
        rbPink.grid(row=2, column=2)
        rbPurple.grid(row=2, column=2)
        self.label2 = Label(frame1)
        self.label2.grid(row=1)
    def processChange(self):
        self.label2["text"] = self.sentence
    def processColor(self):
        if self.v1 == 1:
            self.label2["fg"] = "pink"
        elif self.v2 == 2:
            self.label2["fg"] = "purple"
        else:
            self.label2["fg"] = "black"
ChangeLabelDemo()


# In[6]:


from tkinter import *
class CanvasDemo:
    def __init__(self):
        window = Tk()
        window.title("Canvas Demo")
        self.canvas = Canvas(window, width = 200, height = 100, bg = "green")
        self.canvas.pack()
        frame = Frame(window)
        frame.pack()
        btRectangle = Button(frame, text = "Rectangle", command = self.displayRect)
        btOval = Button(frame, text = "Oval", command = self.displayOval)
        btArc = Button(frame, text = "Arc", command = self.displayArc)
        btPolygon = Button(frame, text = "Polygon", command = self.displayPolygon)
        btLine = Button(frame, text = "Line", command = self.displayLine)
        btString = Button(frame, text = "String", command = self.displayString)
        btClear = Button(frame, text = "Clear", command = self.clearCanvas)
        btRectangle.grid(row = 1, column = 1)
        btOval.grid(row = 1, column = 2)
        btArc.grid(row = 1, column = 3)
        btPolygon.grid(row = 1, column = 4)
        btLine.grid(row = 1, column = 5)
        btString.grid(row = 1, column = 6)
        btClear.grid(row = 1, column = 7)
        window.mainloop() # Create an event loop
    # Display a rectangle
    def displayRect(self):
        self.canvas.create_rectangle(10, 10, 190, 90, tags = "rect")
    # Display an oval
    def displayOval(self):
        self.canvas.create_oval(10, 10, 190, 90, fill = "red", tags = "oval")
    # Display an arc
    def displayArc(self):
        self.canvas.create_arc(10, 10, 190, 90, start = 0,
        extent = 90, width = 8, fill = "red", tags = "arc")
    # Display a polygon
    def displayPolygon(self):
        self.canvas.create_polygon(10, 10, 190, 90, 30, 50, tags = "polygon")
    # Display a line
    def displayLine(self):
        self.canvas.create_line(10, 10, 190, 90, fill = "red", tags = "line")
        self.canvas.create_line(10, 90, 190, 10, width = 9, arrow = "first",activefill = "blue", tags = "line")
    # Display a string
    def displayString(self):
        self.canvas.create_text(60, 40, text = "Hi, I am a string",
        font = "Times 10 bold underline", tags = "string")
    # Clear drawings
    def clearCanvas(self):
        self.canvas.delete("rect", "oval", "arc", "polygon", "line", "string")
CanvasDemo() # Create GUI


# In[ ]:




