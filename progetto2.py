"""Un centro di analisi mediche deve informatizzare parte della gestione dei pazienti, 
dei medici e dei referti di laboratorio. Si richiede la progettazione e la realizzazione di un programma in Python 
che permetta di gestire i dati in maniera strutturata, utilizzando programmazione a oggetti (OOP) 
e la libreria NumPy per l’elaborazione numerica dei dati clinici. """

"""Parte 1 Variabili e Tipi di Dati
Definire le variabili necessarie per rappresentare:
Nome, cognome e codice fiscale di un paziente (stringhe).
Età e peso del paziente (interi e float).
Lista delle analisi effettuate (lista di stringhe).
Scrivere almeno 3 pazienti diversi con queste variabili.
"""

import numpy as np

# Definizione delle variabili per rappresentare i dati del paziente

paziente1_nome = "Mario"
paziente1_cognome = "Rossi"
paziente1_codice_fiscale = "RSSMRA80A01H501Z"
paziente1_eta = 40
paziente1_peso = 75.5
paziente1_analisi = ["Emocromo", "Colesterolo", "Glicemia"]

paziente2_nome = "Giulia"
paziente2_cognome = "Bianchi"
paziente2_codice_fiscale = "BNCGLI85B45H501Z"
paziente2_eta = 35
paziente2_peso = 68.0
paziente2_analisi = ["Emocromo", "Pressione arteriosa"]

paziente3_nome = "Luca"
paziente3_cognome = "Verdi"
paziente3_codice_fiscale = "VRDLCU90C01H501Z"
paziente3_eta = 50
paziente3_peso = 85.5
paziente3_analisi = ["Emocromo", "Colesterolo", "Glicemia", "Pressione arteriosa"]

#--------------------------#

"""Parte 2  Classi e OOP
Creare una classe Paziente con:
Attributi: nome, cognome, codice_fiscale, eta, peso, analisi_effettuate.
Metodo scheda_personale() che restituisca una stringa con i dati principali del paziente.
Creare una classe Medico con:
Attributi: nome, cognome, specializzazione.
Metodo visita_paziente(paziente) che stampi quale medico sta visitando quale paziente.
Creare una classe Analisi che contenga:
Tipo di analisi (es. glicemia, colesterolo).
Risultato numerico.
Metodo valuta() che stabilisca se il valore è nella norma (criteri inventati da voi).
"""

"""Parte 3  Uso di NumPy
Supponiamo che il centro raccolga i risultati di un certo esame per 10 pazienti.
Rappresentare i valori in un array NumPy.
Calcolare con NumPy: media, valore massimo, valore minimo e deviazione standard."""

"""Parte 4  Integrazione OOP + NumPy
Aggiornare la classe Paziente inserendo un attributo risultati_analisi che sia un array NumPy 
contenente i valori numerici delle analisi svolte.
Creare un metodo statistiche_analisi() che calcoli:
Media dei valori
Minimo e massimo
Deviazione standard"""

class Paziente:
    def __init__(self, nome, cognome, codice_fiscale, eta, peso, analisi_effettuate, risultati_analisi):
        self.nome = nome
        self.cognome = cognome
        self.codice_fiscale = codice_fiscale
        self.eta = eta
        self.peso = peso
        self.risultati_analisi = risultati_analisi
        self.analisi_effettuate = analisi_effettuate
        self.risultati_analisi = np.array(risultati_analisi)

    def scheda_personale(self):
        return f"Nome: {self.nome}, Cognome: {self.cognome}, Codice Fiscale: {self.codice_fiscale}, Età: {self.eta}, Peso: {self.peso} kg, Analisi Effettuate: {', '.join(self.analisi_effettuate)}"
    
    def statistiche_analisi(self):
        # Qui usi le ufunc statistiche di NumPy sull'array self.risultati_analisi!
        media = np.mean(self.risultati_analisi)
        massimo = np.max(self.risultati_analisi)
        minimo = np.min(self.risultati_analisi)
        dev_std = np.std(self.risultati_analisi)
        
        print(f"--- Statistiche Cliniche per {self.nome} {self.cognome} ---")
        print(f"Media dei valori: {media:.2f}")
        print(f"Valore Massimo: {massimo} | Valore Minimo: {minimo}")
        print(f"Deviazione Standard: {dev_std:.2f}")
        print("-" * 50)

class Medico:
    def __init__(self, nome, cognome, specializzazione):
        self.nome = nome
        self.cognome = cognome
        self.specializzazione = specializzazione

    def visita_paziente(self, paziente):
        print(f"Il medico {self.nome} {self.cognome}, specializzato in {self.specializzazione}, sta visitando il paziente {paziente.nome} {paziente.cognome}.")

class Analisi:
    def __init__(self, tipo_analisi, risultato):
        self.tipo_analisi = tipo_analisi
        self.risultato = risultato

    def valuta(self):
        if self.tipo_analisi == "glicemia":
            if 70 <= self.risultato <= 99:
                return "Valore nella norma"
            else:
                return "Valore fuori norma"
        elif self.tipo_analisi == "colesterolo":
            if self.risultato < 200:
                return "Valore nella norma"
            else:
                return "Valore fuori norma"
        elif self.tipo_analisi == "pressione arteriosa":
            if 90 <= self.risultato <= 120:
                return "Valore nella norma"
            else:
                return "Valore fuori norma"
        else:
            return "Tipo di analisi non riconosciuto"
        
"""Parte 5  Applicazione completa
Creare un piccolo programma principale (main) che:
Inserisca almeno 3 medici e 5 pazienti.
Ogni paziente deve avere almeno 3 risultati di analisi.
Stampi la scheda di ogni paziente.
Mostri quale medico visita quale paziente.
Stampi le statistiche delle analisi per ciascun paziente."""

# 1. Creazione di un array NumPy isolato per 10 pazienti ipotetici
risultati_screening = np.array([85, 110, 95, 72, 130, 99, 105, 88, 91, 115])
print("=== PARTE 3: SCREENING GENERALE CASO STUDIO (10 Pazienti) ===")
print(f"Media screening: {np.mean(risultati_screening):.2f}")
print(f"Max: {np.max(risultati_screening)} | Min: {np.min(risultati_screening)}")
print(f"Deviazione Standard: {np.std(risultati_screening):.2f}\n" + "="*50 + "\n")


# 2. Programma principale con Medici e Pazienti reali 
medico1 = Medico("Andrea", "Verdi", "Cardiologia")
medico2 = Medico("Luisa", "Bianchi", "Medicina Generale")
medico3 = Medico("Marco", "Neri", "Endocrinologia")

# 5 pazienti (lista di 3 risultati analisi)
pazienti = [
    Paziente("Mario", "Rossi", "RSSMRA80A01H501Z", 40, 75.5, ["Emocromo", "Colesterolo", "Glicemia"], [95, 185, 88]),
    Paziente("Giulia", "Bianchi", "BNCGLI85B45H501Z", 35, 68.0, ["Emocromo", "Pressione arteriosa"], [115, 120, 110]),
    Paziente("Luca", "Verdi", "VRDLCU90C01H501Z", 50, 85.5, ["Glicemia", "Colesterolo"], [140, 230, 155]),
    Paziente("Elena", "Santi", "SNTLNE88R50F205W", 38, 58.4, ["Glicemia"], [105, 99, 101]),
    Paziente("Roberto", "Russo", "RSSRBT65T12H501X", 61, 90.2, ["Colesterolo"], [190, 210, 195])
]

print("=== 1. SCHEDE PERSONALI DEI PAZIENTI ===")
for p in pazienti:
    print(p.scheda_personale())

print("\n=== 2. DIARIO DELLE VISITE ===")
medico2.visita_paziente(pazienti[0])
medico1.visita_paziente(pazienti[1])
medico3.visita_paziente(pazienti[2])

print("\n=== 3. ELABORAZIONE STATISTICHE CLINICHE PER PAZIENTE ===")
for p in pazienti:
    p.statistiche_analisi()