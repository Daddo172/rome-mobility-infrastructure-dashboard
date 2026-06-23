import pandas as pd
import streamlit as st
import plotly.express as px

# 1. Configurazione pagina
st.set_page_config(layout="wide")
st.title("🅿️ Roma Mobility: Analisi Infrastrutturale Parcheggi")

# 2. Caricamento e Pulizia Dati (fatto una sola volta)
@st.cache_data
def load_data():
    # Aggiungiamo 'sep=";"' perché il tuo file usa il punto e virgola
    # Aggiungiamo 'on_bad_lines="skip"' per evitare che si blocchi se una riga è strana
    df = pd.read_csv('parcheggi_roma.csv', sep=';', on_bad_lines='skip', encoding='utf-8')
    
    # Pulizia forzata
    df['P_Totali'] = pd.to_numeric(df['P_Totali'], errors='coerce')
    df['P_Disabili'] = pd.to_numeric(df['P_Disabili'], errors='coerce')
    df['Perc_Disabili'] = (df['P_Disabili'] / df['P_Totali']) * 100
    return df

df = load_data()

# 3. KPI Totali
col1, col2, col3 = st.columns(3)
col1.metric("Totale Parcheggi", len(df))
col2.metric("Posti Auto Totali", int(df['P_Totali'].sum()))
col3.metric("Media Posti/Parcheggio", f"{df['P_Totali'].mean():.0f}")

# 4. Grafico 1: Capacità per Linea
st.subheader("Analisi della Capacità")
fig1 = px.bar(df.groupby('TPL')['P_Totali'].sum().reset_index(), 
              x='TPL', y='P_Totali', 
              color='TPL',
              title="Capacità Totale per Linea TPL")
st.plotly_chart(fig1, use_container_width=True)

# 5. Grafico 2: Percentuale Disabili
st.subheader("Inclusività Infrastrutturale")
fig2 = px.scatter(df, x='P_Totali', y='Perc_Disabili', color='TPL', 
                  hover_data=['Nome'],
                  title="Correlazione tra Dimensione Parcheggio e Posti Disabili (%)")
st.plotly_chart(fig2, use_container_width=True)
