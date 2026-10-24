
import streamlit as st

st.set_page_config(page_title="Calculadora de descontos")

st.title("Calculadora de descontos")
st.write("Descubra quanto você economiza!")

preco = st.text_input("Preço do produto (R$)")
desconto = st.text_input("Desconto (%)")

if st.button("Calcular desconto"):
    try:
        valor = float(preco.replace(",", "."))
        porcentagem = float(desconto.replace(",", "."))

        if valor < 0 or not 0 <= porcentagem <= 100:
            st.error("Confira o preço e o desconto.")
        else:
            economia = valor * porcentagem / 100
            total = valor - economia

            st.success(f"Você economiza: R$ {economia:.2f}")
            st.subheader(f"Preço final: R$ {total:.2f}")

    except ValueError:
        st.error("Digite números válidos nos dois campos.")
