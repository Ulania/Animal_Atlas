from tkinter import*
from PIL import Image, ImageTk 
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox


class Morfologia:
	def __init__(self,root):
		self.root=root
		self.root.title("System Atlasu Zwierzat")
		self.root.geometry("1110x440+236+220")

		#==================varaibles===================
		self.var_gatnek=StringVar()
		self.var_dlugosc=StringVar()
		self.var_nogi=StringVar()
		self.var_ogon=StringVar()
		self.var_oczy=StringVar()

		#==================title========================
		lbl_title=Label(self.root,text="MORFOLOGIA SZCZEGOLY",font=("times mew roman",18,"bold"),bg="black",fg="green",bd=4,relief=RIDGE) #zmienic sobie kolor
		lbl_title.place(x=0,y=0,width=1110,height=50)

		# =================logo img===================== 
		img2=Image.open("C:\\Users\\Uzytkownik\\OneDrive\\Pulpit\\grafiki_bazy\\b.jpg")
		img2=img2.resize((40,40),Image.ANTIALIAS)
		self.photoimg2=ImageTk.PhotoImage(img2)

		lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
		lblimg.place(x=5,y=5,width=40,height=40)
		
		#================label frame===================
		labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Wpisz dane:",font=("times mew roman",12,"bold"),padx=2)
		labelframeleft.place(x=5,y=50,width=425,height=385)

		#============labels and entrys====================
		#gatunek
		lbl_gatunek_ref=Label(labelframeleft,text="Gatunek:",font=("arial",12,"bold"),padx=2,pady=6)
		lbl_gatunek_ref.grid(row=0,column=0,sticky=W)
		enty_gatuenk=ttk.Entry(labelframeleft,textvariable=self.var_gatunek,width=20,font=("arial",13,"bold"))
		enty_gatuenk.grid(row=0,column=1,sticky=W)

		#Fetch data button
		btnFetchData=Button(labelframeleft,command=self.Fetech_gatunek,text="Zaladuj dane",font=("arial",11,"bold"),bg="black",fg="green",width=10)
		btnFetchData.place(x=310,y=2)
		
		#dlugosc_ciala
		lbl_dlugosc_ref=Label(labelframeleft,text="Dlugosc ciala:",font=("arial",12,"bold"),padx=2,pady=6)
		lbl_dlugosc_ref.grid(row=1,column=0,sticky=W) #,textvariable=self.var_id
		enty_dlugosc=ttk.Entry(labelframeleft,textvariable=self.var_dlugosc,width=29,font=("arial",13,"bold"))
		enty_dlugosc.grid(row=1,column=1)
		
		#ilosc nog
		lbl_nogi_ref=Label(labelframeleft,text="Ilosc nog:",font=("arial",12,"bold"),padx=2,pady=6)
		lbl_nogi_ref.grid(row=2,column=0,sticky=W)
		combo_nogi=ttk.Combobox(labelframeleft,textvariable=self.var_nogi,font=("arial",12,"bold"),width=27,state="readonly")
		combo_nogi["value"]=("1"),("2"),("4"),("6"),("8")
		combo_nogi.current(0)
		combo_nogi.grid(row=2,column=1)

		#ogon
		lbl_ogon_ref=Label(labelframeleft,text="Ogon:",font=("arial",12,"bold"),padx=2,pady=6)
		lbl_ogon_ref.grid(row=3,column=0,sticky=W)
		combo_ogon=ttk.Combobox(labelframeleft,textvariable=self.var_ogon,font=("arial",12,"bold"),width=27,state="readonly")
		combo_ogon["value"]=("posiada"),("brak")
		combo_ogon.current(0)
		combo_ogon.grid(row=3,column=1)

		#ilosc oczu
		lbl_oczy_ref=Label(labelframeleft,text="Ilosc oczu:",font=("arial",12,"bold"),padx=2,pady=6)
		lbl_oczy_ref.grid(row=4,column=0,sticky=W)
		enty_oczy=ttk.Entry(labelframeleft,textvariable=self.var_oczy,width=29,font=("arial",13,"bold"))
		enty_oczy.grid(row=4,column=1)

		
		#================btns======================
		btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
		btn_frame.place(x=0,y=260,width=412,height=40)

		btnAdd=Button(btn_frame, text="Add",font=("arial",12,"bold"),bg="black",fg="green", width=9)
		btnAdd.grid(row=0,column=0,padx=1)

		btnUpdate=Button(btn_frame, text="Update",font=("arial",12,"bold"),bg="black",fg="green", width=9)
		btnUpdate.grid(row=0,column=1,padx=1)

		btnDelete=Button(btn_frame, text="Delete",font=("arial",12,"bold"),bg="black",fg="green", width=9)
		btnDelete.grid(row=0,column=2,padx=1)

		btnReset=Button(btn_frame, text="Reset",font=("arial",12,"bold"),bg="black",fg="green", width=9)
		btnReset.grid(row=0,column=3,padx=1)
		

		#==================rightside image========================================
		img3=Image.open("C:\\Users\\Uzytkownik\\OneDrive\\Pulpit\\grafiki_bazy\\b.jpg")#zmienic obrazek
		img3=img2.resize((500,300),Image.ANTIALIAS) #zmienic rozmiar
		self.photoimg3=ImageTk.PhotoImage(img3) 

		lblimg=Label(self.root,image=self.photoimg3,bd=0,relief=RIDGE)
		lblimg.place(x=5,y=5,width=500,height=300)

		
		#==================table frame search system========================================
		Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Szczegoly i wyszukiwanie",font=("times mew roman",12,"bold"),padx=2)
		Table_Frame.place(x=435,y=250,width=670,height=185)
		
		lbl_wyszukaj_ref=Label(Table_Frame,text="Wyszukaj przez:",font=("arial",12,"bold"),bg="blue",fg="white")
		lbl_wyszukaj_ref.grid(row=0,column=0,sticky=W,padx=2)
		
		self.serch_var=StringVar()
		combo_wyszukaj=ttk.Combobox(Table_Frame,font=("arial",12,"bold"),width=10,state="readonly")
		combo_wyszukaj["value"]=("gatunek"),("dlugosc ciala"),("ilosc nog"),("ogon"),("ilosc oczu")
		combo_wyszukaj.current(0)
		combo_wyszukaj.grid(row=0,column=1,padx=2)

		self.txt_search=StringVar()
		txtWyszukaj=ttk.Entry(Table_Frame,font=("arial",13,"bold"),width=18)
		txtWyszukaj.grid(row=0,column=2,padx=2)

		btnSearch=Button(Table_Frame, text="Wyszukaj",font=("arial",11,"bold"),bg="black",fg="green", width=9)
		btnSearch.grid(row=0,column=3,padx=0)

		btnShowAll=Button(Table_Frame, text="Pokaz wszystkie",command=self.fetch_data,font=("arial",11,"bold"),bg="black",fg="green", width=15)
		btnShowAll.grid(row=0,column=4,padx=1)


		#==============Show data Table========================
		details_table=Frame(Table_Frame,bd=2,relief=RIDGE)
		details_table.place(x=5,y=40,width=650,height=160)

		scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
		scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

		self.Ogolne_Details_Table=ttk.Treeview(details_table,column=("gatunek","dlugosc","nogi","ogon","oczy"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
		
		scroll_x.pack(side=BOTTOM,fill=X)
		scroll_y.pack(side=RIGHT,fill=Y)

		scroll_x.config(command=self.Ogolne_Details_Table.xview)
		scroll_y.config(command=self.Ogolne_Details_Table.yview)

		self.Ogolne_Details_Table.heading("gatunek", text="Gatunek")
		self.Ogolne_Details_Table.heading("dlugosc", text="Dlugosc ciala")
		self.Ogolne_Details_Table.heading("nogi", text="Ilosc nog")
		self.Ogolne_Details_Table.heading("ogon", text="Ogon")
		self.Ogolne_Details_Table.heading("oczy", text="Ilosc oczu")

		 
		self.Ogolne_Details_Table["show"]="headings"

		self.Ogolne_Details_Table.column("gatunek",width=100)
		self.Ogolne_Details_Table.column("dlugosc",width=100)
		self.Ogolne_Details_Table.column("nogi",width=100)
		self.Ogolne_Details_Table.column("ogon",width=100)
		self.Ogolne_Details_Table.column("oczy",width=100)
		self.Ogolne_Details_Table.pack(fill=BOTH, expand=1)


        #========================All Data Fetch=========================================
	def Fetch_gatunek(self):
		if self.var_gatunek.get()=="":
			messagebox.showerror("Blad","Prosze podac gatunek",parent=self.root)
		else:
			conn=mysql.connector.connect(host="localhost", username="root",passwd="root", database="projekt_koncowy")
			my_cursor=conn.cursor()
			query=("select id from Ogolne where Gatunek=%s")
			value=(self.var_gatunek.get(),)	
			my_cursor.execute(query,value)
			row=my_cursor.fetchone()
			
			if row==None:
				messagebox.showerror("Blad","Nie znaleziono takeigo gatunku",parent=self.root)
			else:
				conn.commit()
				conn.close()
	
				showDataframe=Frame(self.root,bd=4,relief=RIDGE,padax=2)
				showDataframe.place(x=450,y=55,width=300,height=180) #zmienic wielkosc
				
				lblId=Label(showDataframe,text="ID:",font("arial",12,"bold"))
				lblId.place(x=0,y=0)

				lbl=Lable(showdataframe,text=row,font=("arial",12,"bold"))
				lbl.place(x=90,y=0) #zmienic wartosc

				#=============typ============================
				conn=mysql.connector.connect(host="localhost", username="root",passwd="root", database="projekt_koncowy")
				my_cursor=conn.cursor()
				query=("select typ from Ogolne where Gatunek=%s")
				value=(self.var_gatunek.get(),)	
				my_cursor.execute(query,value)
				row=my_cursor.fetchone()

				lblTyp=Label(showDataframe,text="Typ:",font("arial",12,"bold"))
				lblTyp.place(x=0,y=30)

				lb2=Lable(showdataframe,text=row,font=("arial",12,"bold"))
				lb2.place(x=0=90,y=30) #zmienic wartosc

				#=============gromada============================
				conn=mysql.connector.connect(host="localhost", username="root",passwd="root", database="projekt_koncowy")
				my_cursor=conn.cursor()
				query=("select gromada from Ogolne where Gatunek=%s")
				value=(self.var_gatunek.get(),)	
				my_cursor.execute(query,value)
				row=my_cursor.fetchone()

				lblGromada=Label(showDataframe,text="Gromada:",font("arial",12,"bold"))
				lblGromada.place(x=0,y=60)

				lb3=Lable(showdataframe,text=row,font=("arial",12,"bold"))
				lb3.place(x=0=90,y=60) #zmienic wartosc

				#=============rzad============================
				conn=mysql.connector.connect(host="localhost", username="root",passwd="root", database="projekt_koncowy")
				my_cursor=conn.cursor()
				query=("select rzad from Ogolne where Gatunek=%s")
				value=(self.var_gatunek.get(),)	
				my_cursor.execute(query,value)
				row=my_cursor.fetchone()

				lblRzad=Label(showDataframe,text="Rzad:",font("arial",12,"bold"))
				lblRzad.place(x=0,y=90)

				lb4=Lable(showdataframe,text=row,font=("arial",12,"bold"))
				lb4.place(x=0=90,y=90) #zmienic wartosc
				
				#=============rodzina============================
				conn=mysql.connector.connect(host="localhost", username="root",passwd="root", database="projekt_koncowy")
				my_cursor=conn.cursor()
				query=("select rodzina from Ogolne where Gatunek=%s")
				value=(self.var_gatunek.get(),)	
				my_cursor.execute(query,value)
				row=my_cursor.fetchone()

				lblRodzina=Label(showDataframe,text="Rodzina:",font("arial",12,"bold"))
				lblRodzina.place(x=0,y=120)

				lb5=Lable(showdataframe,text=row,font=("arial",12,"bold"))
				lb5.place(x=0=90,y=120) #zmienic wartosc

				#=============rodzaj============================
				conn=mysql.connector.connect(host="localhost", username="root",passwd="root", database="projekt_koncowy")
				my_cursor=conn.cursor()
				query=("select rodzaj from Ogolne where Gatunek=%s")
				value=(self.var_gatunek.get(),)	
				my_cursor.execute(query,value)
				row=my_cursor.fetchone()

				lblRodzaj=Label(showDataframe,text="Rodzaj:",font("arial",12,"bold"))
				lblRodzaj.place(x=0,y=120)

				lb6=Lable(showdataframe,text=row,font=("arial",12,"bold"))
				lb6.place(x=0=90,y=120) #zmienic wartosc

				





				


		
		
	


if __name__ == "__main__":
	root=Tk()
	obj=Morfologia(root)
	root.mainloop()


