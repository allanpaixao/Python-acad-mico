import tkinter as tk
from tkinter import messagebox
              
def calcular_imc():
    try:
        peso= float(entry_peso.get())
        altura= float(entry_altura.get())
        imc= peso / (altura**2)
        if imc < 18.5:
            situacao= "abaixo do peso"
        elif 18.5 <= imc <=24.9:
            situacao= "peso normal"
        elif 25 <= imc < 29.9:
            situacao= "sobrepeso"
        else:
            situacao= "obesidade"

        messagebox.showinfo("Resultado", f"seu IMC é: {imc:.2f} \nSituação: {situacao}")

    except ValueError:
            messagebox.showerror("Erro", "Por Favor, insira valores validos.")

janela= tk.Tk()
janela.title("calculadora de IMC")

label_peso = tk.Label(janela, text="peso (kg)")
label_peso.grid(row=0, column=0, padx=10, pady=10)
entry_peso = tk.Entry(janela)
entry_peso.grid(row=0, column=1, padx=10, pady=10)

label_altura = tk.Label(janela, text="altura (m):")
label_altura.grid(row=1, column=0, padx=10, pady=10)
entry_altura = tk.Entry(janela)
entry_altura.grid(row=1, column=1, padx=10, pady=10)

botao_calcular= tk.Button(janela, text="Calcular IMC", command=calcular_imc)
botao_calcular.grid(row=2, column=0, columnspan=2, pady=20)

janela.mainloop()
