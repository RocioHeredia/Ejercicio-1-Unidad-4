from tkinter import *
from tkinter import ttk, messagebox


class Aplicacion:
    __ventana = None
    __vestimenta_cant = None
    __vestimenta_preciobase = None
    __vestimenta_precioactual = None
    __alimentos_cant = None
    __alimentos_preciobase = None
    __alimentos_precioactual = None
    __educacion_cant = None
    __educacion_preciobase = None
    __educacion_precioactual = None
    __ipc = None

    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.geometry('450x200')
        self.__ventana.configure(bg='white')
        self.__ventana.title('Calculadora IPC')
        mainframe = ttk.Frame(self.__ventana, padding='0 5 12 0')
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        mainframe['borderwidth'] = 2

        # Colocamos StringVar a cada variable

        self.__vestimenta_cant = StringVar()
        self.__vestimenta_preciobase = StringVar()
        self.__vestimenta_precioactual = StringVar()
        self.__alimentos_cant = StringVar()
        self.__alimentos_preciobase = StringVar()
        self.__alimentos_precioactual = StringVar()
        self.__educacion_cant = StringVar()
        self.__educacion_preciobase = StringVar()
        self.__educacion_precioactual = StringVar()
        self.__ipc = StringVar()

        # Creamos los Label de cada variable
        ttk.Label(mainframe, text='Item').grid(column=1, row=1)
        ttk.Label(mainframe, text='Vestimenta').grid(column=1, row=2)
        ttk.Label(mainframe, text='Alimentos').grid(column=1, row=3)
        ttk.Label(mainframe, text='Educacion').grid(column=1, row=4)
        ttk.Label(mainframe, text='Cantidad').grid(column=2, row=1)
        self.vestimenta_cantEntry = ttk.Entry(mainframe, width=15, textvariable=self.__vestimenta_cant)
        self.vestimenta_cantEntry.grid(column=2, row=2, sticky=W)
        self.alimentos_cantEntry = ttk.Entry(mainframe, width=15, textvariable=self.__alimentos_cant)
        self.alimentos_cantEntry.grid(column=2, row=3, sticky=W)
        self.educacion_cantEntry = ttk.Entry(mainframe, width=15, textvariable=self.__educacion_cant)
        self.educacion_cantEntry.grid(column=2, row=4, sticky=W)
        ttk.Label(mainframe, text='Precio Año Base').grid(column=3, row=1)
        self.vestimenta_preciobaseEntry = ttk.Entry(mainframe, width=15, textvariable=self.__vestimenta_preciobase)
        self.vestimenta_preciobaseEntry.grid(column=3, row=2, sticky=W)
        self.alimentos_baseEntry = ttk.Entry(mainframe, width=15, textvariable=self.__alimentos_preciobase)
        self.alimentos_baseEntry.grid(column=3, row=3, sticky=W)
        self.educacion_baseEntry = ttk.Entry(mainframe, width=15, textvariable=self.__educacion_preciobase)
        self.educacion_baseEntry.grid(column=3, row=4, sticky=W)
        ttk.Label(mainframe, text='Precio Año Actual').grid(column=4, row=1)
        self.vestimenta_actualEntry = ttk.Entry(mainframe, width=15, textvariable=self.__vestimenta_precioactual)
        self.vestimenta_actualEntry.grid(column=4, row=2, sticky=W)
        self.alimentos_actualEntry = ttk.Entry(mainframe, width=15, textvariable=self.__alimentos_precioactual)
        self.alimentos_actualEntry.grid(column=4, row=3, sticky=W)
        self.educacion_actualEntry = ttk.Entry(mainframe, width=15, textvariable=self.__educacion_precioactual)
        self.educacion_actualEntry.grid(column=4, row=4, sticky=W)
        ttk.Button(mainframe, text='Calcular IPC', command=self.calcularIPC).grid(column=2, row=5, sticky=S)
        ttk.Button(mainframe, text='Salir', command=self.__ventana.destroy).grid(column=3, row=5, columnspan=2, sticky=S)
        ttk.Label(mainframe, text='IPC %').grid(column=0, row=6, sticky=S)
        ttk.Label(mainframe, textvariable=self.__ipc).grid(column=0, row=6, columnspan=2, sticky=S)
        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)
        self.vestimenta_cantEntry.focus()
        self.__ventana.mainloop()

    def calcularIPC(self):
        try:
            # Cargamos los datos en variables
            vestimenta_cantidad = int(self.vestimenta_cantEntry.get())
            vestimenta_preciobase = float(self.vestimenta_preciobaseEntry.get())
            vestimenta_precioactual = float(self.vestimenta_actualEntry.get())
            alimentos_cantidad = int(self.alimentos_cantEntry.get())
            alimentos_preciobase = float(self.alimentos_baseEntry.get())
            alimentos_precioactual = float(self.alimentos_actualEntry.get())
            educacion_cantidad = int(self.educacion_cantEntry.get())
            educacion_preciobase = float(self.educacion_baseEntry.get())
            educacion_precioactual = float(self.educacion_actualEntry.get())

            # Calculamos el IPC para cada categoria
            IPC_vestimenta = ((vestimenta_cantidad * vestimenta_preciobase) / (vestimenta_cantidad * vestimenta_precioactual))
            IPC_alimentos = ((alimentos_cantidad * alimentos_preciobase) / (alimentos_cantidad * alimentos_precioactual))
            IPC_educacion = ((educacion_cantidad * educacion_preciobase) / (educacion_cantidad * educacion_precioactual))

            # Quitamos la parte entera para multiplicarla por el 100%
            ipcentera = int(IPC_vestimenta + IPC_alimentos + IPC_educacion)
            ipctotal = ipcentera * 100
            self.__ipc.set(str(ipctotal) + '%')

        except ValueError:
            messagebox.showerror(title='Error de tipo', message='Debe ingresar valores numéricos')

            # Limpiar los valores de las variables y enfocar en el primer campo
            self.__vestimenta_cant.set('')
            self.__vestimenta_preciobase.set('')
            self.__vestimenta_precioactual.set('')
            self.__alimentos_cant.set('')
            self.__alimentos_preciobase.set('')
            self.__alimentos_precioactual.set('')
            self.__educacion_cant.set('')
            self.__educacion_preciobase.set('')
            self.__educacion_precioactual.set('')
            self.__ipc.set('')


def testApp():
    mi_app = Aplicacion()


if __name__ == '__main__':
    testApp()