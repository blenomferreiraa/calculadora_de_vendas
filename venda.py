import customtkinter as ctk
from tkinter import messagebox
import re

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# ================= FUNÇÕES =================
def focar_proximo_ou_calcular(event):
    widget_atual = event.widget
    # identifica o último Entry visível
    ult_entry = None
    for e in reversed(entries):
        if e.winfo_ismapped():  # só considera entradas visíveis
            ult_entry = e
            break

    if widget_atual == ult_entry:
        calcular()  # último campo → calcula
    else:
        proximo = widget_atual.tk_focusNext()
        if proximo:
            proximo.focus()
    return "break"

def formatar_moeda_tempo_real(entry):
    valor = entry.get()
    numeros = re.sub(r"\D", "", valor)

    if numeros == "":
        entry.delete(0, "end")
        return

    valor_float = int(numeros) / 100
    texto = f"{valor_float:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    entry.delete(0, "end")
    entry.insert(0, texto)

def obter_valor(entry):
    return float(entry.get().replace(".", "").replace(",", "."))

def somente_inteiro(valor):
    return valor == "" or re.fullmatch(r"\d+", valor)

# ================= JANELA PRINCIPAL =================
app = ctk.CTk()
app.title("Cálculo de Preço de Venda")
app.geometry("500x650")
app.resizable(False, False)

vcmd_int = app.register(somente_inteiro)

# ================= FUNÇÃO CALCULAR =================
def calcular():
    try:
        nome = entry_nome.get()
        valor_compra = obter_valor(entry_compra)
        valor_icms = obter_valor(entry_icms)
        qtd = int(entry_qtd.get())
        margem = float(entry_margem.get().replace(",", "."))
        custos = obter_valor(entry_custos) if checkbox_custos.get() else 0

        custo_unitario = (valor_compra + valor_icms + custos) / qtd
        venda = custo_unitario * (1 + margem / 100)

        abrir_resultado(nome, valor_compra, valor_icms, custos, margem, venda)

    except ValueError:
        messagebox.showerror("Erro", "Verifique os campos e tente novamente.")

# ================= RESULTADO =================
def abrir_resultado(nome, compra, icms, custos, margem, venda):
    app.withdraw()
    janela = ctk.CTkToplevel(app)
    janela.title("Resultado")
    janela.geometry("450x420")
    janela.resizable(False, False)

    ctk.CTkLabel(
        janela,
        text="PREÇO DE VENDA",
        font=ctk.CTkFont(size=18, weight="bold")
    ).pack(pady=15)

    # Nome do Produto
    ctk.CTkLabel(
        janela,
        text=f"Produto: {nome}",
        justify="left",
        font=ctk.CTkFont(size=14)
    ).pack(anchor="w", padx=20)

    # Vermelho: preço de compra, ICMS, outros custos
    for label, valor in [("Preço de Compra", compra), ("ICMS", icms), ("Outros Custos", custos)]:
        ctk.CTkLabel(
            janela,
            text=f"{label}: R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."),
            justify="left",
            font=ctk.CTkFont(size=14),
            text_color="red"
        ).pack(anchor="w", padx=20)

    # Verde: margem e preço final
    ctk.CTkLabel(
        janela,
        text=f"Margem de Lucro: {margem}%",
        justify="left",
        font=ctk.CTkFont(size=14),
        text_color="green"
    ).pack(anchor="w", padx=20)

    ctk.CTkLabel(
        janela,
        text=f"PREÇO FINAL: R$ {venda:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."),
        justify="left",
        font=ctk.CTkFont(size=14, weight="bold"),
        text_color="green"
    ).pack(anchor="w", padx=20, pady=10)

    def voltar():
        janela.destroy()
        app.deiconify()
        entry_nome.focus()

    ctk.CTkButton(janela, text="Voltar", command=voltar).pack(pady=20)

# ================= INTERFACE =================
ctk.CTkLabel(
    app,
    text="CÁLCULO DE PREÇO DE VENDA",
    font=ctk.CTkFont(size=18, weight="bold")
).pack(pady=10)

def criar_campo(texto, tipo="texto"):
    label = ctk.CTkLabel(app, text=texto)
    label.pack(anchor="w", padx=40)

    entry = ctk.CTkEntry(app)
    entry.pack(pady=5, padx=40, fill="x")
    entry.bind("<Return>", focar_proximo_ou_calcular)

    if tipo == "numero":
        entry.bind("<KeyRelease>", lambda e: formatar_moeda_tempo_real(entry))
    elif tipo == "inteiro":
        entry.configure(validate="key", validatecommand=(vcmd_int, "%P"))

    return label, entry

# Campos
label_nome, entry_nome = criar_campo("Nome do Produto", "texto")
label_compra, entry_compra = criar_campo("Preço de Compra (R$)", "numero")
label_icms, entry_icms = criar_campo("Valor do ICMS (R$)", "numero")
label_qtd, entry_qtd = criar_campo("Quantidade", "inteiro")
label_margem, entry_margem = criar_campo("Margem de Lucro (%)", "numero")
label_custos, entry_custos = criar_campo("Outros Custos (R$)", "numero")
entry_custos.bind("<Return>", lambda e: calcular())
label_custos.pack_forget()
entry_custos.pack_forget()

# Lista de entries na ordem
entries = [entry_nome, entry_compra, entry_icms, entry_qtd, entry_margem, entry_custos]

# Botão calcular
btn_calcular = ctk.CTkButton(app, text="Calcular Preço de Venda", command=calcular)
btn_calcular.pack(pady=15)

# Checkbox para mostrar/ocultar Outros Custos
def toggle_custos():
    if checkbox_custos.get():
        label_custos.pack(anchor="w", padx=40)
        entry_custos.pack(pady=5, padx=40, fill="x")
        entry_custos.focus()
        # Reposiciona o botão abaixo do entry
        btn_calcular.pack_forget()
        btn_calcular.pack(pady=15, padx=40, fill="x")
    else:
        entry_custos.delete(0, "end")
        label_custos.pack_forget()
        entry_custos.pack_forget()
        # Botão volta para posição abaixo do checkbox
        btn_calcular.pack_forget()
        btn_calcular.pack(pady=15)

checkbox_custos = ctk.CTkCheckBox(
    app,
    text="Possui outros custos?",
    command=toggle_custos
)
checkbox_custos.pack(pady=10)

entry_nome.focus()
app.mainloop()
