from tkinter import *
from PIL import Image, ImageTk  #pip install pillow
#from ogolne import Ogolne_Win


class AtlasZwierzatSystem:
	def __init__(self,root):
		self.root=root
		self.root.title("Atlas Zwierzat")
		self.root.geometry("1350x690+0+0")

		# =================ist img===================== podluzny obrazek na gorze
		img1=Image.open("C:\\Users\\bloom\\Desktop\\atlas_zwierząt_bazy_danych_pyhon\\grafiki_bazy\\dd.jpg")
		img1=img1.resize((1350,140),Image.ANTIALIAS)
		self.photoimg1=ImageTk.PhotoImage(img1)
		
		lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
		lblimg.place(x=0,y=0,width=1350,height=140) 

		# =================logo img===================== logo w prawym gornym rogu
		img2=Image.open("C:\\Users\\bloom\\Desktop\\atlas_zwierząt_bazy_danych_pyhon\\grafiki_bazy\\lz.jpg")
		img2=img2.resize((230,140),Image.ANTIALIAS)
		self.photoimg2=ImageTk.PhotoImage(img2)
		
		lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
		lblimg.place(x=0,y=0,width=230,height=140) 

		#==================title========================
		lbl_title=Label(self.root,text="ATLAS ZWIERZAT",font=("times mew roman",40,"bold"),bg="black",fg="green",bd=4,relief=RIDGE) #zmienic sobie kolor
		lbl_title.place(x=0,y=140,width=1350,height=50)

		#==================main frame===================
		main_frame=Frame(self.root,bd=4,relief=RIDGE)
		main_frame.place(x=0,y=190,width=1350,height=620)

		#==================menu=========================
		lbl_menu=Label(main_frame,text="MENU",font=("times mew roman", 20, "bold"),bg="black",fg="green",bd=4,relief=RIDGE)
		lbl_menu.place(x=0,y=0,width=230)

		#==================btn frame===================
		btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
		btn_frame.place(x=0,y=35,width=228,height=190)
															#command=self.Ogolne_details,
		ogolne_btn=Button(btn_frame,text="Ogolne          ", width=22, font=("times mew roman", 14, "bold"),bg="black",fg="white", bd=0,cursor="hand1") 
		ogolne_btn.grid(row=0,column=0,pady=1)

		morfologia_btn=Button(btn_frame,text="Morfologia         ", width=22, font=("times mew roman", 14, "bold"),bg="black",fg="white", bd=0,cursor="hand1") 
		morfologia_btn.grid(row=1,column=0,pady=1)

		charakterystyka_btn=Button(btn_frame,text="Charakterystyka          ", width=22, font=("times mew roman", 14, "bold"),bg="black",fg="white", bd=0,cursor="hand1") 
		charakterystyka_btn.grid(row=2,column=0,pady=1)

		sposob_zycia_btn=Button(btn_frame,text="Sposob Zycia          ", width=22, font=("times mew roman", 14, "bold"),bg="black",fg="white", bd=0,cursor="hand1") 
		sposob_zycia_btn.grid(row=3,column=0,pady=1)

		rozwoj_btn=Button(btn_frame,text="Rozwoj/Rozmnazanie          ", width=22, font=("times mew roman", 14, "bold"),bg="black",fg="white", bd=0,cursor="hand1") 
		rozwoj_btn.grid(row=4,column=0,pady=1)



		#================================= right side image ==================================================================================================================

		img3=Image.open("C:\\Users\\bloom\\Desktop\\atlas_zwierząt_bazy_danych_pyhon\\grafiki_bazy\\t_0.jpg")
		img3=img3.resize((1110,590),Image.ANTIALIAS)
		self.photoimg3=ImageTk.PhotoImage(img3)
		
		lblimg=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
		lblimg.place(x=230,y=-5,width=1115,height=500) #590


		#================================= left down side image ==================================================================================================================

		img4=Image.open("C:\\Users\\bloom\\Desktop\\atlas_zwierząt_bazy_danych_pyhon\\grafiki_bazy\\green.jpg")
		img4=img4.resize((1110,590),Image.ANTIALIAS)
		self.photoimg4=ImageTk.PhotoImage(img4)
		
		lblimg=Label(main_frame,image=self.photoimg4,bd=4,relief=RIDGE)
		lblimg.place(x=0,y=220,width=230,height=275) 
	

	#def Ogolne_details(self):
	#	self.new_window=Toplevel(self.root)
	#	self.app=Ogolne_Win(self.new_window)



if __name__ == "__main__":
	root=Tk()
	obj=AtlasZwierzatSystem(root)
	root.mainloop()


	
