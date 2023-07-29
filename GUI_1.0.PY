import ttkbootstrap as tb

ventana=tb.Window('JKtaks',themename='superhero')
barra_menus = tb.Menu()
# Insertarla en la ventana principal.
ventana.config(menu=barra_menus)

ventana.mainloop()

