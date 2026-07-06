import tkinter as tk
from tkinter import messagebox
from user_repository import UserRepository
from register_window import RegisterWindow


class LoginWindow:
    def __init__(self, root, on_login_success):
        self.repository = UserRepository()
        self.root = root
        self.on_login_success = on_login_success
        self.limpiar()
        self.crear_componentes()

    def limpiar(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def crear_componentes(self):
        self.root.title("Iniciar Sesión")
        self.root.geometry("400x450")
        self.root.configure(bg="#2C3E50")
        self.root.resizable(False, False)

        try:
            logo = tk.PhotoImage(file="img/icono.png")
            logo = logo.subsample(12, 12)
            lbl_logo = tk.Label(self.root, image=logo, bg="#2C3E50")
            lbl_logo.image = logo
            lbl_logo.pack(pady=(30, 10))
        except:
            pass

        tk.Label(self.root, text="Iniciar Sesión", font=("Arial", 18, "bold"),
                 bg="#2C3E50", fg="#ECF0F1").pack(pady=(5, 20))

        marco = tk.Frame(self.root, bg="#2C3E50")
        marco.pack()

        tk.Label(marco, text="Usuario:", font=("Arial", 12),
                 bg="#2C3E50", fg="white").pack(anchor="w")
        self.txt_usuario = tk.Entry(marco, font=("Arial", 12), width=25)
        self.txt_usuario.pack(pady=(0, 10))

        tk.Label(marco, text="Contraseña:", font=("Arial", 12),
                 bg="#2C3E50", fg="white").pack(anchor="w")
        self.txt_clave = tk.Entry(marco, font=("Arial", 12), width=25, show="*")
        self.txt_clave.pack(pady=(0, 10))

        marco_botones = tk.Frame(self.root, bg="#2C3E50")
        marco_botones.pack(pady=20)

        tk.Button(marco_botones, text="Registrarme", font=("Arial", 11, "bold"),
                  bg="#27AE60", fg="white", width=12, command=self.abrir_registro
                  ).pack(side=tk.LEFT, padx=5)

        tk.Button(marco_botones, text="Login", font=("Arial", 11, "bold"),
                  bg="#2980B9", fg="white", width=12, command=self.login
                  ).pack(side=tk.LEFT, padx=5)

    def login(self):
        usuario = self.txt_usuario.get()
        clave = self.txt_clave.get()

        if usuario == "" or clave == "":
            messagebox.showwarning("Campos vacíos", "Ingrese usuario y contraseña")
            return

        user_data = self.repository.validar_usuario(usuario, clave)

        if user_data:
            messagebox.showinfo("Acceso permitido", f"Bienvenido {user_data['nombre']}")
            self.on_login_success(user_data)
        else:
            messagebox.showerror("Acceso denegado", "Usuario o contraseña incorrectos")

    def abrir_registro(self):
        RegisterWindow(self.root)
