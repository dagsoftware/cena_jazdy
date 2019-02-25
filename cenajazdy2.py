# -*- coding: cp1250 -*-

from Tkinter import *
from math import sqrt

class myApp:

	def vymaz(self):
		self.enta.delete(0, END)
		
		self.enta.insert(0, '0')
		self.enta.focus_force()
		
		self.entb.delete(0, END)
		self.entb.insert(2, '2')
		
		self.entc.delete(0, END)
		self.entc.insert(1, '1')

	def vyresit(self):
		try:
			self.a = float(self.enta.get())
			self.b = float(self.entb.get())
			self.c = int(self.entc.get())
			
			txt = ""
			
			#konstanty
			spotreba = 6 # l / 100 km
			cena = 1.239 # EUR / 1 l (shell martin košúty - 17.10.2015)
			kurz = 26.5 # kč / 1 EUR (globus ostrava - 17.10.2015)
			cena_km = spotreba * cena / 100 # (0.07434 - 17.10.2015)
			
			#czk = 0.09756 # cena za kilometer (program v. 0.1 - do 25.9.2015)
			cena = (cena_km*self.a)/self.b
			
			for i in range(1, self.c):
				cena = cena * 0.95
			
			cena_kc = cena * kurz
			
			txt = "%.2f € \n %.2f Kč " % (cena, cena_kc)
			
			self.lvt.configure(text=txt, font="Arial 16")

		except ValueError:
			# vypis, ze udaje neboli spravne zadane
			txt = "Chyba!\n\nMinimálne 1 údaj\n nebol zadaný správne."
			self.lvt.configure(text=txt, foreground="red")
			pass

	def __init__(self, root):
		
		root.title('Cena jazdy')
		
		self.top = Frame(root)
		self.top.pack(fill=BOTH)
		
		#top
		self.nadpisf = Frame(self.top, relief=FLAT, borderwidth=0, background='white')
		self.nadpisf.pack(fill=X, side=TOP, padx=0, pady=0, ipady=0)
		
		self.ln=Label(self.nadpisf, background='white', text="PROGRAM NA VÝPOČET CENY ZA JAZDU \n verzia 2.0 ©2015 Ďanovský Ján")
		self.ln.pack(fill=Y, padx=8, pady=4)
		
		#zadavanie
		self.zadanif = Frame(self.top,relief=GROOVE, borderwidth=2)
		self.zadanif.pack(fill=Y, side=LEFT, expand=1, padx=4, pady=4, ipady=4)
		
		self.la=Label(self.zadanif, text="Vzdialenosť (km)")
		self.la.pack(fill=X, padx=8, pady=1)
		self.enta = Entry(self.zadanif, width = 14)
		self.enta.pack(padx=8, pady=3)
		
		self.lb=Label(self.zadanif, text="Počet osôb v aute")
		self.lb.pack(fill=X, padx=8, pady=1)
		self.entb = Entry(self.zadanif, width = 14)
		self.entb.pack(padx=8, pady=3)
		
		self.lc=Label(self.zadanif, text="Poradie jazdy")
		self.lc.pack(fill=X, padx=8, pady=1)
		self.entc = Entry(self.zadanif, width = 14)
		self.entc.pack(padx=8, pady=3)
		
		self.but = Button(self.zadanif, text='Vymazať', command=self.vymaz)
		self.but.pack(padx=4, pady=4)
		
		self.vymaz()
		self.enta.focus_force()
		
		#vysledek
		self.pvysledokf = Frame(self.top, relief=FLAT, borderwidth=0)
		self.pvysledokf.pack(fill=BOTH, side=LEFT, expand=1, padx=0, pady=0, ipady=0)
		
		self.vysledokf = Frame(self.pvysledokf, relief=GROOVE, borderwidth=2)
		self.vysledokf.pack(fill=BOTH, side=TOP, expand=1, padx=4, pady=4, ipady=4)
		
		self.lv=Label(self.vysledokf, text="Cena")
		self.lv.pack(fill=Y, padx=8, pady=1)
		
		self.vysledoktf = Frame(self.vysledokf, relief=SUNKEN, borderwidth=2, background="gray")
		self.vysledoktf.pack(fill=BOTH, side=TOP, expand=1, padx=4, pady=4, ipady=4)
		
		self.lvt=Label(self.vysledoktf, text="Kliknite na „Vypočítať“", background="gray")
		self.lvt.pack(fill=Y, side=LEFT, expand=1, padx=8, pady=1)
		
		#buttons
		self.but2 = Button(self.pvysledokf, text='Vypočítať', command=self.vyresit)
		self.but2.pack(side=LEFT, padx=4, pady=4)
		
		self.but3 = Button(self.pvysledokf, text='Koniec', command=self.top.quit)
		self.but3.pack(side=RIGHT, padx=4, pady=4)


root = Tk()
app = myApp(root)
root.mainloop()

