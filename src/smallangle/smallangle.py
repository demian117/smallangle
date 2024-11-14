import click
import numpy as np
from numpy import pi
import pandas as pd

@click.group()
def cmd_group():
    pass

@cmd_group.command()
@click.option(
    "-n",
    "--number",
    default=10,
    help="Number of steps to calculate the sin for.",
    show_default=True,  # show default in help
)
def sin(number):
    """Calculate the sine of NUMBER values between 0 and 2 pi.

    NUMBER is the number of steps to calculate the sin for.
    """
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)

@cmd_group.command()
@click.option(
    "-n",
    "--number",
    default=10,
    help="Number of steps to calculate the tan for.",
    show_default=True,  # show default in help
)
def tan(number):
    """Calculate the tangent of NUMBER values between 0 and 2 pi.

    NUMBER is the number of steps to calculate the sin for.
    """
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)

if __name__ == "__main__":
    cmd_group()