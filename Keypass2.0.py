import random
import tkinter as tk
from tkinter import messagebox

def gerar_senha():
    caracteres = "zaq12xvfr4bgr5nht5!@#$%&*"
    senha = ''.join(random.choice(caracteres) for _ in range(8))
    resultado_var.set(senha)

# Criar janela
janela = tk.Tk()
janela.title("Gerador de Senhas")
janela.geometry("300x200")
janela.resizable(False, False)

# Texto de título
titulo = tk.Label(janela, text="Gerador de Senhas", font=("Arial", 16, "bold"))
titulo.pack(pady=10)

# Botão para gerar senha
botao = tk.Button(janela, text="Gerar Senha", command=gerar_senha, font=("Arial", 12))
botao.pack(pady=10)

# Campo para mostrar a senha gerada
resultado_var = tk.StringVar()
resultado = tk.Entry(janela, textvariable=resultado_var, font=("Arial", 14), justify="center")
resultado.pack(pady=10)

# Iniciar a interface
janela.mainloop()
