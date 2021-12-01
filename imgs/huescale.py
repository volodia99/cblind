nx=100
x=np.linspace(0,5, nx)
option = ["blue", "bluegreen", "green", "gold", "brown", "rose", "purple"]

fig, ax = plt.subplots(nrows=4, ncols=2, figsize=(8,10))
p = 0
ny = 9
y=np.zeros((ny,nx), dtype=int)
color, linestyle = cb.Colorplots().huescale(ny)
for i in range(ny):
    y[i]=x+i
    ax[0,0].plot(x,y[i],color=color[i], ls="-")
ny = 3
y=np.zeros((ny,nx), dtype=int)
color, linestyle = cb.Colorplots().huescale(ny, option[0])
for i in range(ny):
    y[i]=x+i
    ax[0,1].plot(x,y[i],color=color[i], ls="-")
ax[0,0].set_title("ocherscale", fontsize=10, loc="right", font="monospace", color="k")
ax[0,1].set_title(f"option = {option[0]}", fontsize=10, loc="right", font="monospace", color="k")
ax[0,0].set_axis_off()
ax[0,1].set_axis_off()
for p, (axi,axj) in zip(range(1,8,2),ax[1:,:]):
    ny = 3
    y=np.zeros((ny,nx), dtype=int)
    color, linestyle = cb.Colorplots().huescale(ny, option[p])
    for i in range(ny):
        y[i]=x+i
        axi.plot(x,y[i], color=color[i])
    color, linestyle = cb.Colorplots().huescale(ny, option[p+1])
    for i in range(ny):
        y[i]=x+i
        axj.plot(x,y[i], color=color[i])
    axi.set_title(f"option = {option[p]}", fontsize=10, loc="right", font="monospace", color="k")
    axj.set_title(f"option = {option[p+1]}", fontsize=10, loc="right", font="monospace", color="k")
    axi.set_axis_off()
    axj.set_axis_off()
fig.tight_layout()
plt.savefig("huescale.png", dpi=100, facecolor='lightgray')
