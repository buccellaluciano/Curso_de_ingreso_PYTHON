import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
nombre:
apellido:
---
Ejercicio: Match_03
---
Enuciado:
Al presionar el botón ‘Informar’ mostrar mediante alert los siguientes 
mensajes en función del mes seleccionado:
    Si es febrero: ‘Este mes no tiene más de 29 días’
    Si no es febrero: ‘Este mes tiene 30 días o mas’

'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.label_meses = customtkinter.CTkLabel(master=self, text="Meses")
        self.label_meses.grid(row=0, column=0, padx=20, pady=10)
        meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
        self.combobox_mes = customtkinter.CTkComboBox(master=self, values=meses)
        self.combobox_mes.grid(row=1, column=0, padx=20, pady=(10, 10))
        
        self.btn_informar = customtkinter.CTkButton(master=self, text="Informar", command=self.btn_informar_on_click)
        self.btn_informar.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_informar_on_click(self):
        mes=self.combobox_mes.get()
        match mes:
            case 'Enero':
                alert('titulo', "Este mes tiene 30 días o mas")
            case 'Febero':
                alert('titulo', "Este mes no tiene más de 29 días")
            case 'Marzo':
                alert('titulo', "Este mes tiene 30 días o mas")
            case 'Abril':
                alert('titulo', "Este mes tiene 30 días o mas")
            case 'Mayo':
                alert('titulo', "Este mes tiene 30 días o mas") 
            case 'Junio':
                alert('titulo', "Este mes tiene 30 días o mas")
            case 'Julio':
                alert('titulo', "Este mes tiene 30 días o mas")
            case 'Agosto':
                alert('titulo', "Este mes tiene 30 días o mas")
            case 'Septiembre':
                alert('titulo',"Este mes tiene 30 días o mas")
            case 'Octubre':
                alert('titulo',"Este mes tiene 30 días o mas")
            case 'Noviembre':
                alert('titulo',"Este mes tiene 30 días o mas")
            case 'Diciembre':
                alert('titulo',"Este mes tiene 30 días o mas")
        pass
    
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()