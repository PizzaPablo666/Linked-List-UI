from tkinter import *
import tkinter as tk
from tkinter import ttk
from playsound import playsound
import multiprocessing

global taili
global taily
taili = 4
taily = 0
global labels
labels = []
def create_label(val, taili, taily, nextID):
    count = len(root.winfo_children())
    label = Label(root, text=f"Label #{val} \n#{nextID}")
    label.grid(row=taili, column=taily)
    labels.append(label)

def removing_label(tali, taly):
	label = Label(root, text="AAAAAAAAAAAAAAAA\nA", bg="#9cacff",fg="#9cacff")
	label.grid(row=taili, column=taily)

	
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None

    def Atbegining(self, data_in):
        NewNode = Node(data_in)
        obj_id = id(self.head)
        NewNode.next = self.head
        self.head = NewNode
        llist.LListprint()

        # Function to add newnode
    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        if self.head is None:
            self.head = NewNode
            llist.LListprint()
            return
        laste = self.head
        while(laste.next):
            laste = laste.next
        laste.next=NewNode
        llist.LListprint()

# Function to add node
    def Inbetween(self,middle_node_num,newdata):
        printval = self.head
        while(middle_node_num > 1):
            printval = printval.next
            middle_node_num -= 1
        if printval is None:
        	return
        NewNode = Node(newdata)
        NewNode.next = printval.next
        printval.next = NewNode
        self.LListprint()
		
# Function to remove node
    def RemoveNode(self, RemoveNode):
        HeadVal = self.head

        if (HeadVal is not None):
            if (RemoveNode == 1):
                self.head = HeadVal.next
                HeadVal = None
                return
        while(RemoveNode > 2):
            HeadVal = HeadVal.next
            RemoveNode -= 1
        if HeadVal is None:
        	return
        prev = HeadVal
        HeadVal = HeadVal.next
        prev.next = HeadVal.next
        HeadVal = None
        
        llist.LListprint()

    def LListprint(self):
    	global taili
    	global taily
    	taili = 4
    	taily = 0
    	printval = self.head
    	while (printval):
            obj_id = id(printval.next)
            if taily == 4:
                taily = 0
                taili += 2
                BlankLabel = Label(root, text="", bg="#9cacff", fg="#9cacff")
                BlankLabel.grid(row=taili - 1, column=0)
            create_label(printval.data, taili, taily, obj_id)
            taily += 1
            print(printval.data)
            printval = printval.next

root = Tk()
root.configure(bg="#9cacff")
root.title("Linked List")


#CreateList
def CreateList_Func():
	global llist 
	llist = SLinkedList()
	status = Tk()
	status.title("Status")
	statusLabel = Label(status, text="\nLinked List is created!\n")
	statusLabel.grid(row=0,column=0)

#AddNode
def AddNodeBeg_Func():
	valuePage = Tk()
	valuePage.title("Enter Value")
	valuePage.configure(bg="red")
	value = Entry(valuePage, width=20, bg="black", fg="white", borderwidth=5)
	value.grid(row=0, column=0)
	AddValue_But = Button(valuePage, text="Add Value", 
		padx=53, pady=10,
		bg="#ff5733",
		command=lambda: llist.Atbegining(value.get()))
	print(value.get())
	AddValue_But.grid(row=1, column=0)

#AddNewNode
def AddNodeEnd_Func():
	valuePage = Tk()
	valuePage.title("Enter Value")
	valuePage.configure(bg="red")
	value = Entry(valuePage, width=20, bg="black", fg="white", borderwidth=5)
	value.grid(row=0, column=0)
	AddValue_But = Button(valuePage, text="Add Value", 
		padx=53, pady=10,
		bg="#ff5733",
		command=lambda: llist.AtEnd(value.get()))
	print(value.get())
	AddValue_But.grid(row=1, column=0)

#RemoveNode
def RemoveNode_Func():
	valuePage = Tk()
	valuePage.title("Enter the Node")
	valuePage.configure(bg="red")

	nodeNum = Entry(valuePage, width=20, bg="black", fg="white", borderwidth=5)
	nodeNum.grid(row=0, column=1)

	AddValue1_But = Button(valuePage, text="Remove this node", 
		padx=53, pady=10,
		bg="#ff5733", 
		command=lambda: llist.RemoveNode(int(nodeNum.get())))
	AddValue1_But.grid(row=1, column=0)

#InsertNode
def InsertNode_Func():
	valuePage = Tk()
	valuePage.title("Enter Value and Node number")
	valuePage.configure(bg="red")

	value = Entry(valuePage, width=20, bg="black", fg="white", borderwidth=5)
	value.grid(row=0, column=0)
	nodeNum = Entry(valuePage, width=20, bg="black", fg="white", borderwidth=5)
	nodeNum.grid(row=0, column=1)

	AddValue1_But = Button(valuePage, text="Check Values", 
		padx=53, pady=10,
		bg="#ff5733", 
		command=lambda: llist.Inbetween(int(nodeNum.get()),value.get()))
	AddValue1_But.grid(row=1, column=0)

#RemoveAll
def RemoveAll_Func():
    global taili
    global taily
    taili = 4
    taily = 0
    count = 0
    current = llist.head
    while (llist.head != None):
        if(taily == 4):
            taily = 0
            taili += 1
        current = llist.head
        llist.head = llist.head.next
        removing_label(taili, taily)
        taily += 1
        count +=1 
        current = None

#Multiprocessing
def MultiProc_Func():
	p = multiprocessing.Process(target=PlaySound_Func)
	p.start()
	sound = Tk()
	sound_But = Button(sound, text="Press to stop", 
	padx=30, pady=3,
	bg="#ee75ff",
	command=lambda: [p.terminate(), sound.destroy()])
	sound_But.grid(row=0, column=0)

#playsound
def PlaySound_Func():
	playsound('future.mp3')

#Exit
def Exit_Func():
	root.destroy()




#Create List
CreateList_But = Button(root, text="Create List", 
	padx=55, pady=10,
	bg="#ffa500",
	command=CreateList_Func)
CreateList_But.grid(row=0, column=0)

#Add Node
AddNodeEnd_But = Button(root, text="Add Node\n At the End", 
	padx=52, pady=3,
	bg="#808080",
	command=AddNodeEnd_Func)
AddNodeEnd_But.grid(row=0, column=1)

#Add New Node
AddNodeBeg_But = Button(root, text="Add Node\n At the Beginning", 
	padx=30, pady=3,
	bg="#ee75ff",
	command=AddNodeBeg_Func)
AddNodeBeg_But.grid(row=0, column=2)

#Reove Node
RemoveNode_But = Button(root, text="Remove Node", 
	padx=40, pady=10, 
	bg="#8475ff",
	command=RemoveNode_Func)
RemoveNode_But.grid(row=0, column=3)

#Insert Node
InsertNode_But = Button(root, text="Insert Node", 
	padx=52, pady=10,
	bg="#33c7ff",
	command=InsertNode_Func)
InsertNode_But.grid(row=1, column=0)

#Remove All
RemoveAll_But = Button(root, text="Remove All", 
	padx=49, pady=10,
	bg="#6bff33",
	command=RemoveAll_Func)
RemoveAll_But.grid(row=1, column=1)

#Playsound
Playsound_But = Button(root, text="Play Music", 
	padx=49, pady=10,
	bg="#6bff33",
	command=MultiProc_Func)
Playsound_But.grid(row=1, column=2)

#Exit
Exit_But = Button(root, text="Exit", 
	padx=73, pady=10,
	bg="#ff5733",
	command=Exit_Func)
Exit_But.grid(row=1, column=3)



#separator
BlankLabel = Label(root, text="", bg="#9cacff", fg="#9cacff")
BlankLabel.grid(row=2, column=0)
sep2 = ttk.Separator(root, orient="horizontal")
sep2.grid(row=3, column=0, columnspan=4, ipadx=360)


root.mainloop()  