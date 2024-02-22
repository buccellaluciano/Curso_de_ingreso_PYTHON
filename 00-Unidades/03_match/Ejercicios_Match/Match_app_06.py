import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
nombre:
apellido:
---
Ejercicio: Match_06
---
Enunciado:
Obtener la hora ingresada en el cuadro de texto txt_hora. 
Al presionar el botón ‘Informar’ mostrar mediante alert alguno de los 
siguientes mensajes según la hora ingresada:
    Si está entre las 7 y las 11: ‘Es de mañana’
    Si está entre las 12 y las 19: ‘Es de tarde’
    Si está entre las 20 y las 24 o entre las 0 y las 6: ‘Es de noche’
    Si no está entre 0 y las 24: ‘La hora no existe’
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.label_hora = customtkinter.CTkLabel(master=self, text="Hora")
        self.label_hora.grid(row=0, column=0, padx=20, pady=10)
        self.txt_hora = customtkinter.CTkEntry(master=self)
        self.txt_hora.grid(row=0, column=1)
        
        self.btn_informar = customtkinter.CTkButton(master=self, text="Informar", command=self.btn_informar_on_click)
        self.btn_informar.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_informar_on_click(self):
        hora=self.txt_hora.get()
        match hora:
            case '00':
                alert('titulo', "Es de noche")
            case '1':
                alert('titulo', "Es de noche")
            case '2':
                alert('titulo', "Es de noche")
            case '3':
                alert('titulo', "Es de noche")
            case '4':
                alert('titulo', "Es de noche")
            case '5':
                alert('titulo', "Es de noche")
            case '6':
                alert('titulo', "Es de noche")
            case '7':
                alert('titulo', "Es de mañana")
            case '8':
                alert('titulo', "Es de mañana")
            case '9':
                alert('titulo', "Es de mañana")
            case '10':
                alert('titulo', "Es de mañana")
            case '11':
                alert('titulo', "Es de mañana")
            case '12':
                alert('titulo', "Es de tarde")
            case '13':
                alert('titulo', "Es de tarde")      
            case '14':
                alert('titulo', "Es de tarde")      
            case '15':
                alert('titulo', "Es de tarde")      
            case '16':
                alert('titulo', "Es de tarde")      
            case '17':
                alert('titulo', "Es de tarde")      
            case '18':
                alert('titulo', "Es de tarde")      
            case '19':
                alert('titulo', "Es de tarde")      
            case '20':
                alert('titulo', "Es de noche")      
            case '21':
                alert('titulo', "Es de noche")      
            case '22':
                alert('titulo', "Es de noche")      
            case '23':
                alert('titulo', "Es de noche")         
            case '24':
                alert('titulo', "Es de noche")   
            case other:
                alert('tiutlo', "La hora no existe") 
        pass
    
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()