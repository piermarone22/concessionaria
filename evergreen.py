import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

with open("style.css") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

 

st.title("Finanziamento classico")

st.subheader("Inserisci i dati per calcolare i costi totali")

col1,col2,col3 = st.columns(3)
with col1:
    st.title("Rata")
with col2:
    st.session_state["rata"] = st.number_input("",min_value=0, step=10)
st.write("")
st.write("")
st.write("")
st.divider()

col1,col2,col3 = st.columns(3)

with col1:
    assicurazione = st.number_input("Assicurazione", min_value=0, step=50)
with col2:
    anni_ass = st.slider("Anni", min_value=1, max_value=20)

spesa_ass = assicurazione * anni_ass

with col3:
    st.write("")
    st.write("")
    st.metric("💵 Totale Assicurazioni", f"{spesa_ass:,.2f} €")
col1,col2,col3 = st.columns(3)

with col1:
    manu = st.number_input("Manutenzioni", min_value=0, step=50)

with col2:
    anni_manu = st.slider("Anni", min_value=1, max_value=20, key="slidermanu")

spesa_manu = manu * anni_manu

with col3:
    st.write("")
    st.write("")
    st.metric("💵 Totale Manutenzioni", f"{spesa_manu:,.2f} €")

col1,col2,col3 = st.columns(3)
with col1:
    gomme = st.number_input("Gomme", min_value=0, step=50)

with col2:
    anni_gomme = st.slider("Numero di treni", min_value=1, max_value=20, key="slidergomme")

spesa_gomme = gomme * anni_gomme

with col3:
    st.write("")
    st.write("")
    st.metric("💵 Totale Gomme", f"{spesa_gomme:,.2f} €")

col1,col2,col3 = st.columns(3)

with col1:
    impre = st.number_input("Imprevisti", min_value=0, step=50)

with col2:
    st.write("")
    st.write("")
    st.metric("💵 Totale Imprevisti", f"{impre:,.2f} €")


totale = spesa_ass + spesa_manu + spesa_gomme + impre

with col3:
    st.write("") 
    st.write("")
    st.metric("TOTALE", f"{totale:,.2f} €") 


tot_mese = round(totale / anni_ass / 12)

anni_ass = int(anni_ass)
st.header("Costi di guida")

col1,col2,col3,col4,col5 = st.columns(5)

with col1:
    st.metric("TOTALE COSTI", f"{totale:,d} €")

with col2:
    st.header("/")

with col3:
    st.metric("ANNI", f"{anni_ass:,d}")

with col4:
    st.header("=")

with col5:
    st.metric("TOTALE AL MESE",f"{tot_mese:,.2f} €")



st.session_state['tot_tot'] = st.session_state['rata'] + tot_mese


st.divider()

st.title("Quanto sarà la mia rata?")

col1,col2,col3,col4,col5 = st.columns(5)

with col1:
    st.metric("RATA", f"{st.session_state["rata"]:,.2f} €")

with col2:
    st.header("+")

with col3:
    st.metric("COSTI DI GUIDA",f"{tot_mese:,.2f} €")

with col4:
    st.header("=")

with col5:
    st.metric("TOTALE AL MESE",f"{st.session_state["tot_tot"]:,.2f} €")

st.metric("", f"💵 Spenderai quindi {st.session_state["tot_tot"]:,.2f} € al mese.")


df = pd.DataFrame({
    "Voce di Spesa": ["Assicurazioni", "Manutenzioni", "Gomme", "Imprevisti"],
    "Totale (€)": [spesa_ass, spesa_manu, spesa_gomme, impre]
})


if st.button("CONFRONTA CON EVERGREEN"):
        st.switch_page("pages/ever.py")


with st.expander("Visualizza grafico"):
    st.subheader("📈 Distribuzione Costi")
    fig, ax = plt.subplots()
    ax.bar(df["Voce di Spesa"], df["Totale (€)"], color=['lightblue', 'teal', 'mediumseagreen', 'forestgreen'])
    ax.set_ylabel("Costo (€)")
    ax.set_facecolor((0,0,0,0))
    fig.patch.set_alpha(0)
    ax.tick_params(colors='white')  # Numeri sugli assi bianchi
    ax.yaxis.label.set_color('white')  # Etichetta asse Y bianca
    ax.xaxis.label.set_color('white')  # Etichetta asse X bianca
    ax.spines['bottom'].set_color('white')  # Bordo inferiore bianco
    ax.spines['left'].set_color('white')  # Bordo sinistro bianco
    st.pyplot(fig)



data_to_export = {
    "Voce di Spesa": ["Assicurazioni", "Manutenzioni", "Gomme", "Imprevisti"],
    "Totale (€)": [spesa_ass, spesa_manu, spesa_gomme, impre]
}

# Crea il DataFrame per l'export
df_export = pd.DataFrame(data_to_export)
df_export["Totale (€)"] = df_export["Totale (€)"].apply(lambda x: f"{x:,.2f} €")

# Esporta il DataFrame in un file Excel
def export_to_excel():
    # Crea un Excel writer (in questo caso un file temporaneo)
    with pd.ExcelWriter("/mnt/data/finanziamento_classico.xlsx", engine="xlsxwriter") as writer:
        df_export.to_excel(writer, sheet_name="Costi", index=False)
        
        # Aggiungi il totale generale alla fine del foglio Excel
        df_totale = pd.DataFrame({
            "Voce di Spesa": ["Totale"],
            "Totale (€)": [f"{totale:,.2f} €"]
        })
        df_totale.to_excel(writer, sheet_name="Costi", index=False, startrow=len(df_export) + 2)
        
        # Salva il file Excel
    st.download_button(
        label="Scarica il report in Excel",
        data=open("/mnt/data/finanziamento_classico.xlsx", "rb").read(),
        file_name="finanziamento_classico.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )




# Aggiungi un pulsante che l'utente può premere per scaricare il file Excel
if st.button("Esporta in Excel"):
    export_to_excel()

