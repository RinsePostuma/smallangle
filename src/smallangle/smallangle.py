import click
import numpy as np
from numpy import pi
import pandas as pd

@click.group()
def smallangle():
    """ A tool to calculate the outcomes of sinus and tangent between 0 and 2 pi """
    pass
@smallangle.command()
@click.option("-n", "--number", default=50, show_default=True, help="Number of steps between 0 and 2 pi")
def sin(number):
    """Generate a list of x and sin(x) between 0 and 2 pi

    Args:
        number (int): number of steps between 0 and 2 pi
    """    
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)

@smallangle.command()
@click.option("-n", "--number", default=50, show_default=True, help="Number of steps between 0 and 2 pi")
def tan(number):
    """Generate a list of x and sin(x) between 0 and 2 pi

    Args:
        number (int): number of steps between 0 and 2 pi
    """
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)

if __name__ == "__main__":
    smallangle()