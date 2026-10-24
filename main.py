   #imports
import customtkinter as ctk
import random


   #definições
usuarios = [
   "Usuário",

   ]




   #janela
janela = ctk.CTk()
janela.geometry("1920x1080")
janela.title("Calculadora de descontos")
ctk.set_appearance_mode("dark")


   #defs
def menu():
   title1_menu.pack(pady=30)
   title2_menu.pack(pady=30)
   entry_valor_menu.pack(pady=25)
   entry_desconto_menu.pack(pady=25)
   button_calcular_menu.pack(pady=55)


   frame_menu_linha.pack(fill="x", padx=410, pady=15)


   title1_menu_desconto.pack(pady=10)
   title2_menu_valor.pack(pady=10)


def calcular():
   valor = float(entry_valor_menu.get().replace(",", "."))
   desconto = int(entry_desconto_menu.get().replace(",", "."))


   if valor < 0 or desconto < 0 or desconto > 100:
       return


   elif valor and desconto:
       valor_desconto = (valor * desconto )/ 100
       resultado = valor - (valor * desconto)/100


       title1_menu_desconto.configure(text=f"Valor do desconto: {valor_desconto:.2f}")
       title2_menu_valor.configure(text=f"Preço final: {resultado:.2f}")


   #elementos
       #menu
           #texto
title1_menu = ctk.CTkLabel(janela, text=(f"Bem-vindo {random.choice(usuarios)}"), font=("arial", 70, "bold"))
title2_menu = ctk.CTkLabel(janela, text=("Calculadora de descontos"), font=("Arial", 70))


title1_menu_desconto = ctk.CTkLabel(janela, text="Valor do desconto-", font=("arial", 70, "bold"))
title2_menu_valor = ctk.CTkLabel(janela, text="Preço final-", font=("arial", 70, "bold"), text_color="#2ecc71")
           #entrada
entry_valor_menu = ctk.CTkEntry(janela, placeholder_text=("Preço (R$)"), font=("Arial", 50), text_color="white", border_color="white", width=1100, height=80)
entry_desconto_menu = ctk.CTkEntry(janela, placeholder_text=("Desconto (%)"), font=("Arial", 50), text_color="white", border_color="white", width=1100, height=80)
           #botão
button_calcular_menu = ctk.CTkButton(janela, text="Calcular desconto", font=("Arial", 60), width=1100, height=100, command=calcular)
           #frame
frame_menu_linha = ctk.CTkFrame(janela, height=2, fg_color="#404040", corner_radius= 0)


menu()


janela.mainloop()
