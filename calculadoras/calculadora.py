import tkinter as tk
from tkinter import messagebox

#Calculadora basica
class CalculadoraBasica:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Tkinter")
        self.root.geometry("500x400")
        self.root.configure(bg="#2E4053")
        self.root.resizable(False, False)

        try:
            icono = tk.PhotoImage(file="../img/icono.png")
            self.root.iconphoto(True, icono)
        except:
            pass

        self.estudiante = tk.Label(
            root, text="Calculadora Basica", font=("Arial", 10, "italic"),
            bg="#2E4053", fg="#F0B27A"
        )
        self.estudiante.pack(pady=(10, 0))

        marco = tk.Frame(root, bg="#2E4053")
        marco.pack(pady=20)

        tk.Label(marco, text="Número 1:", font=("Arial", 11),bg="#2E4053", fg="white").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.num1 = tk.Entry(marco, font=("Arial", 11), width=15)
        self.num1.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(marco, text="Número 2:", font=("Arial", 11),bg="#2E4053", fg="white").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.num2 = tk.Entry(marco, font=("Arial", 11), width=15)
        self.num2.grid(row=1, column=1, padx=5, pady=5)

        marco_botones = tk.Frame(root, bg="#2E4053")
        marco_botones.pack(pady=10)

        self.crear_boton(marco_botones, "+", self.sumar, 0, 0)
        self.crear_boton(marco_botones, "-", self.restar, 0, 1)
        self.crear_boton(marco_botones, "x", self.multiplicar, 0, 2)
        self.crear_boton(marco_botones, "÷", self.dividir, 0, 3)
        self.crear_boton(marco_botones, "Limpiar", self.limpiar, 1, 0, 4)

        self.resultado = tk.Label(
            root, text="Resultado: ---", font=("Arial", 13, "bold"),
            bg="#1ABC9C", fg="white", width=30, height=2, relief="ridge"
        )
        self.resultado.pack(pady=15)

    def crear_boton(self, padre, texto, comando, fila, col, colspan=1):
        btn = tk.Button(
            padre, text=texto, font=("Arial", 11, "bold"),
            bg="#5D6D7E", fg="white", width=8, height=1,
            command=comando, relief="raised", bd=3
        )
        btn.grid(row=fila, column=col, columnspan=colspan, padx=4, pady=4)

    def obtener_numeros(self):
        try:
            a = float(self.num1.get())
            b = float(self.num2.get())
            return a, b
        except ValueError:
            if self.num1.get() == "" or self.num2.get() == "":
                messagebox.showerror("Error", "Los campos no pueden estar vacíos.")
            else:
                messagebox.showerror("Error", "Ingrese solo números válidos.")
            return None, None

    def sumar(self):
        a, b = self.obtener_numeros()
        if a is not None:
            self.mostrar_resultado(f"{a} + {b} = {a + b}")

    def restar(self):
        a, b = self.obtener_numeros()
        if a is not None:
            self.mostrar_resultado(f"{a} - {b} = {a - b}")

    def multiplicar(self):
        a, b = self.obtener_numeros()
        if a is not None:
            self.mostrar_resultado(f"{a} x {b} = {a * b}")

    def dividir(self):
        a, b = self.obtener_numeros()
        if a is not None:
            if b == 0:
                messagebox.showerror("Error", "No se puede dividir entre cero.")
                return
            self.mostrar_resultado(f"{a} ÷ {b} = {a / b:.2f}")

    def limpiar(self):
        self.num1.delete(0, tk.END)
        self.num2.delete(0, tk.END)
        self.resultado.config(text="Resultado: ---")
        self.num1.focus()

    def mostrar_resultado(self, texto):
        self.resultado.config(text=texto)
