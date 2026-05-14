# Vizualizace fraktálů: Mandelbrotova a Juliova množina

## Popis projektu

Tento projekt je zaměřen na generování a interaktivní vizualizaci
fraktálů v komplexní rovině pomocí programovacího jazyka Python.

Projekt implementuje dva známé typy fraktálů:

- Mandelbrotovu množinu
- Juliovu množinu

Fraktály jsou generovány pomocí iterativního vztahu:

z_{n+1} = z_n^2 + c 

kde:
- z je komplexní číslo
- c je konstanta v komplexní rovině

Program umožňuje uživateli interaktivně měnit parametry výpočtu
a sledovat změny fraktálu v reálném čase.

---

# Použité knihovny

Projekt využívá následující knihovny:

- NumPy
- Matplotlib
- Numba
- ipywidgets

Knihovna NumPy slouží pro práci s numerickými poli,
Matplotlib pro vykreslování grafiky,
Numba pro zrychlení výpočtů pomocí JIT kompilace
a ipywidgets pro interaktivní ovládání parametrů.

---

# Funkcionalita programu

Program umožňuje:

- generování Mandelbrotovy množiny
- generování Juliovy množiny
- změnu počtu iterací
- změnu parametrů komplexní konstanty c
- přepínání mezi Mandelbrotovou a Juliovou množinou
- interaktivní ovládání pomocí Sliderů a RadioButtons
- barevné vykreslení podle rychlosti divergence bodů

---

# Struktura projektu

## main.py
Hlavní soubor programu.
Obsahuje vytvoření grafického okna,
interaktivní prvky a vykreslení fraktálu.

## fraktal.py
Obsahuje výpočetní algoritmy pro:
- Mandelbrotovu množinu
- Juliovu množinu

Výpočty jsou optimalizovány pomocí knihovny Numba.

## projekt.ipynb
Jupyter Notebook verze projektu.
Slouží pro interaktivní testování a demonstraci programu.

## requirements.txt
Obsahuje seznam potřebných knihoven.

---

# Princip fungování

Každý bod komplexní roviny je iterativně testován.
Pokud hodnota posloupnosti překročí zvolený práh,
bod diverguje a je obarven podle počtu iterací.

Body, které zůstávají omezené,
jsou považovány za součást fraktálové množiny.

---

# Spuštění projektu

## Instalace knihoven

```bash
pip install -r requirements.txt

