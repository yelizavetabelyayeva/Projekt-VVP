# Vizualizace fraktálů: Mandelbrotova a Juliova množina

Tento projekt je zaměřený na vizualizaci dvou klasických fraktálů v komplexní rovině:
- Mandelbrotova množina
- Juliova množina

Program je napsaný v jazyce Python a využívá knihovny numpy, matplotlib, numba a ipywidgets.  
Cílem je umožnit uživateli generovat fraktály efektivně, interaktivně měnit parametry a sledovat jejich vliv na tvar množiny.

---

## Co program dělá

- Vypočítává a vykresluje Mandelbrotovu a Juliovu množinu podle iterativního vzorce:  
  \[
  z_{n+1} = z_n^2 + c
  \]
- Umožňuje volit mezi Mandelbrotovou a Juliovou množinou pomocí přepínače
- V případě Juliovy množiny umožňuje měnit hodnoty komplexní konstanty \( c \)
- Používá knihovnu Numba pro zrychlení výpočtu (JIT kompilace)
- Obsahuje interaktivní posuvníky (Slider) a výběr barevné mapy pomocí ipywidgets
- Vizualizace funguje:
  - ve skriptu main.py s Matplotlib
  - i v Jupyter Notebooku projekt.ipynb s interaktivním ovládáním

---

## Struktura projektu

- main.py – hlavní skript pro spuštění interaktivní vizualizace (Mandelbrot/Julia)
- fraktal.py – obsahuje výpočetní funkce pro obě množiny
- projekt.ipynb – interaktivní Jupyter notebook s možností ovládání přes posuvníky
- requirements.txt – seznam potřebných knihoven
- README.md – tento popis projektu

---

## Instalace a spuštění

1. Nainstaluj všechny potřebné knihovny:
pip install -r requirements.txt


2. Spusť projekt v Jupyter Notebooku:
jupyter notebook


3. Otevři soubor projekt.ipynb a spusť jednotlivé buňky.

---

## Shrnutí

Tento projekt demonstruje interaktivní výpočet a vizualizaci fraktálů v Pythonu.  
Uživatel může volit mezi dvěma množinami, měnit parametry jako počet iterací nebo konstantu \( c \),  
a sledovat změny v reálném čase. Výpočetní část je optimalizována pomocí knihovny Numba  
a vizualizace probíhá přes Matplotlib a ipywidgets.

---

Autorka  
Yelizaveta Belyayeva  
Projekt vypracovaný pro předmět *Vědecké výpočty v Pythonu (VVP)*