import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import random
import customtkinter

'''
nombre:
apellido:
---
Ejercicio: for_09
---
Enunciado:
Al comenzar el juego generamos un número secreto del 1 al 100, se pedira al usuario el ingreso de un numero por prompt y si el número ingresado es el mismo que el número secreto se dará por terminado el juego con un mensaje similar a este: 

En esta oportunidad el juego evaluará tus aptitudes a partir de la cantidad de intentos, por lo cual se informará lo siguiente:
    1° intento: “Usted es un psíquico”.
	2° intento: “Excelente percepción”.
	3° intento: “Esto es suerte”.
	4° hasta 6° intento: “Excelente técnica”.
	7 intentos: “Perdiste, suerte para la próxima”.

de no ser igual se debe informar si 
“Falta…”  para llegar al número secreto  o si 
“Se pasó…”  del número secreto.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        num=random.randrange(start=1, stop=5)
        cont=0
        ganar=False
        input=prompt("Ingresar", "Ingrese un numero aleatorio")
        for x in range(1,10):
            if int(input)>num:
                frio_calor="Te pasaste"
            elif int(input)<num:
                frio_calor="Falta"
            else:
                ganar=True
            cont+=1
            if cont<7 and ganar==False:
                alert('titulo', frio_calor)
                input=prompt("Ingresar", "Ingrese un numero aleatorio")
            elif cont ==7 and ganar==False:
               alert('titulo', "Perdiste, suerte para la próxima")
               break
            else:
                match cont:
                    case 1:
                        alert('titulo', "Usted es un psíquico")
                    case 2:
                        alert('titulo', "Excelente percepción")
                    case 3:
                        alert('titulo', "Esto es suerte")
                    case _:
                        alert('titulo', "Excelente tecnica")
                break     
        pass
                

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()