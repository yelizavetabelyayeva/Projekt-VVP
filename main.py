from fraktal import generate_mandelbrot, generate_julia

import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, RadioButtons


def main():
    width, height = 600, 600
    xmin, xmax = -2.0, 1.0
    ymin, ymax = -1.5, 1.5
    initial_iter = 100
    initial_c_re = -0.8
    initial_c_im = 0.156

    fig, ax = plt.subplots(figsize=(6, 6))
    plt.subplots_adjust(left=0.25, bottom=0.35)

    data = generate_mandelbrot(
        xmin, xmax, ymin, ymax,
        width, height, initial_iter
    )

    img = ax.imshow(
        data,
        extent=(xmin, xmax, ymin, ymax),
        cmap='plasma',
        origin='lower'
    )

    ax.set_title("Fraktál")
    ax.set_xlabel("Re")
    ax.set_ylabel("Im")

    ax_iter = plt.axes([0.25, 0.2, 0.65, 0.03])
    slider_iter = Slider(
        ax_iter, 'Iterace', 10, 1000,
        valinit=initial_iter, valstep=10
    )

    ax_c_re = plt.axes([0.25, 0.15, 0.65, 0.03])
    slider_c_re = Slider(
        ax_c_re, 'Re(c)', -1.5, 1.5,
        valinit=initial_c_re, valstep=0.01
    )

    ax_c_im = plt.axes([0.25, 0.1, 0.65, 0.03])
    slider_c_im = Slider(
        ax_c_im, 'Im(c)', -1.5, 1.5,
        valinit=initial_c_im, valstep=0.01
    )

    ax_radio = plt.axes([0.025, 0.5, 0.15, 0.15])
    radio = RadioButtons(ax_radio, ('Mandelbrot', 'Julia'))

    def update(val):
        max_iter = int(slider_iter.val)
        c_re = slider_c_re.val
        c_im = slider_c_im.val
        fractal_type = radio.value_selected

        if fractal_type == 'Mandelbrot':
            data = generate_mandelbrot(
                xmin, xmax, ymin, ymax,
                width, height, max_iter
            )
        else:
            data = generate_julia(
                xmin, xmax, ymin, ymax,
                width, height, max_iter,
                c_re, c_im
            )

        img.set_data(data)
        img.set_clim(0, max_iter)
        fig.canvas.draw_idle()

    slider_iter.on_changed(update)
    slider_c_re.on_changed(update)
    slider_c_im.on_changed(update)
    radio.on_clicked(update)

    plt.show()


if __name__ == "__main__":
    main()

