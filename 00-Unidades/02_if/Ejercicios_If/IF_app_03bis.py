import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
Buccella
Ejercicio: if_03bis
Luciano
Enunciado:
A partir del ingreso de la altura de un basquetbolista determinar si es pivot o no. Para serlo el mismo deberá medir mas de 1.80 metros
'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.label1 = customtkinter.CTkLabel(master=self, text="Altura (en centímetros)")
        self.label1.grid(row=0, column=0, padx=20, pady=10)

        self.txt_altura = customtkinter.CTkEntry(master=self)
        self.txt_altura.grid(row=0, column=1)

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

    def btn_mostrar_on_click(self):
        altura = self.txt_altura.get()
        if int(altura)==216:
            alert('titulo', "Es Shaquille O'Neal")
        elif int(altura)>=180:
            alert('titulo', "Es pivot")
        else:
            alert('titulo', "No es pivot")
        
        pass


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()