import tkinter as tk
from tkinter import messagebox

#Calculadora de temperatura - grados Celsius a Fahrenheit y viceversa
class CalculadoraTemp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Temperatura")
        self.root.geometry("500x400")
        self.root.configure(bg="#34495E")
        self.root.resizable(False, False)

        try:
            icono = tk.PhotoImage(file="../img/icono.png")
            self.root.iconphoto(True, icono)
        except:
            pass

        tk.Label(root, text="Calculadora de Temperatura", font=("Arial", 12, "italic"),bg="#34495E", fg="#ECF0F1").pack(pady=20)
        tk.Label(root, text="Temperatura:", font=("Arial", 11),bg="#34495E", fg="white").pack(pady=5)
        #Entrada de temperatura
        self.temperatura = tk.Entry(root, font=("Arial", 11), width=20)
        self.temperatura.pack(pady=5)

        tk.Button(root, text="Celsius a Fahrenheit", font=("Arial", 11, "bold"),bg="#2980B9", fg="white", width=25, command=self.celsius_a_fahrenheit).pack(pady=10)
        tk.Button(root, text="Fahrenheit a Celsius", font=("Arial", 11, "bold"),bg="#27AE60", fg="white", width=25, command=self.fahrenheit_a_celsius).pack(pady=10)

        self.resultado = tk.Label(root, text="Resultado: ---", font=("Arial", 13, "bold"),bg="#1ABC9C", fg="white", width=30, height=2, relief="ridge")
        self.resultado.pack(pady=15)

    def celsius_a_fahrenheit(self):
        try:
            celsius = float(self.temperatura.get())
            fahrenheit = (celsius * 9/5) + 32 #Formula para convertir Celsius a Fahrenheit
            self.resultado.config(text=f"Resultado: {fahrenheit:.2f} °F")
        except ValueError:
            if self.temperatura.get() == "":
                messagebox.showerror("Error", "El campo no puede estar vacío.")
            else:
                messagebox.showerror("Error", "Ingrese una temperatura válida.")

    def fahrenheit_a_celsius(self):
        try:
            fahrenheit = float(self.temperatura.get())
            celsius = (fahrenheit - 32) * 5/9 #Formula para convertir Fahrenheit a Celsius
            self.resultado.config(text=f"Resultado: {celsius:.2f} °C")
        except ValueError:
            if self.temperatura.get() == "":
                messagebox.showerror("Error", "El campo no puede estar vacío.")
            else:
                messagebox.showerror("Error", "Ingrese una temperatura válida.")