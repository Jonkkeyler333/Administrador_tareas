import ttkbootstrap as tb
import tkinter as tk
from tkinter import messagebox
from evento import Evento

class Aplicacion:
    def __init__(self):
        self.ventana = tb.Window('JKtaks', themename='superhero')
        self.ventana.geometry("1600x650")
        self.imagen = tk.PhotoImage(file='images/img1.png')
        self.imagen2 = tk.PhotoImage(file='images/img2.png')
        frame_style = tb.Style()
        frame_style.configure('f1.TFrame', background='#05F4E9')
        self.frame_Evento=tb.Frame(style='f1.TFrame',height=500,width=1000)
        self.frame_Evento.place(x=500,y=140)
        self.eventos=[]
        self.crear_menu()
        self.crear_contenido()
        
    def crear_menu(self):
        barra_menus = tb.Menu()
        self.ventana.config(menu=barra_menus)
        menu_archivo = tb.Menu(barra_menus, tearoff=False)
        menu_archivo.add_command(label='Nuevo', accelerator="Ctrl+N")
        barra_menus.add_cascade(menu=menu_archivo, label="Archivo")

    def nuevo_Evento(self):
        if self.entrada.winfo_ismapped():  # Verifica si el botón está mapeado (visible)
            self.entrada.pack_forget()    # Oculta el botón
        else:
            self.entrada.pack()

    def confirmar_Evento(self):
        if self.entrada1.get() == '' or self.entrada1.get() == None:
            messagebox.showwarning(message="El título de su evento se encuentra vacío, intentelo otra vez", title="Error")
        else:
            name=self.entrada1.get() #obtiene el nombre del evento
            date=self.fecha.entry.get()  # Obtiene la fecha seleccionada
            hour=self.hora.get()  # Obtiene la hora seleccionada
            evento=Evento(name,date,hour)
            self.eventos.append(evento)
            self._crear_evento(evento)
            messagebox.showinfo(message=evento, title="Completado")
    
    
            
    def _crear_evento(self,e:Evento)->None:
        ficha=tb.Label(text=e.nombre,master=self.frame_Evento)
        ficha.pack(side=tb.TOP)

    def crear_contenido(self):
        ##Contenedor de botones
        self.buttonbar = tb.Frame(style='primary.TFrame')
        self.buttonbar.pack(fill=tb.X, pady=1, side=tb.TOP)

        self.b1 = tb.Button(master=self.buttonbar, image=self.imagen, compound=tb.LEFT, text='Nuevo', bootstyle='primary', command=self.nuevo_Evento)
        self.b1.pack(side=tb.LEFT, ipadx=5, ipady=5, padx=(1, 0), pady=1)

        entrada_style = tb.Style()
        entrada_style.configure('entrada.TFrame', background='#05F4E9')

        self.entrada = tb.Frame(style='entrada.TFrame')##Contenedor de entrada
        self.l1 = tb.Label(text='Ingrese el nombre de su evento', master=self.entrada, bootstyle='info,inverse')
        self.l1.pack(side=tb.LEFT, ipadx=5, ipady=5, padx=(1,2))
        self.entrada1 = tb.Entry(master=self.entrada, bootstyle="info")
        self.entrada1.pack(side=tb.LEFT, ipadx=5, ipady=5, padx=(1,6), pady=3)
        self.l2 = tb.Label(text='Ingrese la fecha de su evento ', master=self.entrada, bootstyle='info,inverse')
        self.l2.pack(side=tb.LEFT, ipadx=5, ipady=5, pady=5, padx=(0,6))
        self.fecha = tb.DateEntry(master=self.entrada, bootstyle='info')
        self.fecha.pack(padx=(0,20), side=tb.LEFT,)
        self.l3=tb.Label(text='Seleccione la hora',master=self.entrada,bootstyle='info,inverse') 
        self.l3.pack(side=tb.LEFT,padx=(0,6),pady=5,ipadx=5, ipady=5)
        self.hora = tb.Spinbox(master=self.entrada, bootstyle='info', from_=0, to=24)
        self.hora.pack(side=tb.LEFT)

        self.b2 = tb.Button(master=self.entrada, image=self.imagen2, compound=tb.LEFT, text='Confirma', bootstyle='info', command=self.confirmar_Evento)
        self.b2.pack(side=tb.LEFT, padx=(6,10))

if __name__ == "__main__":
    app = Aplicacion()
    app.ventana.mainloop()