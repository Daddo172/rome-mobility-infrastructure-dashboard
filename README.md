🅿️ Roma Mobility: Infrastructure Dashboard<br>
🎯 Obiettivo del Progetto<br>
Sviluppo di un'applicazione web interattiva per l'analisi dell'offerta infrastrutturale dei parcheggi di scambio a Roma. L'obiettivo è fornire uno strumento di supporto alle decisioni (Decision Support System) per analizzare la capacità di interscambio modale (Auto-Ferrovia) e monitorare l'inclusività (posti riservati ai disabili) in relazione alle diverse linee di trasporto pubblico (TPL).<br>
🚀 Funzionalità Principali<br>
KPI Executive: Visualizzazione immediata della capacità totale e dell'offerta media per parcheggio.<br>
Analisi dell'Offerta per Linea: Confronto interattivo tra le diverse linee TPL (Metro, Ferroviarie, Linee di Superficie).<br>
Correlazione Inclusività: Analisi scatter plot per valutare se la scala dell'infrastruttura sia correlata a una maggiore offerta di posti dedicati ai disabili.<br>
Filtri dinamici: Interfaccia intuitiva costruita con Streamlit.<br>
📊 Visualizzazione dell'App<br>
Analisi Capacità<br>
![alt text](images/capacita_tpl.png)

Descrizione: Distribuzione della capacità totale di posti auto per ciascuna linea TPL.<br>
Analisi Inclusività<br>
![alt text](images/correlazione_disabili.png)

Descrizione: Analisi della correlazione tra dimensione totale del parcheggio e percentuale di posti disabili offerti.<br>
💻 Tech Stack<br>
Dashboarding: Python, Streamlit<br>
Data Manipulation: Pandas, NumPy<br>
Interactive Charts: Plotly Express<br>
Deployment: Streamlit Community Cloud (Pronto)<br>
📁 Repository Structure<br>
app.py: Codice sorgente dell'applicazione Streamlit.<br>
parcheggi_roma.csv: Dataset pulito.<br>
requirements.txt: Dipendenze del progetto.<br>
💡 Come eseguire l'App<br>
Clona il repository.<br>
Installa le dipendenze: pip install -r requirements.txt<br>
Lancia l'applicazione: python -m streamlit run app.py<br>
