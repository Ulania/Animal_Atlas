from tkinter import*
from PIL import Image, ImageTk 
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox


class Rozwoj_rozmnazanie:
	def __init__(self,root):
		self.root=root
		self.root.title("System Atlasu Zwierzat")
		self.root.geometry("1110x440+236+220")

		#==================varaibles===================
		self.var_gatunek=StringVar()
		self.var_dlugosc_ciazy=StringVar()
		self.var_ilosc_potomstwa=StringVar()
		self.var_czas_z_matka=StringVar()
		self.var_rodzaj_reprodukcji=StringVar()

		#==================title========================
		lbl_title=Label(self.root,text="ROZWOJ/ROZMNAZANIE SZCZEGOLY",font=("times mew roman",18,"bold"),bg="black",fg="green",bd=4,relief=RIDGE)
		lbl_title.place(x=0,y=0,width=1110,height=50)

		# =================logo img===================== 
		img2=Image.open("C:\\Users\\Uzytkownik\\OneDrive\\Pulpit\\grafiki_bazy\\p.png") #obrazek
		img2=img2.resize((100,40),Image.ANTIALIAS)
		self.photoimg2=ImageTk.PhotoImage(img2)

		lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
		lblimg.place(x=5,y=5,width=100,height=40)
		
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
		btnFetchData=Button(labelframeleft,command=self.Fetch_gatunek,text="Zaladuj dane",font=("arial",11,"bold"),bg="black",fg="green",width=10)
		btnFetchData.place(x=313,y=2)
		
		#dlugosc_ciazy
		lbl_dlugosc_ciazy_ref=Label(labelframeleft,text="Dlugosc ciazy:",font=("arial",12,"bold"),padx=2,pady=6)
		lbl_dlugosc_ciazy_ref.grid(row=1,column=0,sticky=W) #,textvariable=self.var_id
		enty_czas_z_matka=ttk.Entry(labelframeleft,textvariable=self.var_dlugosc_ciazy,width=29,font=("arial",13,"bold"))
		enty_czas_z_matka.grid(row=1,column=1)
		
		#ilosc_potomstwa
		lbl_ilosc_potomstwa_ref=Label(labelframeleft,text="Ile potomstwa:",font=("arial",12,"bold"),padx=2,pady=6)
		lbl_ilosc_potomstwa_ref.grid(row=2,column=0,sticky=W)
		enty_czas_z_matka=ttk.Entry(labelframeleft,textvariable=self.var_ilosc_potomstwa,width=29,font=("arial",13,"bold"))
		enty_czas_z_matka.grid(row=2,column=1)
		
		#czas_z_matka
		lbl_czas_z_matka_ref=Label(labelframeleft,text="Czas z matka:",font=("arial",12,"bold"),padx=2,pady=6)
		lbl_czas_z_matka_ref.grid(row=3,column=0,sticky=W)
		enty_czas_z_matka=ttk.Entry(labelframeleft,textvariable=self.var_czas_z_matka,width=29,font=("arial",13,"bold"))
		enty_czas_z_matka.grid(row=3,column=1)

		#rodzaj_reprodukcji
		lbl_rodzaj_reprodukcji_ref=Label(labelframeleft,text="Tryb zycia:",font=("arial",12,"bold"),padx=2,pady=6)
		lbl_rodzaj_reprodukcji_ref.grid(row=4,column=0,sticky=W)
		combo_rodzaj_reprodukcji=ttk.Combobox(labelframeleft,textvariable=self.var_rodzaj_reprodukcji,font=("arial",12,"bold"),width=27,state="readonly")
		combo_rodzaj_reprodukcji["value"]=("zyworodny"),("jajorodny")
		combo_rodzaj_reprodukcji.current(0)
		combo_rodzaj_reprodukcji.grid(row=4,column=1)

		
		#================btns======================
		btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
		btn_frame.place(x=0,y=230,width=412,height=40)

		btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",12,"bold"),bg="black",fg="green", width=9)
		btnAdd.grid(row=0,column=0,padx=1)

		btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("arial",12,"bold"),bg="black",fg="green", width=9)
		btnUpdate.grid(row=0,column=1,padx=1)

		btnDelete=Button(btn_frame,text="Delete",command=self.mDelete,font=("arial",12,"bold"),bg="black",fg="green", width=9)
		btnDelete.grid(row=0,column=2,padx=1)

		btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",12,"bold"),bg="black",fg="green", width=9)
		btnReset.grid(row=0,column=3,padx=1)
		

		#==================rightside image========================================
		img3=Image.open("C:\\Users\\Uzytkownik\\OneDrive\\Pulpit\\grafiki_bazy\\f.jpg")#zmienic obrazek
		img3=img3.resize((400,185),Image.ANTIALIAS) 
		self.photoimg3=ImageTk.PhotoImage(img3)

		lblimg=Label(self.root,image=self.photoimg3,bd=0,relief=RIDGE)
		lblimg.place(x=690,y=60,width=400,height=185)

		
		#==================table frame search system========================================
		Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Szczegoly i wyszukiwanie",font=("times mew roman",12,"bold"),padx=2)
		Table_Frame.place(x=435,y=255,width=670,height=180)
		
		lbl_wyszukaj_ref=Label(Table_Frame,text="Wyszukaj przez:",font=("arial",12,"bold"),bg="blue",fg="white")
		lbl_wyszukaj_ref.grid(row=0,column=0,sticky=W,padx=2)
		
		self.serch_var=StringVar()
		combo_wyszukaj=ttk.Combobox(Table_Frame,font=("arial",12,"bold"),textvariable=self.serch_var,width=10,state="readonly")
		combo_wyszukaj["value"]=("gatunek"),("dlugosc_ciazy"),("ilosc_potomstwa"),("czas_z_matka"),("rodzaj_reprodukcji")
		combo_wyszukaj.current(0)
		combo_wyszukaj.grid(row=0,column=1,padx=2)

		self.txt_search=StringVar()
		txtWyszukaj=ttk.Entry(Table_Frame,font=("arial",13,"bold"),textvariable=self.txt_search,width=18)
		txtWyszukaj.grid(row=0,column=2,padx=2)

		btnSearch=Button(Table_Frame, text="Wyszukaj",command=self.search,font=("arial",11,"bold"),bg="black",fg="green", width=9)
		btnSearch.grid(row=0,column=3,padx=0)

		btnShowAll=Button(Table_Frame, text="Pokaz wszystkie",command=self.fetch_data,font=("arial",11,"bold"),bg="black",fg="green", width=15)
		btnShowAll.grid(row=0,column=4,padx=1)


		#==============Show data Table========================
		details_table=Frame(Table_Frame,bd=2,relief=RIDGE)
		details_table.place(x=5,y=40,width=650,height=160)

		scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
		scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

		self.Rozwoj_rozmnazanie_Details_Table=ttk.Treeview(details_table,column=("gatunek","dlugosc_ciazy","ilosc_potomstwa","czas_z_matka","rodzaj_reprodukcji"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
		
		scroll_x.pack(side=BOTTOM,fill=X)
		scroll_y.pack(side=RIGHT,fill=Y)

		scroll_x.config(command=self.Rozwoj_rozmnazanie_Details_Table.xview)
		scroll_y.config(command=self.Rozwoj_rozmnazanie_Details_Table.yview)

		self.Rozwoj_rozmnazanie_Details_Table.heading("gatunek", text="Gatunek")
		self.Rozwoj_rozmnazanie_Details_Table.heading("dlugosc_ciazy", text="Dlugosc ciazy")
		self.Rozwoj_rozmnazanie_Details_Table.heading("ilosc_potomstwa", text="Ile potomstwa")
		self.Rozwoj_rozmnazanie_Details_Table.heading("czas_z_matka", text="Czas z matka")
		self.Rozwoj_rozmnazanie_Details_Table.heading("rodzaj_reprodukcji", text="rodzaj_reprodukcji")

		 
		self.Rozwoj_rozmnazanie_Details_Table["show"]="headings"

		self.Rozwoj_rozmnazanie_Details_Table.column("gatunek",width=100)
		self.Rozwoj_rozmnazanie_Details_Table.column("dlugosc_ciazy",width=100)
		self.Rozwoj_rozmnazanie_Details_Table.column("ilosc_potomstwa",width=100)
		self.Rozwoj_rozmnazanie_Details_Table.column("czas_z_matka",width=100)
		self.Rozwoj_rozmnazanie_Details_Table.column("rodzaj_reprodukcji",width=100)
		self.Rozwoj_rozmnazanie_Details_Table.pack(fill=BOTH, expand=1)

		self.Rozwoj_rozmnazanie_Details_Table.pack(fill=BOTH, expand=1)
		self.Rozwoj_rozmnazanie_Details_Table.bind("<ButtonRelease-1>",self.get_cursor)
		self.fetch_data()

	#add function
	def add_data(self):
		if self.var_gatunek.get()=="" or self.var_dlugosc_ciazy.get()=="" or self.var_ilosc_potomstwa.get()=="" or self.var_czas_z_matka.get()=="":
			messagebox.showerror("Blad","Wszystkie pola sa wymagane")

		else:
			try:
				conn=mysql.connector.connect(host="localhost", username="root",passwd="root", database="projekt_koncowy")
				my_cursor=conn.cursor()
				my_cursor.execute("insert into Rozwoj_rozmnazanie values(%s,%s,%s,%s,%s)",(
																			self.var_gatunek.get(),
																			self.var_dlugosc_ciazy.get(),
																			self.var_ilosc_potomstwa.get(),
																			self.var_czas_z_matka.get(),
																			self.var_rodzaj_reprodukcji.get(),
																		))
				conn.commit()
				self.fetch_data()
				conn.close()
				messagebox.showinfo("Udalo sie","Rekord zostal dodany",parent=self.root)
			except Exception as es:
				messagebox.showwarning("Ostrzezenie",f"Cos poszlo nie tak:{str(es)}",parent=self.root)

	def fetch_data(self):
		conn=mysql.connector.connect(host="localhost", username="root",passwd="root", database="projekt_koncowy")
		my_cursor=conn.cursor()
		my_cursor.execute("select * from Rozwoj_rozmnazanie")
		rows=my_cursor.fetchall()
		if len(rows)!=0:
			self.Rozwoj_rozmnazanie_Details_Table.delete(*self.Rozwoj_rozmnazanie_Details_Table.get_children())
			for i in rows:
				self.Rozwoj_rozmnazanie_Details_Table.insert("",END,values=i)
			conn.commit()
			conn.close()

	def get_cursor(self,event=""):
		cursor_row=self.Rozwoj_rozmnazanie_Details_Table.focus()
		content=self.Rozwoj_rozmnazanie_Details_Table.item(cursor_row)
		row=content["values"]

		self.var_gatunek.set(row[0])
		self.var_gatunek.set(row[0])
		self.var_dlugosc_ciazy.set(row[1])
		self.var_ilosc_potomstwa.set(row[2])
		self.var_czas_z_matka.set(row[3])
		self.var_rodzaj_reprodukcji.set(row[4])

	#update function
	def update(self):
		if self.var_gatunek.get()=="" or self.var_dlugosc_ciazy.get()=="" or self.var_ilosc_potomstwa.get()==""or self.var_czas_z_matka.get()==""  :
			messagebox.showerror("Blad","Wszystkie pola sa wymagane",parent=self.root)

		else:
			conn=mysql.connector.connect(host="localhost", username="root",passwd="root", database="projekt_koncowy")
			my_cursor=conn.cursor()
			my_cursor.execute("update Rozwoj_rozmnazanie set dlugosc_ciazy=%s,ilosc_potomstwa=%s,czas_z_matka=%s,rodzaj_reprodukcji=%s where gatunek=%s",(

																					self.var_dlugosc_ciazy.get(),
																					self.var_ilosc_potomstwa.get(),
																					self.var_czas_z_matka.get(),
																					self.var_rodzaj_reprodukcji.get(),
																					self.var_gatunek.get()
																							))
			conn.commit()
			self.fetch_data()
			conn.close()
			messagebox.showinfo("Udalo sie","Rekord zostal zminiony",parent=self.root)

	#delete function
	def mDelete(self):
		mDelete=messagebox.askyesno("Atlas zwierzat","Czy na pewno chcesz usunac rekord?",parent=self.root)
		if mDelete>0:
			conn=mysql.connector.connect(host="localhost", username="root",passwd="root", database="projekt_koncowy")
			my_cursor=conn.cursor()
			query="delete from Rozwoj_rozmnazanie where gatunek=%s"
			value=(self.var_gatunek.get(),)
			my_cursor.execute(query,value)
		else:
			if not mDelete:
				return
		conn.commit()
		self.fetch_data()
		conn.close()

	#reset function
	def reset(self):
		self.var_gatunek.set(""),
		self.var_dlugosc_ciazy.set(""),
		self.var_ilosc_potomstwa.set(""),
		self.var_czas_z_matka.set("")

	#search system
	def search(self):
		conn=mysql.connector.connect(host="localhost", username="root",passwd="root", database="projekt_koncowy")
		my_cursor=conn.cursor()

		my_cursor.execute("select * from rozwoj_rozmnazanie where "+str(self.serch_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
		rows=my_cursor.fetchall()
		if len (rows)!=0:
			self.Rozwoj_rozmnazanie_Details_Table.delete(*self.Rozwoj_rozmnazanie_Details_Table.get_children())
			for i in rows:
				self.Rozwoj_rozmnazanie_Details_Table.insert("",END,values=i)
			conn.commit()
		conn.close()


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
				messagebox.showerror("Blad","Nie znaleziono takiego gatunku",parent=self.root)
			else:
				conn.commit()
				conn.close()
	
				showDataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
				showDataframe.place(x=450,y=60,width=220,height=185) 
				
				lblId=Label(showDataframe,text="ID:",font=("arial",12,"bold"))
				lblId.place(x=0,y=0)

				lbl=Label(showDataframe,text=row,font=("arial",12,"bold"))
				lbl.place(x=90,y=0) 

				#=============typ============================
				conn=mysql.connector.connect(host="localhost", username="root",passwd="root", database="projekt_koncowy")
				my_cursor=conn.cursor()
				query=("select typ from Ogolne where Gatunek=%s")
				value=(self.var_gatunek.get(),)	
				my_cursor.execute(query,value)
				row=my_cursor.fetchone()

				lblTyp=Label(showDataframe,text="Typ:",font=("arial",12,"bold"))
				lblTyp.place(x=0,y=30)

				lb2=Label(showDataframe,text=row,font=("arial",12,"bold"))
				lb2.place(x=90,y=30) #zmienic wartosc

				#=============gromada============================
				conn=mysql.connector.connect(host="localhost", username="root",passwd="root", database="projekt_koncowy")
				my_cursor=conn.cursor()
				query=("select gromada from Ogolne where Gatunek=%s")
				value=(self.var_gatunek.get(),)	
				my_cursor.execute(query,value)
				row=my_cursor.fetchone()

				lblGromada=Label(showDataframe,text="Gromada:",font=("arial",12,"bold"))
				lblGromada.place(x=0,y=60)

				lb3=Label(showDataframe,text=row,font=("arial",12,"bold"))
				lb3.place(x=90,y=60) #zmienic wartosc

				#=============rzad============================
				conn=mysql.connector.connect(host="localhost", username="root",passwd="root", database="projekt_koncowy")
				my_cursor=conn.cursor()
				query=("select rzad from Ogolne where Gatunek=%s")
				value=(self.var_gatunek.get(),)	
				my_cursor.execute(query,value)
				row=my_cursor.fetchone()

				lblRzad=Label(showDataframe,text="Rzad:",font=("arial",12,"bold"))
				lblRzad.place(x=0,y=90)

				lb4=Label(showDataframe,text=row,font=("arial",12,"bold"))
				lb4.place(x=90,y=90) #zmienic wartosc
				
				#=============rodzina============================
				conn=mysql.connector.connect(host="localhost", username="root",passwd="root", database="projekt_koncowy")
				my_cursor=conn.cursor()
				query=("select rodzina from Ogolne where Gatunek=%s")
				value=(self.var_gatunek.get(),)	
				my_cursor.execute(query,value)
				row=my_cursor.fetchone()

				lblRodzina=Label(showDataframe,text="Rodzina:",font=("arial",12,"bold"))
				lblRodzina.place(x=0,y=120)

				lb5=Label(showDataframe,text=row,font=("arial",12,"bold"))
				lb5.place(x=90,y=120) #zmienic wartosc

				#=============rodzaj============================
				conn=mysql.connector.connect(host="localhost", username="root",passwd="root", database="projekt_koncowy")
				my_cursor=conn.cursor()
				query=("select rodzaj from Ogolne where Gatunek=%s")
				value=(self.var_gatunek.get(),)	
				my_cursor.execute(query,value)
				row=my_cursor.fetchone()

				lblRodzaj=Label(showDataframe,text="Rodzaj:",font=("arial",12,"bold"))
				lblRodzaj.place(x=0,y=150)

				lb6=Label(showDataframe,text=row,font=("arial",12,"bold"))
				lb6.place(x=90,y=150) 



if __name__ == "__main__":
	root=Tk()
	obj=Rozwoj_rozmnazanie(root)
	root.mainloop()


class my_class(object):
    pass





