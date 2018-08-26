from Tkinter import *
from query import get_query
import webbrowser

def print_results():
	q = query.get()
	try:
		ql = get_query(q.lower().split())
	except:
		ql = []
	
	# print link into result
	for i in range(len(ql)):
		if i==0:
			result1.config(text=ql[i])
		elif i==1:
			result2.config(text=ql[i])
		elif i==2:
			result3.config(text=ql[i])
		elif i==3:
			result4.config(text=ql[i])
		elif i==4:
			result5.config(text=ql[i])
		elif i==5:
			result6.config(text=ql[i])
		elif i==6:
			result7.config(text=ql[i])
		elif i==7:
			result8.config(text=ql[i])
		elif i==8:
			result9.config(text=ql[i])
		elif i==9:
			result10.config(text=ql[i])
	
	# print blank into result
	for i in range(len(ql),10):
		if i==0:
			result1.config(text="")
		elif i==1:
			result2.config(text="")
		elif i==2:
			result3.config(text="")
		elif i==3:
			result4.config(text="")
		elif i==4:
			result5.config(text="")
		elif i==5:
			result6.config(text="")
		elif i==6:
			result7.config(text="")
		elif i==7:
			result8.config(text="")
		elif i==8:
			result9.config(text="")
		elif i==9:
			result10.config(text="")
	
	return
def callback(event):
	webbrowser.open_new(event.widget.cget(r"text"))

myGUI = Tk()
query = StringVar()
myGUI.geometry("1200x700+500+300")
myGUI.title("Qoogle")
logo = Label(myGUI,text="Qoogle",font = ('Comic Sans MS',30)).pack()
entry = Entry(myGUI,textvariable=query).pack()
button = Button(myGUI,text="search",command = print_results).pack()

WL = 1100

result1 = Label(myGUI,text="",fg="blue",cursor="hand2",pady=5,wraplengt=WL)
result1.pack()
result1.bind("<Button-1>",callback)

result2 = Label(myGUI,text="",fg="blue",cursor="hand2",pady=5,wraplengt=WL)
result2.pack()
result2.bind("<Button-1>",callback)

result3 = Label(myGUI,text="",fg="blue",cursor="hand2",pady=5,wraplengt=WL)
result3.pack()
result3.bind("<Button-1>",callback)

result4 = Label(myGUI,text="",fg="blue",cursor="hand2",pady=5,wraplengt=WL)
result4.pack()
result4.bind("<Button-1>",callback)

result5 = Label(myGUI,text="",fg="blue",cursor="hand2",pady=5,wraplengt=WL)
result5.pack()
result5.bind("<Button-1>",callback)

result6 = Label(myGUI,text="",fg="blue",cursor="hand2",pady=5,wraplengt=WL)
result6.pack()
result6.bind("<Button-1>",callback)

result7 = Label(myGUI,text="",fg="blue",cursor="hand2",pady=5,wraplengt=WL)
result7.pack()
result7.bind("<Button-1>",callback)

result8 = Label(myGUI,text="",fg="blue",cursor="hand2",pady=5,wraplengt=WL)
result8.pack()
result8.bind("<Button-1>",callback)

result9 = Label(myGUI,text="",fg="blue",cursor="hand2",pady=5,wraplengt=WL)
result9.pack()
result9.bind("<Button-1>",callback)

result10 = Label(myGUI,text="",fg="blue",cursor="hand2",pady=5,wraplengt=WL)
result10.pack()
result10.bind("<Button-1>",callback)

myGUI.mainloop()
