import streamlit as st
from main import run_agent

st.set_page_config(page_title="Arkantus", layout="centered")

st.title("Arkantus")

prompt = st.text_area(
    "Digite seu prompt",
    placeholder="Ex: Corrija meu código da calculadora...",
    height=150,
)

verbose = st.checkbox("Mostrar detalhes técnicos (verbose)")

if st.button("Executar"):
    if not prompt.strip():
        st.warning("Por favor, insira um prompt.")
    else:
        with st.spinner("Pensando..."):
            resposta = run_agent(prompt, verbose=verbose)
        st.success("Resposta final:")
        st.code(resposta, language="markdown")
