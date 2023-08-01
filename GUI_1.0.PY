# import ttkbootstrap as tb
# import tkinter as tk
# from tkinter import messagebox

# def nuevo_Evento()->None:
#     if entrada.winfo_ismapped():  # Verifica si el botón está mapeado (visible)
#         entrada.pack_forget()    # Oculta el botón
#     else:
#         entrada.pack()

# def confirmar_Evento()->None:
#     if entrada1.get()=='' or entrada1.get()==None:
#         messagebox.showwarning(message="El título de su evento se encuentra vacío, intentelo otra vez", title="Error")
#     else:
#         print(entrada1.get())
#         print(fecha.entry.get())

# ventana=tb.Window('JKtaks',themename='superhero')

# ##Creando menú
# barra_menus = tb.Menu()
# ventana.config(menu=barra_menus)
# menu_archivo = tb.Menu(barra_menus,tearoff=False)
# menu_archivo.add_command(label='Nuevo',accelerator="Ctrl+N",command=print('xd'))

# barra_menus.add_cascade(menu=menu_archivo, label="Archivo")


# ##Contenedor de botones
# buttonbar = tb.Frame(style='primary.TFrame')
# buttonbar.pack(fill=tb.X, pady=1, side=tb.TOP)


# ##boton de añadir evento
# ruta_imagen = 'images/img1.png'
# imagen = tk.PhotoImage(file=ruta_imagen) ##imagen boton
# b1=tb.Button(master=buttonbar,image=imagen,compound=tb.LEFT,text='Nuevo',bootstyle='primary',command=nuevo_Evento)
# b1.pack(side=tb.LEFT, ipadx=5, ipady=5, padx=(1, 0), pady=1)

# entrada_style = tb.Style()
# entrada_style.configure('entrada.TFrame', background='#05F4E9')

# entrada = tb.Frame(style='entrada.TFrame')##Contenedor de entrada
# l1=tb.Label(text='Ingrese el nombre de su evento',master=entrada,bootstyle='info,inverse')
# l1.pack(side=tb.LEFT,ipadx=5, ipady=5,padx=(1,2))
# entrada1=tb.Entry(master=entrada,bootstyle="info")
# entrada1.pack(side=tb.LEFT, ipadx=5, ipady=5, padx=(1,6), pady=3)
# l2=tb.Label(text='Ingrese la fecha de su evento ',master=entrada,bootstyle='info,inverse')
# l2.pack(side=tb.LEFT,ipadx=5,ipady=5,pady=5,padx=(0,6))
# fecha=tb.DateEntry(master=entrada,bootstyle="info")
# fecha.pack(padx=(0,20),side=tb.LEFT)
# hora=tb.Spinbox(master=entrada,bootstyle='info',from_=00,to=24)
# hora.pack(side=tb.LEFT)

# ##ruta imagen 2
# ruta_imagen2='images/img2.png'
# imagen2=tk.PhotoImage(file=ruta_imagen2)
# b2=tb.Button(master=entrada,image=imagen2,compound=tb.LEFT,text='Confirma',bootstyle='info',command=confirmar_Evento)
# b2.pack(side=tb.LEFT,padx=(6,10))


# ventana.mainloop()



import ttkbootstrap as tb
import tkinter as tk
from tkinter import messagebox

class Aplicacion:
    def __init__(self):
        self.ventana = tb.Window('JKtaks', themename='superhero')
        self.imagen = tk.PhotoImage(file='images/img1.png')
        self.imagen2 = tk.PhotoImage(file='images/img2.png')
        self.crear_menu()
        self.crear_contenido()
        
    def crear_menu(self):
        barra_menus = tb.Menu()
        self.ventana.config(menu=barra_menus)
        menu_archivo = tb.Menu(barra_menus, tearoff=False)
        menu_archivo.add_command(label='Nuevo', accelerator="Ctrl+N", command=print('xd'))
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
            print(self.entrada1.get())
            print(self.fecha.get_date())  # Obtiene la fecha seleccionada
            print(self.hora.get())        # Obtiene la hora seleccionada

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
        self.fecha = tb.DateEntry(master=self.entrada, bootstyle="info")
        self.fecha.pack(padx=(0,20), side=tb.LEFT)
        self.hora = tb.Spinbox(master=self.entrada, bootstyle='info', from_=0, to=24)
        self.hora.pack(side=tb.LEFT)

        self.b2 = tb.Button(master=self.entrada, image=self.imagen2, compound=tb.LEFT, text='Confirma', bootstyle='info', command=self.confirmar_Evento)
        self.b2.pack(side=tb.LEFT, padx=(6,10))

if __name__ == "__main__":
    app = Aplicacion()
    app.ventana.mainloop()
