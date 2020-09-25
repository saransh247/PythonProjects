from tkinter import *
from PIL import Image, ImageTk
import random
global var
global x,y,z
global dice

def logic(user,rand):
	comp=rand
	result=""
	if user==comp:
		result="Draw"
		
	elif user==dice[0]:
		if comp==dice[2]:
			result="You Win"
		elif comp==dice[1]:
			result="Computer Win"
	
	elif user==dice[1]:
		if comp==dice[0]:
			result="You Win"
		elif comp==dice[2]:
			result="Computer Win"
	elif user==dice[2]:
		if comp==dice[1]:
			result="You Win"
		elif comp==dice[0]:
			result="Computer Win"
	return result

def check(user):
	rand=random.choice(dice)

	comp = ImageTk.PhotoImage(Image.open(rand))
	users=ImageTk.PhotoImage(Image.open(user))
	
	complabel=Label(root,text="Computer's Choosen")
	complabel.grid(row=5,column=3)
	
	comp_result=Label(root,image=comp)
	comp_result.grid(row=6,column=3)
	#comp_result.configure(comp)
	comp_result.image = comp
 
	
	userlabel=Label(root,text="Your's Choosen")
	userlabel.grid(row=5, column=1)
	
	users_result=Label(root,image=users)
	users_result.grid(row=6,column=1)
	#users_result.configure(users)
	users_result.image=users

	result=logic(user,rand)
	var.set(result)

	finallabel=Label(root, textvariable=var, font="Airel 20 bold italic")
	finallabel.grid(row=4,column=2)
	
def scorefun(result,x,y,z):
	
	if result=="You Win":
		x+=1
		
	elif result=="Computer Win":
		y+=1
	elif result=="Draw":
		z+=1
	return str(x),str(y),str(z)	

if __name__ == '__main__':
	root = Tk()
	root.geometry('500x350')
	root.title('Stone Paper Scissor Game by Saransh Jain')
	x,y,z=0,0,0
	dice = ['Stone.jpg', 'Paper.jpg', 'Scissor.jpg']

	var=StringVar()
	var.set("")

	l0 = Label(root, text="")
	l0.grid(row=0,column=1)

	l1 = Label(root, text="Welcome to the game", fg = "light green", bg = "dark green",font = "Helvetica 16 bold italic")
	l1.grid(row=1,column=2)

	image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))

	stone_photo = ImageTk.PhotoImage(Image.open('Stone.jpg'))
	stone=Button(root, image=stone_photo,command=lambda: check("Stone.jpg"))
	stone.grid(row=3,column=1)
	scissor_photo = ImageTk.PhotoImage(Image.open('Scissor.jpg'))
	scissor=Button(root, image=scissor_photo,command=lambda: check("Scissor.jpg"))
	scissor.grid(row=3,column=2)
	paper_photo = ImageTk.PhotoImage(Image.open('Paper.jpg'))
	paper=Button(root, image=paper_photo,command=lambda: check("Paper.jpg"))
	paper.grid(row=3,column=3)
	roughlabel=Label(root,text="").grid(row=2,column=0)

	root.mainloop()
