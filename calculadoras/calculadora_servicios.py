import tkinter as tk
from tkinter import messagebox

#Calculadora de servicios publicos
class CalculadoraServicios:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Servicios Publicos")
        self.root.geometry("500x400")
        self.root.configure(bg="#34495E")
        self.root.resizable(False, False)

        try:
            icono = tk.PhotoImage(file="../img/icono.png")
            self.root.iconphoto(True, icono)
        except:
            pass

        tk.Label(root, text="Calculadora de Servicios Publicos", font=("Arial", 12, "italic"),
                 bg="#34495E", fg="#ECF0F1").pack(pady=20)

        tk.Label(root, text="Consumo de Energia (kWh):", font=("Arial", 11),
                 bg="#34495E", fg="white").pack(pady=5)
        self.consumo = tk.Entry(root, font=("Arial", 11), width=20)
        self.consumo.pack(pady=5)

        tk.Label(root, text="Tarifa por kWh ($):", font=("Arial", 11),
                 bg="#34495E", fg="white").pack(pady=5)
        self.tarifa = tk.Entry(root, font=("Arial", 11), width=20)
        self.tarifa.pack(pady=5)

        tk.Button(root, text="Calcular Factura", font=("Arial", 11, "bold"),
                  bg="#2980B9", fg="white", width=25, command=self.calcular_factura).pack(pady=10)

        self.resultado = tk.Label(root, text="Total a Pagar: ---", font=("Arial", 13, "bold"),
                                  bg="#1ABC9C", fg="white", width=30, height=2, relief="ridge")
        self.resultado.pack(pady=15)

    def calcular_factura(self):
        try:
            consumo_kwh = float(self.consumo.get())
            tarifa_kwh = float(self.tarifa.get())

            if consumo_kwh < 0:
                messagebox.showerror("Error", "El consumo no puede ser negativo.")
                return
            if tarifa_kwh < 0:
                messagebox.showerror("Error", "La tarifa no puede ser negativa.")
                return

            total = consumo_kwh * tarifa_kwh
            self.resultado.config(text=f"Total a Pagar: ${total:.2f}")
        except ValueError:
            if self.consumo.get() == "" or self.tarifa.get() == "":
                messagebox.showerror("Error", "Los campos no pueden estar vacios.")
            else:
                messagebox.showerror("Error", "Ingrese solo numeros validos.")
