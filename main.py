import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import json
import time
import matplotlib.pyplot as plt

def fibonacci(n, memo=None, output_callback=None):
    if memo is None:
        memo = {}

    if n in memo:
        if output_callback:
            output_callback(f"Usando cache: memo[{n}] = {memo[n]}")
        return memo[n], memo

    if n <= 1:
        memo[n] = n
        if output_callback:
            output_callback(f"Calculando: memo[{n}] = {n}")
        return n, memo

    f1, memo = fibonacci(n - 1, memo, output_callback)
    f2, memo = fibonacci(n - 2, memo, output_callback)
    memo[n] = f1 + f2
    if output_callback:
        output_callback(f"Calculando: memo[{n}] = {memo[n]}")
    return memo[n], memo

def calcular_fibonacci():
    try:
        n = int(entry.get())
        output_text.delete("1.0", tk.END)

        def show_log(line):
            output_text.insert(tk.END, line + "\n")
            output_text.see(tk.END)

        start = time.time()
        resultado, cache = fibonacci(n, output_callback=show_log)
        end = time.time()

        output_text.insert(tk.END, f"\nCache Final:\n")
        for k in sorted(cache):
            output_text.insert(tk.END, f"memo[{k}] = {cache[k]}\n")

        output_text.insert(tk.END, f"\nFibonacci({n}) = {resultado}\n")
        output_text.insert(tk.END, f"Tempo: {end - start:.6f} segundos\n")

        global current_cache
        current_cache = cache

    except ValueError:
        messagebox.showerror("Erro", "Digite um número inteiro válido!")

def salvar_cache_json():
    if not current_cache:
        messagebox.showwarning("Aviso", "Calcule um Fibonacci antes de salvar.")
        return

    filepath = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON Files", "*.json")])
    if filepath:
        with open(filepath, 'w') as f:
            json.dump(current_cache, f, indent=4)
        messagebox.showinfo("Sucesso", f"Cache salvo em {filepath}")

def plotar_tempo_execucao():
    try:
        limite = int(entry.get())
        if limite < 1:
            raise ValueError("Digite um número maior que zero.")

        xs = list(range(1, limite + 1))
        tempos = []

        for n in xs:
            start = time.time()
            fibonacci(n)
            end = time.time()
            tempos.append(end - start)

        plt.style.use('seaborn-dark')
        plt.figure(figsize=(8, 4))
        plt.plot(xs, tempos, marker='o', color='cyan')
        plt.title(f"Tempo de execução para n = 1 até {limite}", fontsize=14)
        plt.xlabel("n", fontsize=12)
        plt.ylabel("Tempo (s)", fontsize=12)
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    except ValueError:
        messagebox.showerror("Erro", "Digite um número inteiro válido para o gráfico!")

root = tk.Tk()
root.title("Fibonacci com Memoization")

root.configure(bg="#2e2e2e")

style = ttk.Style()
style.theme_use("clam")
style.configure("TFrame", background="#2e2e2e")
style.configure("TLabel", background="#2e2e2e", foreground="white", font=("Segoe UI", 11))
style.configure("TButton", background="#444", foreground="white", font=("Segoe UI", 10))
style.map("TButton", background=[("active", "#555")])

frame = ttk.Frame(root, padding=10)
frame.pack()

label = ttk.Label(frame, text="Digite um valor para n:")
label.pack(pady=5)

entry = ttk.Entry(frame, font=("Segoe UI", 11))
entry.pack(pady=5)

btn_frame = ttk.Frame(frame)
btn_frame.pack(pady=10)

ttk.Button(btn_frame, text="Calcular", command=calcular_fibonacci).grid(row=0, column=0, padx=6)
ttk.Button(btn_frame, text="Salvar Cache em JSON", command=salvar_cache_json).grid(row=0, column=1, padx=6)
ttk.Button(btn_frame, text="Ver Tempo Execução", command=plotar_tempo_execucao).grid(row=0, column=2, padx=6)

output_text = tk.Text(frame, height=25, width=80, bg="#1e1e1e", fg="#00ffcc", font=("Courier New", 10))
output_text.pack(pady=10)

current_cache = {}

root.mainloop()