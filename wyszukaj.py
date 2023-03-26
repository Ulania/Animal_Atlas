from tkinter import*
from PIL import Image, ImageTk 
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox


class Wyszukaj:
	def __init__(self,root):
		self.root=root
		self.root.title("System Atlasu Zwierzat")
		self.root.geometry("1110x440+236+220")

		#==================varaibles===================
		self.var_gatunek=StringVar()
		
		#==================title========================
		lbl_title=Label(self.root,text="WYSZUKAJ",font=("times mew roman",18,"bold"),bg="black",fg="green",bd=4,relief=RIDGE)
		lbl_title.place(x=0,y=0,width=1110,height=50)

		# =================logo img===================== 
		img2=Image.open("C:\\Users\\Uzytkownik\\OneDrive\\Pulpit\\grafiki_bazy\\zz.png")
		img2=img2.resize((40,40),Image.ANTIALIAS)
		self.photoimg2=ImageTk.PhotoImage(img2)

		lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
		lblimg.place(x=5,y=5,width=40,height=40)

		#==================rightside image========================================
		img3=Image.open("C:\\Users\\Uzytkownik\\OneDrive\\Pulpit\\grafiki_bazy\\pies.jpg")#zmienic obrazek
		img3=img3.resize((350,370),Image.ANTIALIAS) 
		self.photoimg3=ImageTk.PhotoImage(img3)

		lblimg=Label(self.root,image=self.photoimg3,bd=0,relief=RIDGE)
		lblimg.place(x=745,y=60,width=350,height=370)

		
		#==================Ogolne i Morfologia frames========================================
		Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Ogolne i Morfologia:",font=("times mew roman",12,"bold"),padx=2)
		Table_Frame.place(x=5,y=50,width=350,height=190)

		self.serch_ogolne=StringVar()
		combo_wyszukaj=ttk.Combobox(Table_Frame,font=("arial",12,"bold"),textvariable=self.serch_ogolne,width=10,state="readonly")
		combo_wyszukaj["value"]=("gatunek","gromada","typ ","rzad","rodzina","rodzaj")
		combo_wyszukaj.current(0)
		combo_wyszukaj.grid(row=0,column=0,padx=3)

		self.serch_morfologia=StringVar()
		combo_wyszukaj=ttk.Combobox(Table_Frame,font=("arial",12,"bold"),textvariable=self.serch_morfologia,width=10,state="readonly")
		combo_wyszukaj["value"]=("dlugosc","nogi","ogon","oczy","masa")
		combo_wyszukaj.current(0)
		combo_wyszukaj.grid(row=0,column=1,padx=2)
		
		btnSearch=Button(Table_Frame, text="Wyszukaj",command=self.search,font=("arial",11,"bold"),bg="black",fg="green", width=9)
		btnSearch.grid(row=0,column=2,padx=4)



		#==================Ogolne i Charakterystyka frames========================================
		Table_Frame_char=LabelFrame(self.root,bd=2,relief=RIDGE,text="Ogolne i Charakterystyka:",font=("times mew roman",12,"bold"),padx=2)
		Table_Frame_char.place(x=5,y=240,width=350,height=190)

		self.serch_ogolne_char=StringVar()
		combo_wyszukaj_char=ttk.Combobox(Table_Frame_char,font=("arial",12,"bold"),textvariable=self.serch_ogolne_char,width=10,state="readonly")
		combo_wyszukaj_char["value"]=("gatunek","gromada","typ ","rzad","rodzina","rodzaj")
		combo_wyszukaj_char.current(0)
		combo_wyszukaj_char.grid(row=0,column=0,padx=3)

		self.serch_charakterystyka=StringVar()
		combo_wyszukaj_char=ttk.Combobox(Table_Frame_char,font=("arial",12,"bold"),textvariable=self.serch_charakterystyka,width=10,state="readonly")
		combo_wyszukaj_char["value"]=("dlugosc_zycia","masa_max","masa_min","symetria","cieplota")
		combo_wyszukaj_char.current(0)
		combo_wyszukaj_char.grid(row=0,column=1,padx=2)

		btnSearch_char=Button(Table_Frame_char, text="Wyszukaj",command=self.search_char,font=("arial",11,"bold"),bg="black",fg="green", width=9)
		btnSearch_char.grid(row=0,column=2,padx=4)



		#==================Ogolne i Sposob zycia frames========================================
		Table_Frame_spos=LabelFrame(self.root,bd=2,relief=RIDGE,text="Ogolne i Sposob zycia:",font=("times mew roman",12,"bold"),padx=2)
		Table_Frame_spos.place(x=375,y=50,width=350,height=190)

		self.serch_ogolne_spos=StringVar()
		combo_wyszukaj_spos=ttk.Combobox(Table_Frame_spos,font=("arial",12,"bold"),textvariable=self.serch_ogolne_spos,width=10,state="readonly")
		combo_wyszukaj_spos["value"]=("gatunek","gromada","typ ","rzad","rodzina","rodzaj")
		combo_wyszukaj_spos.current(0)
		combo_wyszukaj_spos.grid(row=0,column=0,padx=3)

		self.serch_sposob_zycia=StringVar()
		combo_wyszukaj_spos=ttk.Combobox(Table_Frame_spos,font=("arial",12,"bold"),textvariable=self.serch_sposob_zycia,width=10,state="readonly")
		combo_wyszukaj_spos["value"]=("poruszanie","srodowisko","kontynent","tryb_zycia","klimat")
		combo_wyszukaj_spos.current(0)
		combo_wyszukaj_spos.grid(row=0,column=1,padx=2)

		btnSearch_spos=Button(Table_Frame_spos, text="Wyszukaj",command=self.search_spos,font=("arial",11,"bold"),bg="black",fg="green", width=9)
		btnSearch_spos.grid(row=0,column=2,padx=4)


		#==================Ogolne i Rozwoj rozmnazanie frames========================================
		Table_Frame_rozw=LabelFrame(self.root,bd=2,relief=RIDGE,text="Ogolne i Rozwoj/rozmnazanie:",font=("times mew roman",12,"bold"),padx=2)
		Table_Frame_rozw.place(x=375,y=240,width=350,height=190)

		self.serch_ogolne_rozw=StringVar()
		combo_wyszukaj_rozw=ttk.Combobox(Table_Frame_rozw,font=("arial",12,"bold"),textvariable=self.serch_ogolne_rozw,width=10,state="readonly")
		combo_wyszukaj_rozw["value"]=("gatunek","gromada","typ ","rzad","rodzina","rodzaj")
		combo_wyszukaj_rozw.current(0)
		combo_wyszukaj_rozw.grid(row=0,column=0,padx=3)

		self.serch_rozwoj_rozmnazanie=StringVar()
		combo_wyszukaj_rozw=ttk.Combobox(Table_Frame_rozw,font=("arial",12,"bold"),textvariable=self.serch_rozwoj_rozmnazanie,width=10,state="readonly")
		combo_wyszukaj_rozw["value"]=("dlugosc_ciazy","ilosc_potomstwa","czas_z_matka","rodzaj_reprodukcji")
		combo_wyszukaj_rozw.current(0)
		combo_wyszukaj_rozw.grid(row=0,column=1,padx=2)

		btnSearch_rozw=Button(Table_Frame_rozw, text="Wyszukaj",command=self.search_rozw,font=("arial",11,"bold"),bg="black",fg="green", width=9)
		btnSearch_rozw.grid(row=0,column=2,padx=4)



		#==============Ogolne i Morfologia - Show data Table========================
		details_table=Frame(Table_Frame,bd=2,relief=RIDGE)
		details_table.place(x=5,y=40,width=245,height=120)

		scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
		scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

		self.Morfologia_Details_Table=ttk.Treeview(details_table,column=(str(self.serch_ogolne.get()),str(self.serch_morfologia.get())),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
		
		scroll_x.pack(side=BOTTOM,fill=X)
		scroll_y.pack(side=RIGHT,fill=Y)

		scroll_x.config(command=self.Morfologia_Details_Table.xview)
		scroll_y.config(command=self.Morfologia_Details_Table.yview)

		self.Morfologia_Details_Table.heading(str(self.serch_ogolne.get()), text=" ")
		self.Morfologia_Details_Table.heading(str(self.serch_morfologia.get()), text=" ")
		 
		self.Morfologia_Details_Table["show"]="headings"

		self.Morfologia_Details_Table.column("gatunek", width=100)
		self.Morfologia_Details_Table.column(str(self.serch_morfologia.get()), width=100)


		self.Morfologia_Details_Table.pack(fill=BOTH, expand=1)
		self.Morfologia_Details_Table.bind("<ButtonRelease-1>",self.get_cursor)



		#==============Ogolne i Charakterystyka - Show data Table========================
		details_table_char=Frame(Table_Frame_char,bd=2,relief=RIDGE)
		details_table_char.place(x=5,y=40,width=245,height=120)

		scroll_x=ttk.Scrollbar(details_table_char,orient=HORIZONTAL)
		scroll_y=ttk.Scrollbar(details_table_char,orient=VERTICAL)

		self.Charakterystyka_Details_Table=ttk.Treeview(details_table_char,column=(str(self.serch_ogolne_char.get()),str(self.serch_charakterystyka.get())),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
		
		scroll_x.pack(side=BOTTOM,fill=X)
		scroll_y.pack(side=RIGHT,fill=Y)

		scroll_x.config(command=self.Charakterystyka_Details_Table.xview)
		scroll_y.config(command=self.Charakterystyka_Details_Table.yview)

		self.Charakterystyka_Details_Table.heading(str(self.serch_ogolne_char.get()), text=" ")
		self.Charakterystyka_Details_Table.heading(str(self.serch_charakterystyka.get()), text=" ")
		 
		self.Charakterystyka_Details_Table["show"]="headings"

		self.Charakterystyka_Details_Table.column("gatunek", width=100)
		self.Charakterystyka_Details_Table.column(str(self.serch_charakterystyka.get()), width=100)


		self.Charakterystyka_Details_Table.pack(fill=BOTH, expand=1)
		self.Charakterystyka_Details_Table.bind("<ButtonRelease-1>",self.get_cursor_char)



		#==============Ogolne i Sposob zycia - Show data Table========================
		details_table_spos=Frame(Table_Frame_spos,bd=2,relief=RIDGE)
		details_table_spos.place(x=5,y=40,width=245,height=120)

		scroll_x=ttk.Scrollbar(details_table_spos,orient=HORIZONTAL)
		scroll_y=ttk.Scrollbar(details_table_spos,orient=VERTICAL)

		self.Sposob_zycia_Details_Table=ttk.Treeview(details_table_spos,column=(str(self.serch_ogolne_spos.get()),str(self.serch_sposob_zycia.get())),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
		
		scroll_x.pack(side=BOTTOM,fill=X)
		scroll_y.pack(side=RIGHT,fill=Y)

		scroll_x.config(command=self.Sposob_zycia_Details_Table.xview)
		scroll_y.config(command=self.Sposob_zycia_Details_Table.yview)

		self.Sposob_zycia_Details_Table.heading(str(self.serch_ogolne_spos.get()), text=" ")
		self.Sposob_zycia_Details_Table.heading(str(self.serch_sposob_zycia.get()), text=" ")
		 
		self.Sposob_zycia_Details_Table["show"]="headings"

		self.Sposob_zycia_Details_Table.column("gatunek", width=100)
		self.Sposob_zycia_Details_Table.column(str(self.serch_sposob_zycia.get()), width=100)


		self.Sposob_zycia_Details_Table.pack(fill=BOTH, expand=1)
		self.Sposob_zycia_Details_Table.bind("<ButtonRelease-1>",self.get_cursor_spos)


		#==============Ogolne i Rozwoj/rozmnazanie - Show data Table========================
		details_table_rozw=Frame(Table_Frame_rozw,bd=2,relief=RIDGE)
		details_table_rozw.place(x=5,y=40,width=245,height=120)

		scroll_x=ttk.Scrollbar(details_table_rozw,orient=HORIZONTAL)
		scroll_y=ttk.Scrollbar(details_table_rozw,orient=VERTICAL)

		self.Rozwoj_rozmnazanie_Details_Table=ttk.Treeview(details_table_rozw,column=(str(self.serch_ogolne_rozw.get()),str(self.serch_rozwoj_rozmnazanie.get())),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
		
		scroll_x.pack(side=BOTTOM,fill=X)
		scroll_y.pack(side=RIGHT,fill=Y)

		scroll_x.config(command=self.Rozwoj_rozmnazanie_Details_Table.xview)
		scroll_y.config(command=self.Rozwoj_rozmnazanie_Details_Table.yview)

		self.Rozwoj_rozmnazanie_Details_Table.heading(str(self.serch_ogolne_rozw.get()), text=" ")
		self.Rozwoj_rozmnazanie_Details_Table.heading(str(self.serch_rozwoj_rozmnazanie.get()), text=" ")
		 
		self.Rozwoj_rozmnazanie_Details_Table["show"]="headings"

		self.Rozwoj_rozmnazanie_Details_Table.column("gatunek", width=100)
		self.Rozwoj_rozmnazanie_Details_Table.column(str(self.serch_rozwoj_rozmnazanie.get()), width=100)


		self.Rozwoj_rozmnazanie_Details_Table.pack(fill=BOTH, expand=1)
		self.Rozwoj_rozmnazanie_Details_Table.bind("<ButtonRelease-1>",self.get_cursor_rozw)



	#get_cursor ogolne-morfologia
	def get_cursor(self,event=""):
		cursor_row=self.Morfologia_Details_Table.focus()
		content=self.Morfologia_Details_Table.item(cursor_row)
		row=content["values"]


	#search system ogolne-morfologia	
	def search(self):
		conn=mysql.connector.connect(host="localhost", username="root",passwd="root", database="projekt_koncowy")
		my_cursor=conn.cursor()
			
		sql = "SELECT \
		ogolne."+str(self.serch_ogolne.get())+", \
		morfologia."+str(self.serch_morfologia.get())+" \
		FROM ogolne \
		INNER JOIN morfologia ON morfologia.gatunek = ogolne.gatunek"

		my_cursor.execute(sql)
		rows=my_cursor.fetchall()
		if len (rows)!=0:
			self.Morfologia_Details_Table.delete(*self.Morfologia_Details_Table.get_children())
			for i in rows:
				self.Morfologia_Details_Table.insert("",END,values=i)
			conn.commit()
		conn.close()


	#get_cursor ogolne-charakterystyka
	def get_cursor_char(self,event=""):
		cursor_row=self.Charakterystyka_Details_Table.focus()
		content=self.Charakterystyka_Details_Table.item(cursor_row)
		row=content["values"]


	#search system ogolne-charakterystyka
	def search_char(self):
		conn=mysql.connector.connect(host="localhost", username="root",passwd="root", database="projekt_koncowy")
		my_cursor=conn.cursor()
			
		sql_char = "SELECT \
		ogolne."+str(self.serch_ogolne_char.get())+", \
		charakterystyka."+str(self.serch_charakterystyka.get())+" \
		FROM ogolne \
		INNER JOIN charakterystyka ON charakterystyka.gatunek = ogolne.gatunek"

		my_cursor.execute(sql_char)
		rows=my_cursor.fetchall()
		if len (rows)!=0:
			self.Charakterystyka_Details_Table.delete(*self.Charakterystyka_Details_Table.get_children())
			for i in rows:
				self.Charakterystyka_Details_Table.insert("",END,values=i)
			conn.commit()
		conn.close()


	#get_cursor ogolne-sposob_zycia
	def get_cursor_spos(self,event=""):
		cursor_row=self.Sposob_zycia_Details_Table.focus()
		content=self.Sposob_zycia_Details_Table.item(cursor_row)
		row=content["values"]


	#search system ogolne-sposob	
	def search_spos(self):
		conn=mysql.connector.connect(host="localhost", username="root",passwd="root", database="projekt_koncowy")
		my_cursor=conn.cursor()
			
		sql_spos = "SELECT \
		ogolne."+str(self.serch_ogolne_spos.get())+", \
		sposob_zycia."+str(self.serch_sposob_zycia.get())+" \
		FROM ogolne \
		INNER JOIN sposob_zycia ON sposob_zycia.gatunek = ogolne.gatunek"

		my_cursor.execute(sql_spos)
		rows=my_cursor.fetchall()
		if len (rows)!=0:
			self.Sposob_zycia_Details_Table.delete(*self.Sposob_zycia_Details_Table.get_children())
			for i in rows:
				self.Sposob_zycia_Details_Table.insert("",END,values=i)
			conn.commit()
		conn.close()


		#get_cursor ogolne-sposob_zycia
	def get_cursor_rozw(self,event=""):
		cursor_row=self.Rozwoj_rozmnazanie_Details_Table.focus()
		content=self.Rozwoj_rozmnazanie_Details_Table.item(cursor_row)
		row=content["values"]


	#search system ogolne-rozwoj/rozmnazanie	
	def search_rozw(self):
		conn=mysql.connector.connect(host="localhost", username="root",passwd="root", database="projekt_koncowy")
		my_cursor=conn.cursor()
			
		sql_rozw = "SELECT \
		ogolne."+str(self.serch_ogolne_rozw.get())+", \
		rozwoj_rozmnazanie."+str(self.serch_rozwoj_rozmnazanie.get())+" \
		FROM ogolne \
		INNER JOIN rozwoj_rozmnazanie ON rozwoj_rozmnazanie.gatunek = ogolne.gatunek"

		my_cursor.execute(sql_rozw)
		rows=my_cursor.fetchall()
		if len (rows)!=0:
			self.Rozwoj_rozmnazanie_Details_Table.delete(*self.Rozwoj_rozmnazanie_Details_Table.get_children())
			for i in rows:
				self.Rozwoj_rozmnazanie_Details_Table.insert("",END,values=i)
			conn.commit()
		conn.close()












if __name__ == "__main__":
	root=Tk()
	obj=Wyszukaj(root)
	root.mainloop()


