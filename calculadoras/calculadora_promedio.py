import tkinter as tk
from tkinter import messagebox

#Calculadora de promedio
class CalculadoraPromedio:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Promedio")
        self.root.geometry("500x400")
        self.root.configure(bg="#34495E")
        self.root.resizable(False, False)

        try:
            icono = tk.PhotoImage(file="../img/icono.png")
            self.root.iconphoto(True, icono)
        except:
            pass

        tk.Label(root, text="Calculadora de Promedio", font=("Arial", 12, "italic"),
                 bg="#34495E", fg="#ECF0F1").pack(pady=20)

        tk.Label(root, text="Nota 1:", font=("Arial", 11), bg="#34495E", fg="white").pack(pady=5)
        self.nota1 = tk.Entry(root, font=("Arial", 11), width=20)
        self.nota1.pack(pady=5)

        tk.Label(root, text="Nota 2:", font=("Arial", 11), bg="#34495E", fg="white").pack(pady=5)
        self.nota2 = tk.Entry(root, font=("Arial", 11), width=20)
        self.nota2.pack(pady=5)

        tk.Label(root, text="Nota 3:", font=("Arial", 11), bg="#34495E", fg="white").pack(pady=5)
        self.nota3 = tk.Entry(root, font=("Arial", 11), width=20)
        self.nota3.pack(pady=5)

        tk.Button(root, text="Calcular Promedio", font=("Arial", 11, "bold"),
                  bg="#2980B9", fg="white", width=25, command=self.calcular_promedio).pack(pady=10)

        self.resultado = tk.Label(root, text="Promedio: ---", font=("Arial", 13, "bold"),
                                  bg="#1ABC9C", fg="white", width=30, height=2, relief="ridge")
        self.resultado.pack(pady=15)

    def calcular_promedio(self):
        try:
            n1 = float(self.nota1.get())
            n2 = float(self.nota2.get())
            n3 = float(self.nota3.get())

            if n1 < 0 or n2 < 0 or n3 < 0:
                messagebox.showerror("Error", "Las notas no pueden ser negativas.")
                return

            promedio = (n1 + n2 + n3) / 3
            self.resultado.config(text=f"Promedio: {promedio:.2f}")
        except ValueError:
            if self.nota1.get() == "" or self.nota2.get() == "" or self.nota3.get() == "":
                messagebox.showerror("Error", "Los campos no pueden estar vacíos.")
            else:
                messagebox.showerror("Error", "Ingrese solo números válidos.")
