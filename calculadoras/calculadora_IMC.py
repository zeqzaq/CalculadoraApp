import tkinter as tk
from tkinter import messagebox

#Calculadora de peso
class CalculadoraIMC:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Peso")
        self.root.geometry("500x400")
        self.root.configure(bg="#34495E")
        self.root.resizable(False, False)

        try:
            icono = tk.PhotoImage(file="../img/icono.png")
            self.root.iconphoto(True, icono)
        except:
            pass

        tk.Label(root, text="Calculadora de IMC", font=("Arial", 12, "italic"),bg="#34495E", fg="#ECF0F1").pack(pady=20)
        tk.Label(root, text="Peso en kg:", font=("Arial", 11),bg="#34495E", fg="white").pack(pady=5)
        #Peso en kg
        self.peso_kg = tk.Entry(root, font=("Arial", 11), width=20)
        self.peso_kg.pack(pady=5)
        #Altura
        tk.Label(root, text="Altura en metros:", font=("Arial", 11),bg="#34495E", fg="white").pack(pady=5)
        self.altura_m = tk.Entry(root, font=("Arial", 11), width=20)
        self.altura_m.pack(pady=5)

        tk.Button(root, text="Calcular IMC", font=("Arial", 11, "bold"),bg="#2980B9", fg="white", width=25, command=self.calcular_imc).pack(pady=10)

        self.resultado = tk.Label(root, text="IMC: ---", font=("Arial", 13, "bold"),bg="#1ABC9C", fg="white", width=30, height=2, relief="ridge")
        self.resultado.pack(pady=15)

    def calcular_imc(self):
        try:
            peso = float(self.peso_kg.get())
            altura = float(self.altura_m.get())

            if altura <= 0:
                messagebox.showerror("Error", "La altura debe ser mayor que cero.")
                return
            elif peso <= 0:
                messagebox.showerror("Error", "El peso debe ser mayor que cero.")
                return
            
            #Calcular IMC
            imc = peso / (altura ** 2)
            self.resultado.config(text=f"IMC: {imc:.2f}")
        except ValueError:  
            if self.peso_kg.get() == "":
                messagebox.showerror("Error", "El campo no puede estar vacío.")