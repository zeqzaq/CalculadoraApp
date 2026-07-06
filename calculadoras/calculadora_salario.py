import tkinter as tk
from tkinter import messagebox

#Calculadora de salario
class CalculadoraSalario:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Salario")
        self.root.geometry("500x400")
        self.root.configure(bg="#34495E")
        self.root.resizable(False, False)

        try:
            icono = tk.PhotoImage(file="../img/icono.png")
            self.root.iconphoto(True, icono)
        except:
            pass

        tk.Label(root, text="Calculadora de Salario", font=("Arial", 12, "italic"),bg="#34495E", fg="#ECF0F1").pack(pady=20)
        #Horas maximas semanales
        tk.Label(root, text="Horas Max Semanales: 40", font=("Arial", 11),bg="#34495E", fg="white").pack(pady=5)
        self.horas_semanales = tk.Entry(root, font=("Arial", 11), width=20)
        self.horas_semanales.pack(pady=5)
        #Entrada de salario base
        tk.Label(root, text="Salario Base:", font=("Arial", 11),bg="#34495E", fg="white").pack(pady=5)
        self.salario_base = tk.Entry(root, font=("Arial", 11), width=20)
        self.salario_base.pack(pady=5)
        #Entrada horas extras
        tk.Label(root, text="Horas Extras:", font=("Arial", 11),bg="#34495E", fg="white").pack(pady=5)
        self.horas_extras = tk.Entry(root, font=("Arial", 11), width=20)
        self.horas_extras.pack(pady=5)

        tk.Button(root, text="Calcular Salario Neto", font=("Arial", 11, "bold"),bg="#2980B9", fg="white", width=25, command=self.calcular_salario_neto).pack(pady=10)

        self.resultado = tk.Label(root, text="Salario Neto: ---", font=("Arial", 13, "bold"),bg="#1ABC9C", fg="white", width=30, height=2, relief="ridge")
        self.resultado.pack(pady=15)

    def calcular_salario_neto(self):
        try:
            salario_base = float(self.salario_base.get())
            horas_extras = float(self.horas_extras.get())
            horas_semanales = float(self.horas_semanales.get())
            if salario_base < 0:
                messagebox.showerror("Error", "El salario base no puede ser negativo.")
                return

            salario_neto = 1
            self.resultado.config(text=f"Salario Neto: {salario_neto:.2f}")
        except ValueError:
            if self.salario_base.get() == "":
                messagebox.showerror("Error", "El campo no puede estar vacío.")
            else:
                messagebox.showerror("Error", "Ingrese un salario válido.")