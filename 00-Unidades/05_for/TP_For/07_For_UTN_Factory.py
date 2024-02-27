import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
TP: For_UTN_Factory
---
Enunciado:
UTN Software Factory está en la búsqueda de programadores para incorporar a su equipo de 
trabajo. En las próximas semanas se realizará un exhaustivo proceso de selección. Para ello se 
ingresarán los siguientes datos de los 10 postulantes para luego establecer distintas métricas 
necesarias para tomar decisiones a la hora de la selección:

Nombre
Edad (mayor de edad)
Género (F-M-NB)
Tecnología (PYTHON - JS - ASP.NET)
Puesto (Jr - Ssr - Sr)

Informar por pantalla:
a. Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS 
cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr.
b. Nombre del postulante Jr con menor edad.
c. Promedio de edades por género.
d. Tecnologia con mas postulantes (solo hay una).
e. Porcentaje de postulantes de cada genero.

Todos los datos se ingresan por prompt y los resultados se muestran por consola (print)

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        ajp=0 
        min_jr=0
        edad_f=0
        edad_m=0
        edad_nb=0
        pos_py=0
        pos_js=0
        pos_asp=0
        n_max=0
        n_post=""
        f=0
        m=0
        nb=0
        for x in range(1,3):
            nombre=prompt('nombre', "Ingrese su nombre")
            edad=prompt('edad', "Ingrese su edad")
            genero=prompt('genero',"Ingrese su genero (F/M/NB)")
            genero=genero.upper()
            print (genero)
            if genero!="F" and genero!="M" and genero!="NB":
                alert('error', "No es un genero valido")
                break
            tech=prompt('tecnologia',"Ingrese su tech (PYTHON/JS/ASP.NET)")
            tech=tech.upper()
            if tech!="PYTHON" and tech!="JS" and tech!="ASP.NET":
                alert('error', "No es una tech valida")
                break
            tech=tech.upper()
            puesto=prompt('Puesto',"Ingrese su puesto (JR/SSR/SR)")
            puesto=puesto.upper()
            if puesto!="JR" and puesto!="SSR" and puesto!="SR":
                alert('error', "No es puesto valido")
                break
            match genero:
                case "NB":    
                    if tech=="ASP.NET" or tech=="JS":
                        if int(edad)>=25 and int(edad)<=40:
                            if puesto=="SSR":
                                ajp+=1
            match puesto:
                case "JR":
                    min_jr=int(edad)
                    if int(edad)<min_jr:
                        min_jr=edad
                        jr_name=nombre
            print(str(min_jr))
            match genero:
                case "F":
                    edad_f+=int(edad)/10
                    f+=1*100/10  
                case "M":
                    edad_m+=int(edad)/10
                    m+=1*100/10  
                case "NB":
                    edad_nb+=int(edad)/10 
                    nb+=1*100/10    
            if tech=="PYTHON":
                pos_py+=1
                if pos_py>n_max:
                    n_max=pos_py
                    n_post="Python"
            elif tech=="JS":
                pos_js+=1
                if pos_js>n_max:
                    n_max=pos_js
                    n_post="Js"
            elif tech=="ASP.NET":
                pos_asp+=1
                if tech>n_max:
                    n_max=pos_asp
                    n_post="ASP.NET"
        
        print  (f'"Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr: {str(ajp)}"\n'
                f'"Nombre del postulante Jr con menor edad: {str(min_jr)}"\n'
                f'"Promedio de edades por género: Femenino: {str(edad_f)} Masculino: {str(edad_m)} No binario: {str(edad_nb)}"\n'
                f'"Tecnologia con mas postulantes: {n_post}"\n'
                f'"Porcentaje de postulantes de cada genero: Femenino: {str(f)} Masculino: {str(m)} No Binario: {str(nb)}')     
        pass


        

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
