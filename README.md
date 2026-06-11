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
💡 Insights & Recommendations<br>
Dall'analisi esplorativa condotta sui dati, sono emersi i seguenti punti chiave:<br>
Cosa abbiamo capito (Insights)<br>
Concentrazione Strategica: L'offerta di parcheggi di scambio a Roma non è distribuita uniformemente. Alcune linee (come la Metro B o le linee ferroviarie FL) concentrano la maggior parte della capacità di interscambio, fungendo da veri e propri "polmoni" del sistema di trasporto cittadino.<br>
Correlazione Dimensionale: Dall'analisi della correlazione (Scatter Plot) è emerso che i parcheggi di grandi dimensioni non mostrano necessariamente una proporzionalità diretta nella quota di posti riservati ai disabili, suggerendo una potenziale area di miglioramento in termini di equità infrastrutturale.<br>
Cosa possiamo migliorare (Recommendations)<br>
Ottimizzazione dell'Inclusività: Per le infrastrutture di grandi dimensioni, si consiglia una revisione degli stalli riservati per garantire che l'accessibilità cresca in modo costante rispetto alla capacità totale del parcheggio.<br>
Potenziamento del Monitoraggio: L'attuale assenza di dati geospaziali strutturati e di dati di occupazione in tempo reale limita le possibilità di un'analisi predittiva. Una futura evoluzione del progetto prevede l'integrazione di API per il monitoraggio live e la mappatura GIS avanzata.<br>
Integrazione Tariffe: Un'analisi futura potrebbe correlare la tariffazione oraria con il tasso di occupazione effettivo, permettendo di identificare quali tariffe incentivano maggiormente l'uso del mezzo pubblico.<br>
💻 Tech Stack<br>
Dashboarding: Python, Streamlit<br>
Data Manipulation: Pandas, NumPy<br>
Interactive Charts: Plotly Express<br>
Deployment: Streamlit Community Cloud <br>
📁 Repository Structure<br>
app.py: Codice sorgente dell'applicazione Streamlit.<br>
parcheggi_roma.csv: Dataset pulito.<br>
requirements.txt: Dipendenze del progetto.<br>
💡 Come eseguire l'App<br>
Clona il repository.<br>
Installa le dipendenze: pip install -r requirements.txt<br>
Lancia l'applicazione: python -m streamlit run app.py<br>
