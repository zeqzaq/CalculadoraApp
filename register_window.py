import tkinter as tk
from tkinter import messagebox
from user_repository import UserRepository


class RegisterWindow:
    def __init__(self, root):
        self.repository = UserRepository()
        self.root = root

        self.ventana = tk.Toplevel(root)
        self.ventana.title("Registro de Usuario")
        self.ventana.geometry("500x620")
        self.ventana.configure(bg="#2C3E50")
        self.ventana.resizable(False, False)

        try:
            logo = tk.PhotoImage(file="img/icono.png")
            logo = logo.subsample(12, 12)
            lbl_logo = tk.Label(self.ventana, image=logo, bg="#2C3E50")
            lbl_logo.image = logo
            lbl_logo.pack(pady=(20, 5))
        except:
            pass

        self.crear_componentes()

    def crear_componentes(self):
        tk.Label(self.ventana, text="Registro", font=("Arial", 18, "bold"),
                 bg="#2C3E50", fg="#ECF0F1").pack(pady=(5, 15))

        marco = tk.Frame(self.ventana, bg="#2C3E50")
        marco.pack()

        campos = [
            ("Nombre:", "txt_nombre"),
            ("Cédula:", "txt_cedula"),
            ("Celular:", "txt_celular"),
            ("Correo:", "txt_correo"),
            ("Usuario:", "txt_usuario"),
            ("Contraseña:", "txt_clave"),
        ]

        self.entries = {}
        for label, attr in campos:
            tk.Label(marco, text=label, font=("Arial", 11),
                     bg="#2C3E50", fg="white").pack(anchor="w", pady=(5, 0))
            if "clave" in attr:
                entry = tk.Entry(marco, font=("Arial", 11), width=25, show="*")
            else:
                entry = tk.Entry(marco, font=("Arial", 11), width=25)
            entry.pack(pady=(0, 3))
            self.entries[attr] = entry

        tk.Button(self.ventana, text="Registrar", font=("Arial", 12, "bold"),
                  bg="#2980B9", fg="white", width=20, command=self.registrar
                  ).pack(pady=20)

        self.entries["txt_usuario"].bind("<Return>", lambda e: self.registrar())
        self.entries["txt_clave"].bind("<Return>", lambda e: self.registrar())

    def registrar(self):
        nombre = self.entries["txt_nombre"].get()
        cedula = self.entries["txt_cedula"].get()
        celular = self.entries["txt_celular"].get()
        correo = self.entries["txt_correo"].get()
        usuario = self.entries["txt_usuario"].get()
        clave = self.entries["txt_clave"].get()

        if not all([nombre, cedula, celular, correo, usuario, clave]):
            messagebox.showwarning("Campos vacíos", "Todos los campos son obligatorios")
            return

        registrado = self.repository.registrar_usuario(nombre, cedula, celular, correo, usuario, clave)

        if registrado:
            messagebox.showinfo("Registro exitoso", "Usuario registrado correctamente")
            self.ventana.destroy()
        else:
            messagebox.showerror("Error", "No se pudo registrar el usuario. Verifique que el usuario no exista.")
