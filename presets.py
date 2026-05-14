"""
Soubor obsahuje přednastavené hodnoty
pro Juliovu množinu.

Každý preset představuje komplexní konstantu c,
která vytváří odlišný tvar fraktálu.
"""

# Slovník přednastavených parametrů
# Formát:
# "Název": (reálná část, imaginární část)

JULIA_PRESETS = {

    # Klasický tvar Juliovy množiny
    "Classic": (-0.8, 0.156),

    # Spirálovitý tvar
    "Spiral": (0.285, 0.01),

    # Symetrický vzor
    "Symmetry": (-0.4, 0.6),

    # Jemná struktura
    "Cloud": (-0.70176, -0.3842),

    # Výrazně členitý tvar
    "Dragon": (-0.835, -0.2321),

    # Organický vzhled
    "Flower": (0.355, 0.355),

    # Komplexnější detailní struktura
    "Lightning": (-0.54, 0.54)
}