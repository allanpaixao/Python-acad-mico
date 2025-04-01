import tkinter as tk
from tkinter import messagebox

def calcular_desconto_ir():
    try:
        salario_bruto = float(entry_salario_bruto.get())
        desconto_inss = float(entry_desconto_inss.get())
        
        # Cálculo do salário base e do desconto do imposto de renda
        salario_base = salario_bruto - desconto_inss
        if salario_base <= 1903.98:
            desconto_ir = 0
        elif salario_base <= 2826.65:
            desconto_ir = (salario_base * 0.075) - 142.8
        elif salario_base <= 3751.05:
            desconto_ir = (salario_base * 0.15) - 354.8
        elif salario_base <= 4664.68:
            desconto_ir = (salario_base * 0.225) - 636.13
        else:
            desconto_ir = (salario_base * 0.275) - 869.36
        
        # Exibir o desconto de IR na interface
        label_resultado.config(text=f"Desconto IR: R${desconto_ir:.2f}")
    
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")

# Configuração da janela principal
janela = tk.Tk()
janela.title("Cálculo de Desconto do IR")
janela.geometry("300x200")

# Labels e campos de entrada
tk.Label(janela, text="Salário Bruto:").grid(row=0, column=0, padx=10, pady=10)
entry_salario_bruto = tk.Entry(janela)
entry_salario_bruto.grid(row=0, column=1, padx=10, pady=10)

tk.Label(janela, text="Desconto INSS:").grid(row=1, column=0, padx=10, pady=10)
entry_desconto_inss = tk.Entry(janela)
entry_desconto_inss.grid(row=1, column=1, padx=10, pady=10)

# Botão para calcular
btn_calcular = tk.Button(janela, text="Calcular Desconto IR", command=calcular_desconto_ir)
btn_calcular.grid(row=2, column=0, columnspan=2, pady=10)

# Label para exibir o resultado
label_resultado = tk.Label(janela, text="Desconto IR: R$")
label_resultado.grid(row=3, column=0, columnspan=2, pady=10)

# Executar a janela principal
janela.mainloop()
