import tkinter as tk
from tkinter import messagebox

#Conversor de monedas
class CalculadoraMonedas:
    def __init__(self, root):
        self.root = root
        self.root.title("Conversor de Monedas")
        self.root.geometry("500x400")
        self.root.configure(bg="#34495E")
        self.root.resizable(False, False)

        try:
            icono = tk.PhotoImage(file="../img/icono.png")
            self.root.iconphoto(True, icono)
        except:
            pass

        tk.Label(root, text="Conversor de Monedas", font=("Arial", 12, "italic"),
                 bg="#34495E", fg="#ECF0F1").pack(pady=20)

        tk.Label(root, text="Pesos Colombianos (COP):", font=("Arial", 11),
                 bg="#34495E", fg="white").pack(pady=5)
        self.pesos = tk.Entry(root, font=("Arial", 11), width=20)
        self.pesos.pack(pady=5)

        tk.Button(root, text="Convertir a Dólares", font=("Arial", 11, "bold"),
                  bg="#2980B9", fg="white", width=25, command=self.a_dolares).pack(pady=10)
        tk.Button(root, text="Convertir a Euros", font=("Arial", 11, "bold"),
                  bg="#27AE60", fg="white", width=25, command=self.a_euros).pack(pady=10)

        self.resultado = tk.Label(root, text="Resultado: ---", font=("Arial", 13, "bold"),
                                  bg="#1ABC9C", fg="white", width=30, height=2, relief="ridge")
        self.resultado.pack(pady=15)

    def a_dolares(self):
        try:
            cop = float(self.pesos.get())
            if cop < 0:
                messagebox.showerror("Error", "El valor no puede ser negativo.")
                return
            dolar = cop / 4100
            self.resultado.config(text=f"${cop:.0f} COP = ${dolar:.2f} USD")
        except ValueError:
            if self.pesos.get() == "":
                messagebox.showerror("Error", "El campo no puede estar vacío.")
            else:
                messagebox.showerror("Error", "Ingrese un valor válido.")

    def a_euros(self):
        try:
            cop = float(self.pesos.get())
            if cop < 0:
                messagebox.showerror("Error", "El valor no puede ser negativo.")
                return
            euro = cop / 4500
            self.resultado.config(text=f"${cop:.0f} COP = €{euro:.2f} EUR")
        except ValueError:
            if self.pesos.get() == "":
                messagebox.showerror("Error", "El campo no puede estar vacío.")
            else:
                messagebox.showerror("Error", "Ingrese un valor válido.")
