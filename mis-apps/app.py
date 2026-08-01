import streamlit as st

st.title("Indicador de Preocupación")

verbal = st.checkbox("1. Expresión Verbal - El usuario expresa miedo")
conductual = st.checkbox("2. Comportamiento - Signos de inquietud")

total = 0
if verbal:
    total = total + 1
if conductual:
    total = total + 1

st.divider()

if total == 0:
    st.success("🟢 NIVEL BAJO")
    st.info("Conducta: Continuar con la atención habitual.")

if total == 1:
    st.warning("🟡 NIVEL MODERADO")
    st.info("Conducta: Validar emoción y dar más información.")

if total == 2:
    st.error("🔴 NIVEL ALTO")
    st.info("Conducta: Detener, ofrecer agua y avisar a supervisor.")