import tkinter as tk
from tkinter import messagebox
#Calculadora de edad
class CalculadoraEdad:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Edad")
        self.root.geometry("500x400")
        self.root.configure(bg="#34495E")
        self.root.resizable(False, False)

        try:
            icono = tk.PhotoImage(file="../img/icono.png")
            self.root.iconphoto(True, icono)
        except:
            pass

        tk.Label(root, text="Calculadora de Edad", font=("Arial", 12, "italic"),
                 bg="#34495E", fg="#ECF0F1").pack(pady=20)

        tk.Label(root, text="Año de Nacimiento:", font=("Arial", 11),bg="#34495E", fg="white").pack(pady=5)
        #Año de nacimiento
        self.año_nacimiento = tk.Entry(root, font=("Arial", 11), width=20)
        self.año_nacimiento.pack(pady=5)
        #Mes de nacimiento
        tk.Label(root, text="Mes de Nacimiento:", font=("Arial", 11),bg="#34495E", fg="white").pack(pady=5)
        self.mes_nacimiento = tk.Entry(root, font=("Arial", 11), width=20)
        self.mes_nacimiento.pack(pady=5)
        #Día de nacimiento
        tk.Label(root, text="Día de Nacimiento:", font=("Arial", 11),bg="#34495E", fg="white").pack(pady=5)
        self.dia_nacimiento = tk.Entry(root, font=("Arial", 11), width=20)
        self.dia_nacimiento.pack(pady=5)

        tk.Button(root, text="Calcular Edad", font=("Arial", 11, "bold"),bg="#2980B9", fg="white", width=15, command=self.calcular_edad).pack(pady=10)

        self.resultado = tk.Label(root, text="Edad: ---", font=("Arial", 13, "bold"), bg="#1ABC9C", fg="white", width=30, height=2, relief="ridge")
        self.resultado.pack(pady=15)

    def calcular_edad(self):
        try:
            año_hoy = 2026#Año actual
            dia_hoy = 22#Dia actual
            mes_hoy = 6#Mes actual

            año = int(self.año_nacimiento.get())
            mes = int(self.mes_nacimiento.get())
            dia = int(self.dia_nacimiento.get())
            #Calcular edad
            edad = año_hoy - año
            if (mes > mes_hoy) or (mes == mes_hoy and dia > dia_hoy):
                edad -= 1
            elif edad < 0:
                messagebox.showerror("Error", "El año de nacimiento no puede ser en el futuro.")
                return
            self.resultado.config(text=f"Edad: {edad} años")
        except ValueError:
            if self.año_nacimiento.get() == "":
                messagebox.showerror("Error", "El campo no puede estar vacío.")
            else:
                messagebox.showerror("Error", "Ingrese un año válido.")
