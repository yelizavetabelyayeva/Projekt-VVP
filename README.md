# Vizualizace fraktálů: Mandelbrotova a Juliova množina

## Popis projektu

Tento projekt je zaměřen na generování a interaktivní vizualizaci
fraktálů v komplexní rovině pomocí programovacího jazyka Python.

Projekt implementuje dva známé typy fraktálů:

- Mandelbrotovu množinu
- Juliovu množinu

Fraktály jsou generovány pomocí iterativního vztahu:

$$
z_{n+1} = z_n^2 + c
$$

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

## Spuštění programu

```bash
python main.py
```

Po spuštění programu se otevře grafické okno
s interaktivní vizualizací fraktálu.

## Spuštění Jupyter Notebooku

```bash
jupyter notebook
```

Poté otevřít soubor:

```text
projekt.ipynb
```

---

# Interaktivní ovládání

Projekt obsahuje interaktivní prvky,
které umožňují uživateli měnit parametry programu
v reálném čase.

Použité prvky:
- Slider pro změnu počtu iterací
- Slider pro změnu reálné části konstanty c
- Slider pro změnu imaginární části konstanty c
- RadioButtons pro přepínání mezi Mandelbrotovou
  a Juliovou množinou

Po změně parametrů se fraktál automaticky překreslí.

---

# Možná rozšíření projektu

Projekt je možné dále rozšířit například o:

- realtime zoom
- ukládání obrázků
- změnu barevných schémat
- další typy fraktálů
- ovládání pomocí myši a klávesnice
- animace přibližování

---

# Závěr

Projekt demonstruje využití programovacího jazyka Python
pro numerické výpočty a interaktivní vizualizaci
matematických objektů.

Součástí projektu je:
- práce s komplexními čísly
- optimalizace výpočtů
- grafická vizualizace
- interaktivní ovládání parametrů
- využití numerických knihoven Pythonu

Projekt zároveň ukazuje možnosti knihoven
NumPy, Matplotlib a Numba při práci
s matematickými simulacemi a vizualizacemi.

---

# Informace o projektu

Předmět: Vědecké výpočty v Pythonu (VVP)

Akademický rok: 2025/2026

---
# Autor

Jméno: Belyayeva Yelizaveta

Login: BEL0178
