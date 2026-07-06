import tkinter as tk
from calculadoras.calculadora_IMC import CalculadoraIMC
from calculadoras.calculadora import CalculadoraBasica
from calculadoras.calculadora_edad import CalculadoraEdad
from calculadoras.calculadora_temp import CalculadoraTemp
from calculadoras.calculadora_salario import CalculadoraSalario
from calculadoras.calculadora_promedio import CalculadoraPromedio
from calculadoras.calculadora_monedas import CalculadoraMonedas
from calculadoras.calculadora_descuentos import CalculadoraDescuentos
from calculadoras.calculadora_clima import CalculadoraClima
from calculadoras.calculadora_combustible import CalculadoraCombustible
from calculadoras.calculadora_servicios import CalculadoraServicios


class HomeWindow:
    def __init__(self, root, user_data, on_logout):
        self.root = root
        self.user_data = user_data
        self.on_logout = on_logout
        self.limpiar()
        self.crear_componentes()

    def limpiar(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def crear_componentes(self):
        self.root.title("Panel Principal")
        self.root.geometry("600x750")
        self.root.configure(bg="#34495E")
        self.root.resizable(False, False)

        canvas = tk.Canvas(self.root, bg="#34495E", highlightthickness=0)
        scrollbar = tk.Scrollbar(self.root, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg="#34495E")

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="n", width=480)
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        def _on_mousewheel(event):
            if event.delta:
                canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

        canvas.bind_all("<MouseWheel>", _on_mousewheel)

        self.construir_contenido(scrollable_frame)

    def construir_contenido(self, parent):
        try:
            logo = tk.PhotoImage(file="img/icono.png")
            logo = logo.subsample(12, 12)
            lbl_logo = tk.Label(parent, image=logo, bg="#34495E")
            lbl_logo.image = logo
            lbl_logo.pack(pady=(20, 5))
        except:
            pass

        tk.Label(parent, text=f"Hola {self.user_data['nombre']}",
                 font=("Arial", 16, "bold"), bg="#34495E", fg="#F0B27A").pack(pady=(5, 5))

        tk.Button(parent, text="Cerrar Sesión", font=("Arial", 10, "bold"),
                  bg="#E74C3C", fg="white", command=self.cerrar_sesion).pack(pady=(0, 15))

        tk.Label(parent, text="¿Qué quieres hacer?", font=("Arial", 13, "italic"),
                 bg="#34495E", fg="#ECF0F1").pack(pady=(5, 15))

        tk.Button(parent, text="Calculadora Básica", font=("Arial", 11, "bold"),
                  bg="#2980B9", fg="white", width=30, command=self.abrir_calculadora).pack(pady=4)

        tk.Button(parent, text="Calculadora de Edad", font=("Arial", 11, "bold"),
                  bg="#27AE60", fg="white", width=30, command=self.abrir_calculadora_edad).pack(pady=4)

        tk.Button(parent, text="Calculadora de Temperatura", font=("Arial", 11, "bold"),
                  bg="#8E44AD", fg="white", width=30, command=self.abrir_calculadora_temp).pack(pady=4)

        tk.Button(parent, text="Calculadora de IMC", font=("Arial", 11, "bold"),
                  bg="#E74C3C", fg="white", width=30, command=self.abrir_calculadora_IMC).pack(pady=4)

        tk.Button(parent, text="Calculadora de Salario", font=("Arial", 11, "bold"),
                  bg="#F39C12", fg="white", width=30, command=self.abrir_calculadora_salario).pack(pady=4)

        tk.Button(parent, text="Calculadora de Promedio", font=("Arial", 11, "bold"),
                  bg="#1ABC9C", fg="white", width=30, command=self.abrir_calculadora_promedio).pack(pady=4)

        tk.Button(parent, text="Conversor de Monedas", font=("Arial", 11, "bold"),
                  bg="#3498DB", fg="white", width=30, command=self.abrir_calculadora_monedas).pack(pady=4)

        tk.Button(parent, text="Calculadora de Descuentos", font=("Arial", 11, "bold"),
                  bg="#E67E22", fg="white", width=30, command=self.abrir_calculadora_descuentos).pack(pady=4)

        tk.Button(parent, text="Simulador del Clima", font=("Arial", 11, "bold"),
                  bg="#9B59B6", fg="white", width=30, command=self.abrir_calculadora_clima).pack(pady=4)

        tk.Button(parent, text="Calculadora de Combustible", font=("Arial", 11, "bold"),
                  bg="#2ECC71", fg="white", width=30, command=self.abrir_calculadora_combustible).pack(pady=4)

        tk.Button(parent, text="Calculadora de Servicios", font=("Arial", 11, "bold"),
                  bg="#E74C3C", fg="white", width=30, command=self.abrir_calculadora_servicios).pack(pady=4)

        tk.Frame(parent, bg="#34495E", height=2, bd=1, relief="sunken").pack(fill="x", pady=15, padx=20)

        tk.Label(parent, text="Información Personal", font=("Arial", 12, "bold"),
                 bg="#34495E", fg="#ECF0F1").pack(pady=(5, 10))

        info = [
            f"Nombre: {self.user_data['nombre']}",
            f"Cédula: {self.user_data['cedula']}",
            f"Celular: {self.user_data['celular']}",
            f"Correo: {self.user_data['correo']}",
            f"Usuario: {self.user_data['usuario']}",
        ]
        for texto in info:
            tk.Label(parent, text=texto, font=("Arial", 10),
                     bg="#34495E", fg="#BDC3C7").pack(anchor="w", padx=40)

        tk.Frame(parent, bg="#34495E", height=2, bd=1, relief="sunken").pack(fill="x", pady=15, padx=20)

        tk.Label(parent, text="Realizado por:(Cristian Marquez Arcila)", font=("Arial", 10, "italic"),
                 bg="#34495E", fg="#7F8C8D").pack(pady=(5, 15))

    def cerrar_sesion(self):
        self.on_logout()

    def abrir_calculadora(self):
        ventana = tk.Toplevel(self.root)
        CalculadoraBasica(ventana)

    def abrir_calculadora_edad(self):
        ventana = tk.Toplevel(self.root)
        CalculadoraEdad(ventana)

    def abrir_calculadora_temp(self):
        ventana = tk.Toplevel(self.root)
        CalculadoraTemp(ventana)

    def abrir_calculadora_IMC(self):
        ventana = tk.Toplevel(self.root)
        CalculadoraIMC(ventana)

    def abrir_calculadora_salario(self):
        ventana = tk.Toplevel(self.root)
        CalculadoraSalario(ventana)

    def abrir_calculadora_promedio(self):
        ventana = tk.Toplevel(self.root)
        CalculadoraPromedio(ventana)

    def abrir_calculadora_monedas(self):
        ventana = tk.Toplevel(self.root)
        CalculadoraMonedas(ventana)

    def abrir_calculadora_descuentos(self):
        ventana = tk.Toplevel(self.root)
        CalculadoraDescuentos(ventana)

    def abrir_calculadora_clima(self):
        ventana = tk.Toplevel(self.root)
        CalculadoraClima(ventana)

    def abrir_calculadora_combustible(self):
        ventana = tk.Toplevel(self.root)
        CalculadoraCombustible(ventana)

    def abrir_calculadora_servicios(self):
        ventana = tk.Toplevel(self.root)
        CalculadoraServicios(ventana)
