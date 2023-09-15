import matplotlib.pyplot as plt
import numpy as np
import os

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

WHITE = "#FFFFFF"
BLACK = "#000000"
BLUE = "#0077BB"
CYAN = "#009988"
GREEN = "#009988"
ORANGE = "#EE7733"
RED = "#CC3311"
MAGENTA = "#EE3377"
GREY = "#BBBBBB"

###############################################################################


def gibbs(x, f_alpha=None):
    if(f_alpha is None):
        f_alpha = np.zeros(x.shape)

    new_f_alpha = f_alpha[np.logical_not(np.isnan(f_alpha))]
    pdf = np.exp(-new_f_alpha)/np.sum(np.exp(-new_f_alpha))
    f_alpha[np.logical_not(np.isnan(f_alpha))] = pdf
    f_alpha[np.isnan(f_alpha)] = 0.0
    return f_alpha

###############################################################################

f_prior_list = np.array([1.0, 1.0, 1.0, 1.0, 1.0])
f_post_list = np.array([0.04, 0.1, 0.05, 0.1, 0.02])
f_prior_short_list = np.array([1.0, 1.0, 1.0])
f_post_short_list = np.array([0.04, 0.1, 0.05])

x_dict = {
    "prior": np.arange(0, 5),
    "post": np.arange(0, 5),
    "prior_short": np.arange(0, 3),
    "post_short": np.arange(0, 3)
}

dist_dict = {
    "prior": gibbs(x_dict["prior"], f_alpha=1.0*f_prior_list),
    "post": gibbs(x_dict["post"], f_alpha=10.0*f_post_list),
    "prior_short": gibbs(
        x_dict["prior_short"], f_alpha=1.0*f_prior_short_list),
    "post_short": gibbs(x_dict["post_short"], f_alpha=10.0*f_post_short_list),
}

y_max = np.max(np.concatenate([dist_dict["prior"], dist_dict["post"],
                               dist_dict["prior_short"],
                               dist_dict["post_short"]]))

for dist in ["prior", "post", "prior_short", "post_short"]:

    if(dist in ["prior", "post"]):
        fig, ax = plt.subplots(1, 1, figsize=(6, 1))
    elif(dist in ["prior_short", "post_short"]):
        fig, ax = plt.subplots(1, 1, figsize=(3, 1))

    if(dist == "prior"):
        ax.bar(x_dict["prior"], dist_dict["prior"],
               width=0.8, color=RED, alpha=0.8)
        ax.bar(x_dict["prior"], dist_dict["prior"],
               width=0.8, fill=None, edgecolor=RED, linewidth=1.0)
    elif(dist == "post"):
        ax.bar(x_dict["post"], dist_dict["post"],
               width=0.8, color=ORANGE, alpha=0.8)
        ax.bar(x_dict["post"], dist_dict["post"],
               width=0.8, fill=None, edgecolor=ORANGE, linewidth=1.0)
    elif(dist == "prior_short"):
        ax.bar(x_dict["prior_short"], dist_dict["prior_short"],
               width=0.8, color=RED, alpha=0.8)
        ax.bar(x_dict["prior_short"], dist_dict["prior_short"],
               width=0.8, fill=None, edgecolor=RED, linewidth=0.5)
    elif(dist == "post_short"):
        ax.bar(x_dict["post_short"], dist_dict["post_short"],
               width=0.8, color=ORANGE, alpha=0.8)
        ax.bar(x_dict["post_short"], dist_dict["post_short"],
               width=0.8, fill=None, edgecolor=ORANGE, linewidth=0.5)

    ax.set_ylim(0.0, y_max)
    if(dist in ["prior", "prior_short"]):
        ax.set_ylabel(r"Prior $\P$")
    elif(dist in ["post", "post_short"]):
        ax.set_ylabel(r"Posterior $\AQ$")

    if(dist in ["prior", "post"]):
        ax.set_xticks(
            x_dict[dist], [r"$h_1$", r"$h_2$", r"$h_3$", r"$h_4$", r"$h_5$"])
    elif(dist in ["prior_short", "post_short"]):
        ax.set_xticks(x_dict[dist], [r"$h_1$", r"$h_2$", r"$h_3$"])

    ax.spines.right.set_visible(False)
    ax.spines.top.set_visible(False)
    ax.tick_params(left=False, labelleft=False,
                   bottom=False)

    os.makedirs("figures/", exist_ok=True)
    fig.savefig(f"figures/distribution_{dist}.pdf", bbox_inches="tight")
