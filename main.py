import tkinter as tk
from login_window import LoginWindow
from home_window import HomeWindow


class Aplicacion:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Sistema Integrado")
        self.mostrar_login()

    def mostrar_login(self):
        LoginWindow(self.root, self.mostrar_home)

    def mostrar_home(self, user_data):
        HomeWindow(self.root, user_data, self.mostrar_login)

    def ejecutar(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = Aplicacion()
    app.ejecutar()
