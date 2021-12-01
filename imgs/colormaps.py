import numpy as np
import matplotlib.pyplot as plt
import cblind as cb

x = np.repeat(np.linspace(0,1,256),15).reshape(256,15).T
PALETTES = ["cb.rainbow", "cb.extreme_rainbow", "cb.iris", "cb.huescale", "cb.rbscale", "cb.solstice", "cb.bird", "cb.pregunta"]
plt.figure(figsize=(8,10))
maps = [m for m in PALETTES]
l = len(maps)+1
for i, m in enumerate(maps):
    plt.subplot(l,1,i+1)
    plt.axis("off")
    plt.imshow(x, aspect='auto', cmap=cb.cbmap(m), origin="lower")
    plt.title(m, fontsize=10, loc="right", font="monospace", color="w")
plt.tight_layout()
plt.savefig("colormaps.png", dpi=100, facecolor='black')
