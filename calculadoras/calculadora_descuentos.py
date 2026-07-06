import tkinter as tk
from tkinter import messagebox

#Calculadora de descuentos
class CalculadoraDescuentos:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Descuentos")
        self.root.geometry("500x400")
        self.root.configure(bg="#34495E")
        self.root.resizable(False, False)

        try:
            icono = tk.PhotoImage(file="../img/icono.png")
            self.root.iconphoto(True, icono)
        except:
            pass

        tk.Label(root, text="Calculadora de Descuentos", font=("Arial", 12, "italic"),
                 bg="#34495E", fg="#ECF0F1").pack(pady=20)

        tk.Label(root, text="Valor del Producto:", font=("Arial", 11),
                 bg="#34495E", fg="white").pack(pady=5)
        self.valor_producto = tk.Entry(root, font=("Arial", 11), width=20)
        self.valor_producto.pack(pady=5)

        tk.Label(root, text="Porcentaje de Descuento (%):", font=("Arial", 11),
                 bg="#34495E", fg="white").pack(pady=5)
        self.porcentaje_descuento = tk.Entry(root, font=("Arial", 11), width=20)
        self.porcentaje_descuento.pack(pady=5)

        tk.Button(root, text="Calcular Descuento", font=("Arial", 11, "bold"),
                  bg="#2980B9", fg="white", width=25, command=self.calcular_descuento).pack(pady=10)

        self.resultado = tk.Label(root, text="Precio Final: ---", font=("Arial", 13, "bold"),
                                  bg="#1ABC9C", fg="white", width=30, height=2, relief="ridge")
        self.resultado.pack(pady=15)

    def calcular_descuento(self):
        try:
            valor = float(self.valor_producto.get())
            porcentaje = float(self.porcentaje_descuento.get())

            if valor < 0:
                messagebox.showerror("Error", "El valor del producto no puede ser negativo.")
                return
            if porcentaje < 0:
                messagebox.showerror("Error", "El porcentaje no puede ser negativo.")
                return
            if porcentaje > 100:
                messagebox.showerror("Error", "El porcentaje no puede ser mayor a 100.")
                return

            descuento = valor * (porcentaje / 100)
            precio_final = valor - descuento
            self.resultado.config(text=f"Precio Final: ${precio_final:.2f}")
        except ValueError:
            if self.valor_producto.get() == "" or self.porcentaje_descuento.get() == "":
                messagebox.showerror("Error", "Los campos no pueden estar vacíos.")
            else:
                messagebox.showerror("Error", "Ingrese solo números válidos.")
