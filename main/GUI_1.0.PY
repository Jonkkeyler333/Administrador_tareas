import ttkbootstrap as tb
import tkinter as tk
from tkinter import messagebox
from evento import Evento
import csv , os

class Aplicacion:
    def __init__(self)->None:
        self.ventana = tb.Window('JKtaks', themename='superhero')
        self.ventana.geometry("1600x700")
        self.imagen = tk.PhotoImage(file='images/img1.png')
        self.imagen2 = tk.PhotoImage(file='images/img2.png')
        self.imagen3=tk.PhotoImage(file='images/img3.png')
        self.imagen4=tk.PhotoImage(file='images/img4.png')
        self.eventos=[]
        self.posiciones=[]
        self.foldername = 'data_files'
        self.filename = os.path.join(self.foldername, 'data.csv')
        self.ventana.iconbitmap('images/icono.ico')
        self.crear_contenido()
        self.crear_menu()
        
    def crear_menu(self)->None:
        barra_menus = tb.Menu()
        self.ventana.config(menu=barra_menus)
        menu_archivo = tb.Menu(barra_menus, tearoff=False)
        menu_archivo.add_command(label='Nuevo', accelerator="Ctrl+N")
        barra_menus.add_cascade(menu=menu_archivo, label="Archivo")

    def _open(self)->None:
        self.eventos.clear()
        lista_archivos = os.listdir(self.foldername)  ##Se le pasa como argumento el directorio y devuelve el nombre de los archivos dentro de el
        if not lista_archivos:
            print(self.filename)
        else:
            with open(self.filename, mode='r', newline='') as archivo_csv:
                lector_csv=csv.reader(archivo_csv) 
                for fila in lector_csv:
                    if len(fila)>=3 :
                        accept=False
                        if len(self.eventos)==0:
                                accept=True
                        else:
                            for elem in self.eventos:
                                if elem.nombre == fila[0]:
                                    accept=False
                                    
                                else:
                                    accept=True
                        if accept: 
                            e=Evento(fila[0],fila[1],fila[2])
                            self.eventos.append(e)
                            self._crear_evento(e)

    def nuevo_Evento(self):
        """Activa el panel para la configuración del evento
        """
        if self.entrada.winfo_ismapped():  # Verifica si el botón está mapeado (visible)
            self.entrada.pack_forget()    # Oculta el botón
        else:
            self.entrada.pack(side=tb.TOP,pady=(0,20))

    def confirmar_Evento(self):
        if self.entrada1.get() == '' or self.entrada1.get() == None:
            messagebox.showwarning(message="El título de su evento se encuentra vacío, intentelo otra vez", title="Error")
        elif self.hora.get()=='' or self.hora.get()==None:
            messagebox.showwarning(message="Recuerde configurar la hora de su evento", title="Error")
        else:
            name=self.entrada1.get() #obtiene el nombre del evento
            date=self.fecha.entry.get()  # Obtiene la fecha seleccionada
            hour=self.hora.get()  # Obtiene la hora seleccionada
            evento=Evento(name,date,hour)
            self.eventos.append(evento)
            self._crear_evento(evento)
            messagebox.showinfo(message=evento, title="Completado")
            self.entrada1.delete(0, tk.END)
            self.hora.delete(0, tk.END)
            self._save_Data()
     
    def _crear_evento(self,e:Evento)->None:
        """Crea la representación visual del evento

        :param e: El evento a ser representado
        :type e: Evento
        """
        estilo_boton = tb.Style()
        estilo_boton.configure('b1.TButton',font=('Arial',10))
        pos=self._generar_pos()
        ficha=tb.Button(text=e.nombre,master=self.contenedor,style='b1.TButton',image=self.imagen3,compound=tb.LEFT)
        ficha.grid(row=pos[0],column=pos[1],padx=10,pady=10)
        
    def _generar_pos(self)->list:
        """Genera la posición para ubicar al boton

        :return: _description_
        :rtype: list
        """
        posicion=[]
        for k in range(0,5):
            for j in range(0,5):
                posicion=[k,j]
                if posicion not in self.posiciones:
                    self.posiciones.append(posicion)
                    return posicion
    
    def _busqueda(self):
        ventana_secundaria=tb.Toplevel('Búsqueda')
        ventana_secundaria.geometry("800x400")
        
        l=tb.Label(text='Ingrese los parametros de búsqueda',bootstyle='info,inverse',master=ventana_secundaria,font=('Arial',11))
        l.pack(side=tb.TOP,pady=20)
        
        f=tb.Frame(master=ventana_secundaria)
        f.pack(side=tb.TOP,pady=(0,30))
        l1=tb.Label(text='Nombre del evento ',font=('Arial',10),bootstyle='info',master=f)
        l1.pack(side=tb.LEFT)
        b=tb.Checkbutton(bootstyle="round-toggle",master=f)
        b.pack(side=tb.LEFT)
        e=tb.Entry(master=f)
        e.pack(side=tb.LEFT)
        
        f1=tb.Frame(master=ventana_secundaria)
        f1.pack(side=tb.TOP,pady=(0,30))
        l2=tb.Label(text='Nombre del evento ',font=('Arial',10),bootstyle='info',master=f1)
        l2.pack(side=tb.LEFT)
        b1=tb.Checkbutton(bootstyle="round-toggle",master=f1)
        b1.pack(side=tb.LEFT)
        e1=tb.Entry(master=f1)
        e1.pack(side=tb.LEFT)
        
        f2=tb.Frame(master=ventana_secundaria)
        f2.pack(side=tb.TOP,pady=(0,30))
        l3=tb.Label(text='Nombre del evento ',font=('Arial',10),bootstyle='info',master=f2)
        l3.pack(side=tb.LEFT)
        b2=tb.Checkbutton(bootstyle="round-toggle",master=f2)
        b2.pack(side=tb.LEFT)
        e2=tb.Entry(master=f2)
        e2.pack(side=tb.LEFT)
        
        ventana_secundaria.mainloop()

    def crear_contenido(self):
        """Crea todo el contenido de la interfaz
        """
        ##Contenedor de botones
        self.buttonbar = tb.Frame(style='primary.TFrame')
        self.buttonbar.pack(fill=tb.X, pady=1, side=tb.TOP)
        
        self.b1 = tb.Button(master=self.buttonbar, image=self.imagen, compound=tb.LEFT, text='Nuevo', bootstyle='primary', command=self.nuevo_Evento)
        self.b1.pack(side=tb.LEFT, ipadx=5, ipady=5, padx=(1, 0), pady=1)
        
        self.b2=tb.Button(master=self.buttonbar,text='Buscar',bootstyle='primary',compound=tb.LEFT,image=self.imagen4,command=self._busqueda)
        self.b2.pack(side=tb.LEFT,ipadx=5,ipady=5,padx=(1, 0),pady=1)

        entrada_style = tb.Style()
        entrada_style.configure('entrada.TFrame', background='#05F4E9')
        self.entrada = tb.Frame(style='entrada.TFrame')##Contenedor de entrada
        
        ##Contenedor de eventos
        self.contenedor = tb.Labelframe(text='Eventos', padding=10,)
        self.contenedor.pack(side=tb.TOP, fill=tb.BOTH, expand=tb.YES,padx=(20,20),pady=(0,20)) 
        
        self.l1 = tb.Label(text='Ingrese el nombre de su evento', master=self.entrada, bootstyle='info,inverse',font=('Arial',9))
        self.l1.pack(side=tb.LEFT, ipadx=5, ipady=5, padx=(1,2))
        self.entrada1 = tb.Entry(master=self.entrada, bootstyle="info")  ##Nombre del evento
        self.entrada1.pack(side=tb.LEFT, ipadx=5, ipady=5, padx=(1,6), pady=3)
        self.l2 = tb.Label(text='Ingrese la fecha de su evento ', master=self.entrada, bootstyle='info,inverse',font=('Arial',9))
        self.l2.pack(side=tb.LEFT, ipadx=5, ipady=5, pady=5, padx=(0,6))
        self.fecha = tb.DateEntry(master=self.entrada, bootstyle='info')
        self.fecha.pack(padx=(0,20), side=tb.LEFT,)
        self.l3=tb.Label(text='Seleccione la hora',master=self.entrada,bootstyle='info,inverse',font=('Arial',9)) 
        self.l3.pack(side=tb.LEFT,padx=(0,6),pady=5,ipadx=5, ipady=5)
        self.hora = tb.Spinbox(master=self.entrada, bootstyle='info', from_=0, to=24)
        self.hora.pack(side=tb.LEFT)

        self.b3 = tb.Button(master=self.entrada, image=self.imagen2, compound=tb.LEFT, text='Confirma', bootstyle='info', command=self.confirmar_Evento)
        self.b3.pack(side=tb.LEFT, padx=(6,10))
        
        self._open()
    
    def _get_Data(self)->list:
        data=[]
        for elem in self.eventos:
            data.append([elem.nombre,elem.fecha,elem.hora])
        return data
        
    def _save_Data(self)->None:
        with open(self.filename, mode='a', newline='') as archivo_csv:
            escritor = csv.writer(archivo_csv)
            escritor.writerows(self._get_Data())

if __name__ == "__main__":
    app = Aplicacion()
    app.ventana.mainloop()