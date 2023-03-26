from tkinter import*
from PIL import Image, ImageTk 
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox


class Sposob_zycia:
	def __init__(self,root):
		self.root=root
		self.root.title("System Atlasu Zwierzat")
		self.root.geometry("1110x440+236+220")

		#==================varaibles===================
		self.var_gatunek=StringVar()
		self.var_poruszanie=StringVar()
		self.var_srodowisko=StringVar()
		self.var_kontynent=StringVar()
		self.var_tryb_zycia=StringVar()
		self.var_klimat=StringVar()

		#==================title========================
		lbl_title=Label(self.root,text="SPOSOB ZYCIA SZCZEGOLY",font=("times mew roman",18,"bold"),bg="black",fg="green",bd=4,relief=RIDGE)
		lbl_title.place(x=0,y=0,width=1110,height=50)

		# =================logo img===================== 
		img2=Image.open("C:\\Users\\Uzytkownik\\OneDrive\\Pulpit\\grafiki_bazy\\m.png") #obrazek
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
		btnFetchData=Button(labelframeleft,command=self.Fetch_gatunek,text="Zaladuj dane",font=("arial",11,"bold"),bg="black",fg="green",width=10)
		btnFetchData.place(x=310,y=2)
		
		#poruszanie
		lbl_poruszanie_ref=Label(labelframeleft,text="Poruszanie:",font=("arial",12,"bold"),padx=2,pady=6)
		lbl_poruszanie_ref.grid(row=1,column=0,sticky=W) #,textvariable=self.var_id
		combo_poruszanie=ttk.Combobox(labelframeleft,textvariable=self.var_poruszanie,font=("arial",12,"bold"),width=27,state="readonly")
		combo_poruszanie["value"]=("chodzenie"),("plyniecie"),("latanie"),("pelzanie"),("wiele_sposobow")
		combo_poruszanie.current(0)
		combo_poruszanie.grid(row=1,column=1)
		
		#srodowisko
		lbl_srodowisko_ref=Label(labelframeleft,text="Srodowisko:",font=("arial",12,"bold"),padx=2,pady=6)
		lbl_srodowisko_ref.grid(row=2,column=0,sticky=W)
		combo_srodowisko=ttk.Combobox(labelframeleft,textvariable=self.var_srodowisko,font=("arial",12,"bold"),width=27,state="readonly")
		combo_srodowisko["value"]=("lad"),("woda"),("powietrze"),("wiele")
		combo_srodowisko.current(0)
		combo_srodowisko.grid(row=2,column=1)
		
		#kontynent
		lbl_kontynent_ref=Label(labelframeleft,text="Kontynent:",font=("arial",12,"bold"),padx=2,pady=6)
		lbl_kontynent_ref.grid(row=3,column=0,sticky=W)
		enty_kontynent=ttk.Entry(labelframeleft,textvariable=self.var_kontynent,width=29,font=("arial",13,"bold"))
		enty_kontynent.grid(row=3,column=1)

		#tryb_zycia
		lbl_tryb_zycia_ref=Label(labelframeleft,text="Tryb zycia:",font=("arial",12,"bold"),padx=2,pady=6)
		lbl_tryb_zycia_ref.grid(row=4,column=0,sticky=W)
		combo_tryb_zycia=ttk.Combobox(labelframeleft,textvariable=self.var_tryb_zycia,font=("arial",12,"bold"),width=27,state="readonly")
		combo_tryb_zycia["value"]=("dzienny"),("nocny")
		combo_tryb_zycia.current(0)
		combo_tryb_zycia.grid(row=4,column=1)

		#klimat
		lbl_klimat_ref=Label(labelframeleft,text="Klimat:",font=("arial",12,"bold"),padx=2,pady=6)
		lbl_klimat_ref.grid(row=5,column=0,sticky=W)
		enty_kontynent=ttk.Entry(labelframeleft,textvariable=self.var_klimat,width=29,font=("arial",13,"bold"))
		enty_kontynent.grid(row=5,column=1)

		
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
		img3=Image.open("C:\\Users\\Uzytkownik\\OneDrive\\Pulpit\\grafiki_bazy\\p.jpg")#zmienic obrazek
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
		combo_wyszukaj["value"]=("gatunek"),("poruszanie"),("srodowisko"),("kontynent"),("tryb_zycia"),("klimat")
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

		self.Sposob_zycia_Details_Table=ttk.Treeview(details_table,column=("gatunek","poruszanie","srodowisko","kontynent","tryb_zycia","klimat"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
		
		scroll_x.pack(side=BOTTOM,fill=X)
		scroll_y.pack(side=RIGHT,fill=Y)

		scroll_x.config(command=self.Sposob_zycia_Details_Table.xview)
		scroll_y.config(command=self.Sposob_zycia_Details_Table.yview)

		self.Sposob_zycia_Details_Table.heading("gatunek", text="Gatunek")
		self.Sposob_zycia_Details_Table.heading("poruszanie", text="Poruszanie")
		self.Sposob_zycia_Details_Table.heading("srodowisko", text="Srodowisko zycia")
		self.Sposob_zycia_Details_Table.heading("kontynent", text="Kontynent,")
		self.Sposob_zycia_Details_Table.heading("tryb_zycia", text="Tryb_zycia")
		self.Sposob_zycia_Details_Table.heading("klimat", text="Klimat")

		 
		self.Sposob_zycia_Details_Table["show"]="headings"

		self.Sposob_zycia_Details_Table.column("gatunek",width=100)
		self.Sposob_zycia_Details_Table.column("poruszanie",width=100)
		self.Sposob_zycia_Details_Table.column("srodowisko",width=100)
		self.Sposob_zycia_Details_Table.column("kontynent",width=100)
		self.Sposob_zycia_Details_Table.column("tryb_zycia",width=100)
		self.Sposob_zycia_Details_Table.column("klimat",width=100)
		self.Sposob_zycia_Details_Table.pack(fill=BOTH, expand=1)

		self.Sposob_zycia_Details_Table.pack(fill=BOTH, expand=1)
		self.Sposob_zycia_Details_Table.bind("<ButtonRelease-1>",self.get_cursor)
		self.fetch_data()

	#add function
	def add_data(self):
		if self.var_gatunek.get()=="" or self.var_poruszanie.get()=="" or self.var_srodowisko.get()=="" or self.var_kontynent.get()=="":
			messagebox.showerror("Blad","Wszystkie pola sa wymagane")

		else:
			try:
				conn=mysql.connector.connect(host="localhost", username="root",passwd="root", database="projekt_koncowy")
				my_cursor=conn.cursor()
				my_cursor.execute("insert into sposob_zycia values(%s,%s,%s,%s,%s,%s)",(
																			self.var_gatunek.get(),
																			self.var_poruszanie.get(),
																			self.var_srodowisko.get(),
																			self.var_kontynent.get(),
																			self.var_tryb_zycia.get(),
																			self.var_klimat.get()
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
		my_cursor.execute("select * from sposob_zycia")
		rows=my_cursor.fetchall()
		if len(rows)!=0:
			self.Sposob_zycia_Details_Table.delete(*self.Sposob_zycia_Details_Table.get_children())
			for i in rows:
				self.Sposob_zycia_Details_Table.insert("",END,values=i)
			conn.commit()
			conn.close()

	def get_cursor(self,event=""):
		cursor_row=self.Sposob_zycia_Details_Table.focus()
		content=self.Sposob_zycia_Details_Table.item(cursor_row)
		row=content["values"]

		self.var_gatunek.set(row[0])
		self.var_gatunek.set(row[0])
		self.var_poruszanie.set(row[1])
		self.var_srodowisko.set(row[2])
		self.var_kontynent.set(row[3])
		self.var_tryb_zycia.set(row[4])
		self.var_klimat.set(row[5])

	#update function
	def update(self):
		if self.var_gatunek.get()=="" or self.var_poruszanie.get()=="" or self.var_srodowisko.get()=="" or self.var_kontynent.get()=="":
			messagebox.showerror("Blad","Wszystkie pola sa wymagane",parent=self.root)

		else:
			conn=mysql.connector.connect(host="localhost", username="root",passwd="root", database="projekt_koncowy")
			my_cursor=conn.cursor()
			my_cursor.execute("update Sposob_zycia set poruszanie=%s,srodowisko=%s,kontynent=%s,tryb_zycia=%s,klimat=%s where gatunek=%s",(

																					self.var_poruszanie.get(),
																					self.var_srodowisko.get(),
																					self.var_kontynent.get(),
																					self.var_tryb_zycia.get(),
																					self.var_klimat.get(),
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
			query="delete from Sposob_zycia where gatunek=%s"
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
		self.var_poruszanie.set(""),
		self.var_srodowisko.set(""),
		self.var_kontynent.set("")

	#search system
	def search(self):
		conn=mysql.connector.connect(host="localhost", username="root",passwd="root", database="projekt_koncowy")
		my_cursor=conn.cursor()

		my_cursor.execute("select * from sposob_zycia where "+str(self.serch_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
		rows=my_cursor.fetchall()
		if len (rows)!=0:
			self.Sposob_zycia_Details_Table.delete(*self.Sposob_zycia_Details_Table.get_children())
			for i in rows:
				self.Sposob_zycia_Details_Table.insert("",END,values=i)
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
	obj=Sposob_zycia(root)
	root.mainloop()


class my_class(object):
    pass




