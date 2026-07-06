import tkinter as tk
from tkinter import messagebox

#Calculadora de combustible
class CalculadoraCombustible:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Combustible")
        self.root.geometry("500x400")
        self.root.configure(bg="#34495E")
        self.root.resizable(False, False)

        try:
            icono = tk.PhotoImage(file="../img/icono.png")
            self.root.iconphoto(True, icono)
        except:
            pass

        tk.Label(root, text="Calculadora de Combustible", font=("Arial", 12, "italic"),
                 bg="#34495E", fg="#ECF0F1").pack(pady=20)

        tk.Label(root, text="Kilómetros Recorridos:", font=("Arial", 11),
                 bg="#34495E", fg="white").pack(pady=5)
        self.km = tk.Entry(root, font=("Arial", 11), width=20)
        self.km.pack(pady=5)

        tk.Label(root, text="Combustible Consumido (L):", font=("Arial", 11),
                 bg="#34495E", fg="white").pack(pady=5)
        self.litros = tk.Entry(root, font=("Arial", 11), width=20)
        self.litros.pack(pady=5)

        tk.Button(root, text="Calcular Rendimiento", font=("Arial", 11, "bold"),
                  bg="#2980B9", fg="white", width=25, command=self.calcular_rendimiento).pack(pady=10)

        self.resultado = tk.Label(root, text="Rendimiento: ---", font=("Arial", 13, "bold"),
                                  bg="#1ABC9C", fg="white", width=30, height=2, relief="ridge")
        self.resultado.pack(pady=15)

    def calcular_rendimiento(self):
        try:
            kilometros = float(self.km.get())
            litros = float(self.litros.get())

            if kilometros < 0:
                messagebox.showerror("Error", "Los kilómetros no pueden ser negativos.")
                return
            if litros <= 0:
                messagebox.showerror("Error", "El combustible consumido debe ser mayor que cero.")
                return

            rendimiento = kilometros / litros
            self.resultado.config(text=f"Rendimiento: {rendimiento:.2f} km/L")
        except ValueError:
            if self.km.get() == "" or self.litros.get() == "":
                messagebox.showerror("Error", "Los campos no pueden estar vacíos.")
            else:
                messagebox.showerror("Error", "Ingrese solo números válidos.")
