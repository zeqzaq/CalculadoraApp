import tkinter as tk
from tkinter import messagebox

#Simulador del clima
class CalculadoraClima:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulador del Clima")
        self.root.geometry("500x400")
        self.root.configure(bg="#34495E")
        self.root.resizable(False, False)

        try:
            icono = tk.PhotoImage(file="../img/icono.png")
            self.root.iconphoto(True, icono)
        except:
            pass

        tk.Label(root, text="Simulador del Clima", font=("Arial", 12, "italic"),
                 bg="#34495E", fg="#ECF0F1").pack(pady=20)

        tk.Label(root, text="Temperatura en °C:", font=("Arial", 11),
                 bg="#34495E", fg="white").pack(pady=5)
        self.temperatura = tk.Entry(root, font=("Arial", 11), width=20)
        self.temperatura.pack(pady=5)

        tk.Button(root, text="Consultar Clima", font=("Arial", 11, "bold"),
                  bg="#2980B9", fg="white", width=25, command=self.consultar_clima).pack(pady=10)

        self.resultado = tk.Label(root, text="Clima: ---", font=("Arial", 13, "bold"),
                                  bg="#1ABC9C", fg="white", width=30, height=2, relief="ridge")
        self.resultado.pack(pady=15)

    def consultar_clima(self):
        try:
            temp = float(self.temperatura.get())

            if temp < 0:
                clima = "Frío extremo"
            elif temp < 15:
                clima = "Frío"
            elif temp < 25:
                clima = "Templado"
            elif temp < 35:
                clima = "Caluroso"
            else:
                clima = "Calor extremo"

            self.resultado.config(text=f"Clima: {clima} ({temp:.1f}°C)")
        except ValueError:
            if self.temperatura.get() == "":
                messagebox.showerror("Error", "El campo no puede estar vacío.")
            else:
                messagebox.showerror("Error", "Ingrese una temperatura válida.")
