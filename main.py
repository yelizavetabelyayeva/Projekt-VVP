# Import výpočetních funkcí pro generování fraktálů
from fraktal import generate_mandelbrot, generate_julia

# Import přednastavených hodnot pro Juliovu množinu
from presets import JULIA_PRESETS

# Import knihoven pro vykreslování a interaktivní prvky
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, RadioButtons, Button


def main():

    # Počáteční rozlišení vykreslení
    width, height = 600, 600

    # Rozsah komplexní roviny
    xmin, xmax = -2.0, 1.0
    ymin, ymax = -1.5, 1.5

    # Výchozí hodnoty parametrů
    initial_iter = 100
    initial_c_re = -0.8
    initial_c_im = 0.156
    initial_cmap = "plasma"

    # Vytvoření hlavního okna grafu
    fig, ax = plt.subplots(figsize=(7, 6))

    # Nastavení prostoru pro interaktivní prvky
    plt.subplots_adjust(left=0.25, bottom=0.38)

    # Vygenerování počáteční Mandelbrotovy množiny
    data = generate_mandelbrot(
        xmin,
        xmax,
        ymin,
        ymax,
        width,
        height,
        initial_iter
    )

    # Vykreslení fraktálu
    img = ax.imshow(
        data,
        extent=(xmin, xmax, ymin, ymax),
        cmap=initial_cmap,
        origin="lower"
    )

    # Popis os a název grafu
    ax.set_title("Mandelbrotova množina")
    ax.set_xlabel("Re")
    ax.set_ylabel("Im")

    # Slider pro změnu počtu iterací
    ax_iter = plt.axes([0.25, 0.25, 0.65, 0.03])

    slider_iter = Slider(
        ax_iter,
        "Iterace",
        10,
        1000,
        valinit=initial_iter,
        valstep=10
    )

    # Slider pro reálnou část konstanty c
    ax_c_re = plt.axes([0.25, 0.19, 0.65, 0.03])

    slider_c_re = Slider(
        ax_c_re,
        "Re(c)",
        -1.5,
        1.5,
        valinit=initial_c_re,
        valstep=0.01
    )

    # Slider pro imaginární část konstanty c
    ax_c_im = plt.axes([0.25, 0.13, 0.65, 0.03])

    slider_c_im = Slider(
        ax_c_im,
        "Im(c)",
        -1.5,
        1.5,
        valinit=initial_c_im,
        valstep=0.01
    )

    # Přepínání mezi Mandelbrotovou a Juliovou množinou
    ax_radio_type = plt.axes([0.025, 0.62, 0.16, 0.12])

    radio_type = RadioButtons(
        ax_radio_type,
        ("Mandelbrot", "Julia")
    )

    # Výběr barevného schématu
    ax_radio_cmap = plt.axes([0.025, 0.39, 0.16, 0.18])

    radio_cmap = RadioButtons(
        ax_radio_cmap,
        ("plasma", "viridis", "inferno", "magma")
    )

    # Výběr přednastavených hodnot pro Juliovu množinu
    ax_presets = plt.axes([0.025, 0.11, 0.16, 0.24])

    radio_presets = RadioButtons(
        ax_presets,
        tuple(JULIA_PRESETS.keys())
    )

    # Tlačítko pro reset parametrů
    ax_reset = plt.axes([0.025, 0.03, 0.16, 0.06])

    button_reset = Button(
        ax_reset,
        "Reset"
    )

    # Funkce pro aktualizaci fraktálu
    def update(_=None):

        # Načtení aktuálních hodnot sliderů
        max_iter = int(slider_iter.val)
        c_re = slider_c_re.val
        c_im = slider_c_im.val

        # Výběr typu fraktálu
        fractal_type = radio_type.value_selected

        # Výběr barevného schématu
        cmap = radio_cmap.value_selected

        # Generování Mandelbrotovy množiny
        if fractal_type == "Mandelbrot":

            new_data = generate_mandelbrot(
                xmin,
                xmax,
                ymin,
                ymax,
                width,
                height,
                max_iter
            )

            ax.set_title("Mandelbrotova množina")

        # Generování Juliovy množiny
        else:

            new_data = generate_julia(
                xmin,
                xmax,
                ymin,
                ymax,
                width,
                height,
                max_iter,
                c_re,
                c_im
            )

            ax.set_title(
                f"Juliova množina, c = {c_re:.2f} + {c_im:.2f}i"
            )

        # Aktualizace vykreslených dat
        img.set_data(new_data)

        # Změna barevné mapy
        img.set_cmap(cmap)

        # Aktualizace rozsahu barev
        img.set_clim(0, max_iter)

        # Překreslení okna
        fig.canvas.draw_idle()

    # Funkce pro načtení přednastavených hodnot Juliovy množiny
    def apply_preset(label):

        # Načtení hodnot c podle zvoleného presetu
        c_re, c_im = JULIA_PRESETS[label]

        # Nastavení hodnot do sliderů
        slider_c_re.set_val(c_re)
        slider_c_im.set_val(c_im)

        # Automatické přepnutí na Juliovu množinu
        radio_type.set_active(1)

        update()

    # Funkce pro reset všech parametrů
    def reset(_):

        slider_iter.reset()
        slider_c_re.reset()
        slider_c_im.reset()

        radio_type.set_active(0)
        radio_cmap.set_active(0)

        update()

    # Připojení interaktivních prvků k funkcím
    slider_iter.on_changed(update)
    slider_c_re.on_changed(update)
    slider_c_im.on_changed(update)

    radio_type.on_clicked(update)
    radio_cmap.on_clicked(update)
    radio_presets.on_clicked(apply_preset)

    button_reset.on_clicked(reset)

    # Zobrazení grafického okna
    plt.show()


# Spuštění hlavní části programu
if __name__ == "__main__":
    main()