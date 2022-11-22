import matplotlib.pyplot as plt
import numpy as np
from src.aoc22.dataloader import DataLoader


def example_function():
    """
    example function.
    :return:
    """
    dataloader = DataLoader()
    dataloader.__init__()
    x = np.linspace(0, np.pi, 100)
    sin = np.sin(x)

    my_ax = plt.subplots(1, 1)[1]
    my_ax.plot(x, sin)
    my_ax.set_title("sinus")
    my_ax.set_xlabel("x")
    my_ax.set_ylabel("sin")
    my_ax.grid("on")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    example_function()
