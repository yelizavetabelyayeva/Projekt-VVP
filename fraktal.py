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


@jit(nopython=True)
def generate_julia(
    xmin: float, xmax: float,
    ymin: float, ymax: float,
    width: int, height: int,
    max_iter: int,
    c_re: float, c_im: float
) -> np.ndarray:
    """
    Generuje 2D pole počtů iterací pro Julii množinu.
    """
    image = np.zeros((height, width))
    for i in range(height):
        for j in range(width):
            x = xmin + j * (xmax - xmin) / width
            y = ymin + i * (ymax - ymin) / height
            iteration = 0
            while x * x + y * y <= 4 and iteration < max_iter:
                x_new = x * x - y * y + c_re
                y = 2 * x * y + c_im
                x = x_new
                iteration += 1
            image[i, j] = iteration
    return image
