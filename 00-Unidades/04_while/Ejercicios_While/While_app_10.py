import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
Ejercicio: while_10
---
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    A. La suma acumulada de los negativos
    B. La suma acumulada de los positivos
    C. Cantidad de números positivos ingresados
    D. Cantidad de números negativos ingresados
    E. Cantidad de ceros
    F. Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        
        prompt ('titulo', "hola")
        positivos_suma=0
        negativos_suma=0
        positivos=0
        negativos=0
        ceros=0
        num=prompt('titulo', "ingrese un numero")
        while num!=None:
            
            if int(num)<0:
                negativos_suma+=int(num)
                negativos+=1
            elif int(num)>0:
                positivos_suma+=int(num)
                positivos+=1
            elif int(num)==0:
                ceros+=1
            num=prompt('titulo', "ingrese un numero",)
        
        if negativos>positivos:
            negativos-=positivos
            alert('titulo', "Hay más números negativos, siendo la diferencia de "+str(negativos)+" más")
        elif positivos>negativos:
            positivos-=negativos
            alert('titulo', "Hay más números positivos, siendo la diferencia de "+str(positivos)+" más")
        else:
            alert('titulo', "La cantidad de positivos y negativos en la misma.")
        
        alert('titulo', "La suma de los números positivos es de: "+str(positivos_suma)+"Y la cantidad de positivos es de: "+str(positivos))
        alert('titulo', "La suma de los números negativos es de: "+str(negativos_suma)+"Y la cantidad de negativos es de: "+str(negativos))
        alert('titulo', "La cantidad de ceros es de: "+str(ceros))
        
        pass

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
