import math
import pylab as pl
from matplotlib import pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

from heatmap import call

db = [[51.45111, 51.451247, 51.451438, 51.451441], [5.479317, 5.479945, 5.480229, 5.479414], [10, 5, 2, 20]]
y = db[0]  # location scanners LAT
x = db[1]  # location scanners LONG
users = db[2]  # n devices at location
# f = db[3]  # floor of the data set

# 1px=5.217391 cm   (verhouding BG: 1774 x 617 PX)

plotXmax = 1700
plotYmax = 610
q = 6, 3
lo_map = 0, 0
rb_map = plotXmax, plotYmax

min_lon = 5.47923
min_lat = 51.45139
max_lon = 5.48055
max_lat = 51.45098
"""
lo_geo = 51.451167, 5.478966
lb_geo = 51.451476, 5.479168
ro_geo = 51.451087, 5.480355
rb_geo = 51.451485, 5.480492
"""

DotScale = 5000  # int(round(9.82 * plotXmax, 0))
#  DotScale = int(round(3.82 * plotXmax, 0))
# Omreken factor coördinaten berekenen
m = max(users)

#API settings:
ur = "https://cloud.internalpositioning.com"
fam = "testdb"


def get_data(url, family):
    api_db = call.api_call(url, family)
    final_db = []
    i = 0
    if i < len(api_db):
        if "verdieping_0" in api_db["location"]:
            # bbox = * waardes *
            x_cord = api_db[""]
            final_db[0].append(api)


bbox = (min_lon, min_lat, max_lon, max_lat)


def heatmap(lat, long, c, cmap, vmin, vmax, imname, alph, s, pname, boundry):

    fig, ax = plt.subplots()
    ax.set_xlim(left=boundry[0], right=boundry[2],)
    ax.set_ylim(top=boundry[3], bottom=boundry[1])
    img = plt.imread(imname)
    ax.imshow(img, extent=[boundry[0], boundry[2], boundry[1], boundry[3]], origin=[5.47923, 51.45108])
    plt.title(pname)
    plot = ax.scatter(lat, long, s=s, alpha=alph, c=c, cmap=cmap, vmin=vmin, vmax=vmax, )

    plt.axis('off')

    divider = make_axes_locatable(ax)
    cax = divider.append_axes("right", size="5%", pad=0.05)
    cbar = plt.colorbar(plot, cax=cax)
    cbar.ax.get_yaxis().labelpad = 15
    cbar.ax.set_ylabel('aantal personen', rotation=270)

    a = "gevulde_" + imname


     #im.figsize = (18.5, 6.5)

    plt.savefig(a, dpi=320, transparent=True)
    print("Heatmap [" + imname + "] done.")


heatmap(lat=x, long=y, c=users, cmap=pl.cm.rainbow, boundry=bbox, vmin=1, vmax=m, imname="heatmap_bg.png", s=DotScale, alph=0.4, pname="Heatmap Begane Grond")

#FHICT 19/20 Infra | Proftaak Groep B, Team A: Tijn, Daan, Jimmy, Nassim, Mika, Luc, Thomas



