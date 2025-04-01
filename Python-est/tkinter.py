import tkinter as tk
from tkinter import messagebox

class CalculadoraIMC:
    def __init__(self,root):
        self.root = root
        self.root.title("Calculadora de IMC")

        #Interface gráfica
        self.label_peso = tk.Label(self.root, text="Peso (kg):")
        self.label_peso.grid(row=0, column=0, padx=10, pady=10)
        self.entry_peso = tk.Entry(self.root)
        self.entry_peso.grid(row=0, column=1, padx=10,pady=10)

        self.label_altura = tk.Label(self.root, text="Altura (m):")
        self.label_altura.grid(row=1, column=0, padx=10, pady=10)
        self.entry_altura = tk.Entry(self.root)
        self.entry_altura.grid(row=1, column=1, padx=10,pady=10)

        self.botao_calcular = tk.Button(self.root, text="Calcular IMC" , command=self.calcular)
        self.botao_calcular.grid(row=2, column=0 , columnspan=2, pady=20)

    def calcular_imc(self):
         try:
             peso = float(self.entry_peso.get())
             altura = float(self.entry_altura.get())
             imc = peso/ (altura**2)
             if imc <18.5:
                 situacao = "Abaixo do peso"
             elif 18.5 <= imc < 24.9:
                 situacao = "Peso normal"
             elif 25 <= imc < 29.9:
                 situacao = "Sobrepeso"
             else:
                 situacao = "Obsidade"

             menssagebox.showinfo("Resultado" , f"Seu IMC é: {imc:.2f}\n Situação: {situacao}")
         except ValueError: 
             massagebox.showinfo("Erro" , "POr favor insira valores validos.")

           #Inicializando a interface
if __name__ == "main":
    root = tk.TK()
    app = CalculadoraIMC (root)
    root.mainloop() 
             
