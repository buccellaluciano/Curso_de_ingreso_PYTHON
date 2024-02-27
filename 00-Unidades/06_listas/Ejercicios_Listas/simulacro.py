import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
Ejercicio: listas_01
---
Un gimnasio quiere medir el progreso de sus clientes, para ello se debe ingresar:

Nombre
Edad (debe ser mayor a 12)
Altura (no debe ser negativa)
Días que asiste a la semana (1, 3, 5)
Kilos que levanta en peso muerto (no debe ser cero, ni negativo)

 

No sabemos cuántos clientes serán consultados.
Se debe informar al usuario:
El promedio de kilos que levantan las personas que asisten solo 3 días a la semana.
El porcentaje de clientes que asiste solo 1 día a la semana.
Nombre y edad del cliente con más altura.
Determinar si los clientes eligen más ir 1, 3 o 5 días
Nombre y cantidad de kilos levantados en peso muerto, de la persona más joven que solo asista 5 días a la semana.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

        self.lista_datos = [2,3,5,7,11,13]


    def btn_mostrar_on_click(self):
        num=0
        kilos_prom=0
        cont_1=0
        cont_2=0
        altura_maxima=0
        jirafa_nombre=""
        jirafa_edad=""
        asist_1=0
        asist_3=0
        asist_5=0
        joven_5=0
        nom_5=""
        peso_5=0
        mayor_asistido=""
        asist_cont=0
        num=prompt('titulo', "Ingrese cuanta gente quiere inscribir")
        for x in range (0, int(num)):
            nombre=prompt('titulo', "Ingrese su nombre")
            nombre=nombre.upper()
            edad=prompt('titulo', "Ingrese su edad (Debe ser mayor a 12)")
            edad=int(edad)
            joven_5=edad
            if int(edad)<=12:
                alert('titulo', "Error, la edad debe ser mayor a 12")
                break
            joven_5=edad
            altura=prompt('titulo', "Ingrese su altura (cm)")
            altura=int(altura)
            if int(altura)<0:
                alert('titulo', "Error, la altura no puede er negativa")
                break
            asistencia=prompt('titulo', "Ingrese cuantos dias asistira (1/3/5)")
            asistencia=int(asistencia)
            asist_cont=x
            if asistencia!=1 and asistencia!=3 and asistencia!=5:
                alert('titulo', "Error, solo puedes elegir 1/3/5")
                break
            kilos=prompt('titulo', "Ingrese peso en KG (Debe ser mayor a 0)")
            kilos=int(kilos)
            if kilos<=0:
                alert('titulo', "Error, el peso debe ser mayor a 0")
                break
            match asistencia:
                case 5:
                    asist_5+=1
                    if asist_cont<asist_5:
                         asist_cont=asist_5
                         mayor_asistido="5 dias a la semana"
                    if edad<=joven_5:
                        nom_5=nombre
                        peso_5=kilos
                        print(str(peso_5))
                case 3:
                    asist_3+=1
                    if asist_cont<asist_3:
                         asist_cont=asist_3
                         mayor_asistido="3 dias a la semana"
                    kilos_prom+=kilos
                    cont_1+=1
                case 1:
                     asist_1+=1
                     if asist_cont<asist_1:
                         asist_cont=asist_1
                         mayor_asistido="1 dia a la semana"
                     cont_2+=1
                     
                     
            
            if int(altura)>altura_maxima:
                altura_maxima=altura
                jirafa_nombre=nombre
                jirafa_edad=edad
        if x>0:
            kilos_prom==kilos_prom/asist_3
            cont_2==(cont_2/4)*100
        
        print  (f'"El promedio de kilos que levantan las personas que asisten solo 3 días a la semana.: {str(kilos_prom)}"\n'
                f'"El porcentaje de clientes que asiste solo 1 día a la semana.: {str(cont_2)}"\n'
                f'"Nombre y edad del cliente con más altura: Nombre: {str(jirafa_nombre)} Edad: {str(jirafa_edad)}"\n'
                f'"Cantidad de asistencias mas repetida: {mayor_asistido}"\n'
                f'"Nombre y cantidad de kilos levantados en peso muerto, de la persona más joven que solo asista 5 días a la semana: Nombre: {str(nom_5)} Kilos: {str(peso_5)}')     
        pass    

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()