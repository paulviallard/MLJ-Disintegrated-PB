import os
import sys
import matplotlib.pyplot as plt

sys.path.append("../")
from core.nd_data import NDData

###############################################################################

path = os.path.dirname(os.path.abspath(__file__))+"/"

f = open("slides.tex", "r")
preamble = f.read()
preamble = preamble.replace("\\input{", "\\input{"+path)

plt.rcParams.update({
    "font.size": 10,
    "text.usetex": True,
    "text.latex.preamble": preamble,
    "pgf.preamble": preamble,
    "font.family": "sans-serif",
    "font.sans-serif": "Open Sans",
})

###############################################################################

BLACK = "#000000"
BLUE = "#0077BB"
CYAN = "#009988"
GREEN = "#009988"
ORANGE = "#EE7733"
RED = "#CC3311"
MAGENTA = "#EE3377"
GREY = "#BBBBBB"

###############################################################################

if __name__ == "__main__":

    fig, ax = plt.subplots(1, 1, figsize=((1, 2.5)))

    ax.bar(0, 0.1, hatch=r"\\", color=GREEN)
    ax.bar(0, 0.2, hatch=r"\\", fill=False)
    plt.axis('off')

    os.makedirs("figures/", exist_ok=True)
    plt.savefig(f"figures/comparison_legend.pdf", bbox_inches="tight")
