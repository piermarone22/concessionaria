import streamlit as st
st.title("EVERGREEN")

col1,col2 = st.columns(2)
with col1:
    st.title("Rata")

with col2:
    ratae = st.number_input("",min_value=0, step=10)
    #st.metric(label="Rata", value=f"{st.session_state['rata']:,.2f} €")

st.write("")
st.write("")
st.write("")
st.divider()

st.header("Quale ha più senso?")
col1,col2 = st.columns(2)

with col1:
    st.metric(label="COSTO MENSILE CON FINANZIAMENTO", value=f"{st.session_state['tot_tot']:,.2f} €")
    st.header("Svantaggi")
    st.markdown("""
- Rischi legati alle normative europee
- Incertezza sulla longevità della macchina
- Auto che perde di valore
""")





with col2:
    st.metric(label="COSTO MENSILE CON EVERGREEN", value=f"{ratae} €")
    st.header("Vantaggi")
    st.markdown("""
- Serenità e tranquillità alla guida
- La bellezza di un'auto sempre nuova
- Estensione di garanzia
- Assicurazione: furto e incendio, atti vandalici, urto contro animali selvatici, grandine/eventi atmosferici, cristalli
""")

