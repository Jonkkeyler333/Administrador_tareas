import ttkbootstrap as tb
import os

ventana=tb.Window('JKtaks',themename='superhero')

##Creando menú
barra_menus = tb.Menu()
ventana.config(menu=barra_menus)
menu_archivo = tb.Menu(barra_menus,tearoff=False)
menu_archivo.add_command(label='Nuevo',accelerator="Ctrl+N",command=print('xd'))

barra_menus.add_cascade(menu=menu_archivo, label="Archivo")

buttonbar = tb.Frame(style='primary.TFrame')
buttonbar.pack(fill=tb.X, pady=1, side=tb.TOP)


b1=tb.Button(master=buttonbar,image='img1.png',text='Nueva',bootstyle='primary')
b1.pack()


ventana.mainloop()

