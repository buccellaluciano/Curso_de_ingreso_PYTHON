import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
Ejercicio: for_08
---
Enunciado:
Al presionar el botón 'Mostrar' pedir un número. Mostrar cada número primo entre 1 y el número ingresado, e informar la cantidad de números primos encontrados.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        num=prompt('titulo',"ingresar")
        cont_prim=-1
        cont=1
        cuenta=0
        for j in range(1, int(num)+1, 1):
            if j<10 and cont==8:
                    cont_prim+=1
                    alert('titulo', str(j-1)+" es un numero primo")
                    x=2
            elif j>10 and cont==9:
                    cont_prim+=1
                    alert('titulo', str(j-1)+" es un numero primo")
                    x=2
            
            cont=1
            for x in range(2, 10):
                print('a', "JOTA: "+str(j))
                print('a', "EQUIS: "+str(x))
                if j%x!=0:
                    cont+=1
                    cuenta=j%x
                    print("CUENTA: "+str(cuenta))            
        pass        
        alert('titulo',"hay "+ str(cont_prim) +" numeros primos")
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()