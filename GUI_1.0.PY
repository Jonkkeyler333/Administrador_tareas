import ttkbootstrap as tb
import tkinter as tk


def nuevo_Evento():
    if entrada.winfo_ismapped():  # Verifica si el botón está mapeado (visible)
        entrada.pack_forget()    # Oculta el botón
    else:
        entrada.pack()
        

ventana=tb.Window('JKtaks',themename='superhero')

##Creando menú
barra_menus = tb.Menu()
ventana.config(menu=barra_menus)
menu_archivo = tb.Menu(barra_menus,tearoff=False)
menu_archivo.add_command(label='Nuevo',accelerator="Ctrl+N",command=print('xd'))

barra_menus.add_cascade(menu=menu_archivo, label="Archivo")

buttonbar = tb.Frame(style='primary.TFrame')
buttonbar.pack(fill=tb.X, pady=1, side=tb.TOP)


##boton de añadir evento
ruta_imagen = 'images/img1.png'
imagen = tk.PhotoImage(file=ruta_imagen)
b1=tb.Button(master=buttonbar,image=imagen,compound=tb.LEFT,text='Nuevo',bootstyle='primary',command=nuevo_Evento)
b1.pack(side=tb.LEFT, ipadx=5, ipady=5, padx=(1, 0), pady=1)

entrada_style = tb.Style()
entrada_style.configure('entrada.TFrame', background='#05F4E9')

entrada = tb.Frame(style='entrada.TFrame')
l1=tb.Label(text='Ingrese el nombre de su evento',master=entrada,bootstyle='info,inverse')
l1.pack(side=tb.LEFT,ipadx=5, ipady=5,padx=(1,2))
entrada1=tb.Entry(master=entrada,bootstyle="danger")
entrada1.pack(side=tb.LEFT, ipadx=5, ipady=5, padx=(1,6), pady=3)
l2=tb.Label(text='Ingrese la fecha de su evento ',master=entrada,bootstyle='info,inverse')
l2.pack(side=tb.LEFT,ipadx=5,ipady=5,pady=5,padx=(0,6))
fecha=tb.DateEntry(master=entrada,bootstyle="info")
fecha.pack(padx=(0,20),side=tb.LEFT)
b2=tb.Button(master=entrada,text='Confirma',bootstyle='info')
b2.pack(side=tb.LEFT,padx=(6,10))

ventana.mainloop()

