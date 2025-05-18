import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from numba import jit

# -----------------------------------------------------------------------------
# FUNKCE: Generování Mandelbrotovy množiny
# -----------------------------------------------------------------------------

@jit(nopython=True)
def generate_mandelbrot(
    xmin: float, xmax: float,
    ymin: float, ymax: float,
    width: int, height: int,
    max_iter: int
):
    """
    Generuje 2D pole s hodnotami iterací Mandelbrotovy množiny.

    Parametry:
        xmin, xmax: hranice na reálné ose
        ymin, ymax: hranice na imaginární ose
        width, height: rozměry obrázku v pixelech
        max_iter: maximální počet iterací

    Návratová hodnota:
        2D NumPy pole s hodnotami iterací pro každý bod
    """
    image = np.zeros((height, width))
    
    for i in range(height):
        for j in range(width):
            x0 = xmin + j * (xmax - xmin) / width
            y0 = ymin + i * (ymax - ymin) / height
            x, y = 0.0, 0.0
            iteration = 0
            
            while x * x + y * y <= 4 and iteration < max_iter:
                x_new = x * x - y * y + x0
                y = 2 * x * y + y0
                x = x_new
                iteration += 1
            
            image[i, j] = iteration
    
    return image

# -----------------------------------------------------------------------------
# FUNKCE: Spuštění hlavní části programu
# -----------------------------------------------------------------------------

def main():
    """
    Hlavní funkce programu – nastaví grafické rozhraní
    a zobrazí Mandelbrotovu množinu.
    """
    # Parametry obrázku a fraktálu
    width, height = 600, 600
    xmin, xmax = -2.0, 1.0
    ymin, ymax = -1.5, 1.5
    initial_iter = 100

    # Vytvoření grafického okna
    fig, ax = plt.subplots(figsize=(6, 6))
    plt.subplots_adjust(left=0.1, bottom=0.25)

    # Počáteční výpočet dat
    data = generate_mandelbrot(xmin, xmax, ymin, ymax, width, height, initial_iter)
    img = ax.imshow(data, extent=(xmin, xmax, ymin, ymax), cmap='plasma', origin='lower')
    ax.set_title("Mandelbrotova množina")
    ax.set_xlabel("Re(c)")
    ax.set_ylabel("Im(c)")

    # Přidání posuvníku pro změnu iterací
    ax_slider = plt.axes([0.2, 0.1, 0.6, 0.03])
    slider_iter = Slider(
        ax=ax_slider,
        label='Max Iterací',
        valmin=10,
        valmax=1000,
        valinit=initial_iter,
        valstep=10
    )

    # Funkce pro aktualizaci obrazu při změně hodnoty
    def update(val: float) -> None:
        """
        Aktualizuje zobrazený fraktál podle nové hodnoty iterací.
        """
        new_iter: int = int(slider_iter.val)
        new_data = generate_mandelbrot(xmin, xmax, ymin, ymax, width, height, new_iter)
        img.set_data(new_data)
        img.set_clim(0, new_iter)
        fig.canvas.draw_idle()

    # Připojení funkce k posuvníku
    slider_iter.on_changed(update)

    # Zobrazení
    plt.show()


# -----------------------------------------------------------------------------
# Spuštění hlavní funkce
# -----------------------------------------------------------------------------

if __name__ == "__main__":
    main()
