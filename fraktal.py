import numpy as np
from numba import jit


@jit(nopython=True)
def generate_mandelbrot(
    xmin: float, xmax: float,
    ymin: float, ymax: float,
    width: int, height: int,
    max_iter: int
) -> np.ndarray:
    """
    Generuje 2D pole počtů iterací pro Mandelbrotovu množinu.

    Každý bod komplexní roviny je testován pomocí vztahu:
    z_{n+1} = z_n^2 + c

    Pro Mandelbrotovu množinu platí:
    z_0 = 0
    c je aktuální bod komplexní roviny.
    """

    # Vytvoření prázdného pole pro výsledný obrázek
    image = np.zeros((height, width))

    # Procházíme všechny pixely obrázku
    for i in range(height):
        for j in range(width):

            # Převod souřadnic pixelu na bod v komplexní rovině
            x0 = xmin + j * (xmax - xmin) / width
            y0 = ymin + i * (ymax - ymin) / height

            # Počáteční hodnota z je 0
            x, y = 0.0, 0.0

            # Počítadlo iterací
            iteration = 0

            # Iterujeme, dokud bod nepřekročí hranici divergence
            # nebo dokud nedosáhneme maximálního počtu iterací
            while x * x + y * y <= 4 and iteration < max_iter:

                # Výpočet reálné části z_{n+1}
                x_new = x * x - y * y + x0

                # Výpočet imaginární části z_{n+1}
                y = 2 * x * y + y0

                # Aktualizace reálné části
                x = x_new

                iteration += 1

            # Uložení počtu iterací do výsledného pole
            image[i, j] = iteration

    return image


@jit(nopython=True)
def generate_julia(
    xmin: float, xmax: float,
    ymin: float, ymax: float,
    width: int, height: int,
    max_iter: int,
    c_re: float, c_im: float
) -> np.ndarray:
    """
    Generuje 2D pole počtů iterací pro Juliovu množinu.

    Pro Juliovu množinu platí:
    z_0 je aktuální bod komplexní roviny
    c je pevně zvolená komplexní konstanta.
    """

    # Vytvoření prázdného pole pro výsledný obrázek
    image = np.zeros((height, width))

    # Procházíme všechny pixely obrázku
    for i in range(height):
        for j in range(width):

            # Převod souřadnic pixelu na počáteční bod z_0
            x = xmin + j * (xmax - xmin) / width
            y = ymin + i * (ymax - ymin) / height

            # Počítadlo iterací
            iteration = 0

            # Iterujeme podle vztahu z_{n+1} = z_n^2 + c
            while x * x + y * y <= 4 and iteration < max_iter:

                # Výpočet reálné části
                x_new = x * x - y * y + c_re

                # Výpočet imaginární části
                y = 2 * x * y + c_im

                # Aktualizace reálné části
                x = x_new

                iteration += 1

            # Uložení počtu iterací do výsledného pole
            image[i, j] = iteration

    return image