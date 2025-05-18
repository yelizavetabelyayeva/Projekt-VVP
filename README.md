# Vizualizace fraktálu

Tento projekt je zaměřený na vizualizaci fraktálu Mandelbrotovy množiny.  
Program je napsaný v jazyce Python a umožňuje interaktivně měnit počet iterací pomocí posuvníku. Výsledek se hned překreslí na obrazovce.

## Co program dělá

- Vykreslí obrázek Mandelbrotovy množiny podle daného vzorce  
- Pomocí posuvníku (Slider) se dá nastavit počet iterací  
- Čím víc iterací, tím detailnější výsledek  
- Všechno běží v jednoduchém grafickém okně (matplotlib)

## Jak program spustit

1. Otevřít terminál ve složce s projektem
2. Vytvořit a aktivovat virtuální prostředí:
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Nainstalovat potřebné knihovny:
   ```
   pip install -r requirements.txt
   ```
4. Spustit program:
   ```
   python main.py
   ```

Po spuštění se zobrazí okno s fraktálem a dole posuvník.

## Použité knihovny

- `numpy`  
- `matplotlib`  
- `numba`

Všechny knihovny se nainstalují automaticky pomocí `requirements.txt`.

## Co se dá změnit

- Rozlišení obrázku (`width`, `height`)  
- Souřadnice oblasti (`xmin`, `xmax`, `ymin`, `ymax`)  
- Počet iterací (`initial_iter`)  
- Barevné schéma (`cmap` – např. `'hot'`, `'plasma'`, `'inferno'`)

## Složení projektu

- `main.py` – hlavní skript  
- `requirements.txt` – potřebné knihovny  
- `README.md` – tento soubor  
- `projekt.ipynb` – volitelný notebook s ukázkou

## Autorka
Belyayeva Yelizaveta   
Projekt z Vědecké výpočty v Pythonu (VVP) 